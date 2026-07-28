#!/usr/bin/env python3
"""Canonical, dependency-free AHIF repository verification engine."""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "automation.config.json"
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
STATUS_EXIT = {"pass": 0, "hold": 0, "fail": 1, "internal_error": 2}


class ConfigError(ValueError):
    pass


def git(root: Path, *args: str) -> str:
    proc = subprocess.run(["git", *args], cwd=root, text=True, capture_output=True)
    return proc.stdout.strip() if proc.returncode == 0 else "unknown"


def rel(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def tracked_files(root: Path) -> list[Path]:
    if (root / ".git").exists():
        proc = subprocess.run(["git", "ls-files", "-z"], cwd=root, check=True, capture_output=True)
        return sorted((root / item.decode()) for item in proc.stdout.split(b"\0") if item and (root / item.decode()).is_file())
    ignored = {".git", ".artifacts", "__pycache__"}
    return sorted(p for p in root.rglob("*") if p.is_file() and not ignored.intersection(p.parts))


def load_config(path: Path = CONFIG_PATH, root: Path = ROOT) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ConfigError(f"configuration unreadable: {exc}") from exc
    required = {"schema_version", "version", "sprint", "metadata_files", "source_of_truth_files", "required_modules", "completion_artifacts", "required_workflows", "required_scripts", "required_registries", "reports", "ignored_fixture_paths", "claim_boundary_phrases", "exit_codes"}
    missing = sorted(required - data.keys())
    if missing:
        raise ConfigError(f"missing configuration keys: {', '.join(missing)}")
    list_keys = sorted(required - {"schema_version", "version", "sprint", "reports", "exit_codes"})
    for key in list_keys:
        values = data[key]
        if not isinstance(values, list) or any(not isinstance(v, str) or not v for v in values):
            raise ConfigError(f"{key} must be a list of non-empty strings")
        duplicates = sorted({v for v in values if values.count(v) > 1})
        if duplicates:
            raise ConfigError(f"duplicate {key} entries: {', '.join(duplicates)}")
    if data["exit_codes"] != {"PASS": 0, "HOLD": 0, "FAIL": 1, "INTERNAL_ERROR": 2}:
        raise ConfigError("invalid exit-code mappings")
    report_values = list(data["reports"].values()) if isinstance(data["reports"], dict) else []
    all_paths = [*data["metadata_files"], *data["source_of_truth_files"], *data["required_modules"], *data["completion_artifacts"], *data["required_workflows"], *data["required_scripts"], *data["required_registries"], *report_values]
    for value in all_paths:
        p = PurePosixPath(value)
        if p.is_absolute() or ".." in p.parts or "\\" in value:
            raise ConfigError(f"path must be normalized and repository-relative: {value}")
    for value in [*data["metadata_files"], *data["source_of_truth_files"], *data["completion_artifacts"], *data["required_workflows"], *data["required_scripts"], *data["required_registries"]]:
        if not (root / value).is_file():
            raise ConfigError(f"unknown required path: {value}")
    for value in data["required_modules"]:
        if not (root / value).is_dir():
            raise ConfigError(f"unknown required module: {value}")
    return data


class Engine:
    def __init__(self, root: Path, config: dict[str, Any], machine: bool = False, verbose: bool = False):
        self.root, self.config, self.machine, self.verbose = root, config, machine, verbose
        self.files = tracked_files(root)
        self.sha = git(root, "rev-parse", "HEAD")
        self.timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        self.report_dir = root / PurePosixPath(config["reports"]["directory"])

    def emit(self, kind: str, checks: dict[str, list[str]], status: str | None = None, warnings: list[str] | None = None, output: Path | None = None, extra: dict[str, Any] | None = None) -> int:
        failures = sorted(f"{name}: {message}" for name, messages in checks.items() for message in messages)
        final = status or ("fail" if failures else "pass")
        if failures:
            final = "fail"
        data = {"schema": "ahif.verification-report", "schema_version": "2.0", "report_type": kind, "generated_at": self.timestamp, "commit_sha": self.sha, "checks_executed": [{"name": name, "status": "fail" if checks[name] else "pass"} for name in sorted(checks)], "status": final, "warnings": sorted(warnings or []), "failures": failures, "exit_code": STATUS_EXIT[final]}
        if extra:
            data.update(extra)
        if output:
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        if self.machine:
            print(json.dumps(data, sort_keys=True, separators=(",", ":")))
        else:
            print(f"{final.upper()} {kind}: {len(checks)} checks, {len(failures)} failures")
            if self.verbose:
                for item in failures: print(f"  - {item}")
        return STATUS_EXIT[final]

    def json_errors(self) -> list[str]:
        errors = []
        for path in self.files:
            if path.suffix == ".json":
                try: json.loads(path.read_text(encoding="utf-8"))
                except (OSError, UnicodeError, json.JSONDecodeError) as exc: errors.append(f"invalid JSON: {rel(path, self.root)}: {exc}")
        return errors

    def manifest_errors(self) -> list[str]:
        errors = []
        try: manifest = json.loads((self.root / "manifest.json").read_text(encoding="utf-8"))
        except Exception as exc: return [f"manifest unreadable: {exc}"]
        placeholders = set(self.config.get("placeholder_paths", []))
        for key, value in sorted(manifest.items()):
            if isinstance(value, str) and "/" in value and value not in placeholders and not (self.root / value).is_file(): errors.append(f"manifest.{key} points to missing file: {value}")
        return errors

    def link_errors(self) -> list[str]:
        errors = []
        for path in self.files:
            if path.suffix.lower() != ".md": continue
            for raw in LINK.findall(path.read_text(encoding="utf-8")):
                target = raw.strip().split("#", 1)[0].replace("%20", " ")
                if target and "://" not in target and not target.startswith(("mailto:", "#")) and not (path.parent / target).resolve().is_file(): errors.append(f"broken link: {rel(path, self.root)} -> {raw}")
        return errors

    def metadata_errors(self) -> list[str]:
        errors = []
        try: manifest = json.loads((self.root / "manifest.json").read_text())
        except Exception as exc: return [f"metadata unavailable: {exc}"]
        expected = {"version": self.config["version"], "latest_sprint": self.config["sprint"], "latest_sprint_document": f"docs/sprints/{self.config['sprint']}.md", "release_validation_report": f"docs/releases/RELEASE-{self.config['version']}-VALIDATION.md"}
        for key, value in expected.items():
            if manifest.get(key) != value: errors.append(f"manifest.{key} must be {value!r}")
        for name in self.config["metadata_files"]:
            text = (self.root / name).read_text(encoding="utf-8")
            for token in (self.config["version"], "Sprint 030"):
                if token not in text: errors.append(f"{name} is missing synchronized token: {token}")
        return errors

    def lts_errors(self) -> list[str]:
        try: status = json.loads((self.root / "21_LTS_GOVERNANCE/registry/LTS_STATUS.json").read_text())["status"]
        except Exception as exc: return [f"LTS status unverifiable: {exc}"]
        return [] if status == "hold" else [f"invalid LTS status: expected hold, got {status!r}"]

    def validate(self, output: Path | None) -> int:
        return self.emit("repository-validation", {"configuration": [], "json": self.json_errors(), "links": self.link_errors(), "manifest": self.manifest_errors(), "metadata": self.metadata_errors()}, output=output)

    def regression(self, output: Path | None) -> int:
        errors = []
        for name in sorted(self.config["required_registries"]):
            try:
                if not isinstance(json.loads((self.root / name).read_text()), (dict, list)): errors.append(f"registry root is not object/array: {name}")
            except Exception as exc: errors.append(f"registry invalid: {name}: {exc}")
        return self.emit("governance-regression", {"lts_hold": self.lts_errors(), "registries": errors}, output=output)

    def audit(self, output: Path | None) -> int:
        module_errors = [f"module has no tracked files: {name}" for name in self.config["required_modules"] if not any(rel(p, self.root).startswith(name + "/") for p in self.files)]
        artifact_errors = [f"completion artifact is not manifest-registered: {name}" for name in self.config["completion_artifacts"] if name not in json.loads((self.root / "manifest.json").read_text()).values()]
        pipeline = {
            "user_request": "12_TEMPLATES/USER_INPUT_TEMPLATE.md", "context": "00_CONTEXT/AHIF_AI_CONTEXT.md", "identity": "02_CORE_IDENTITY/CANONICAL_IDENTITY.md",
            "knowledge_graph": "09_DECISION_ENGINE/knowledge_graph/KNOWLEDGE_GRAPH_OVERVIEW.md", "decision_engine": "09_DECISION_ENGINE/inference/INFERENCE_PIPELINE.md",
            "reasoning_engine": "09_DECISION_ENGINE/reasoning/REASONING_PIPELINE.md", "prompt_compiler": "10_PROMPT_COMPILER/COMPILER_PIPELINE.md",
            "quality_assurance": "11_QUALITY_ASSURANCE/QA_PIPELINE.md", "final_prompt": "15_FINAL_PROMPT/EXECUTION_ORCHESTRATION.md",
            "model_adapter": "16_MODEL_ADAPTERS/MODEL_SPECIFIC_ADAPTER_LAYER.md",
        }
        pipeline_errors = [f"pipeline stage missing: {stage} -> {path}" for stage, path in pipeline.items() if not (self.root / path).is_file()]
        return self.emit("framework-completion-audit", {"artifacts": artifact_errors, "links": self.link_errors(), "manifest": self.manifest_errors(), "modules": module_errors, "pipeline": pipeline_errors}, output=output, extra={"modules_audited": len(self.config["required_modules"]), "pipeline_stages_audited": len(pipeline)})

    def health(self, output: Path | None) -> int:
        checks = {"configuration": [], "lts_hold": self.lts_errors(), "manifest": self.manifest_errors()}
        extra = {"version": self.config["version"], "sprint": self.config["sprint"], "workflows": sorted(self.config["required_workflows"]), "scripts": sorted(self.config["required_scripts"]), "registries": sorted(self.config["required_registries"]), "release_eligibility": "hold", "lts_status": "hold"}
        return self.emit("repository-health", checks, "hold", ["Repository evidence is conformant; separate operational LTS evidence remains absent."], output, extra)

    def release(self, output: Path | None) -> int:
        stale = []
        for key in ("validation", "regression", "health"):
            path = self.root / self.config["reports"][key]
            try:
                report = json.loads(path.read_text())
                if report.get("commit_sha") != self.sha: stale.append(f"stale report evidence: {rel(path, self.root)}")
                if report.get("status") not in ("pass", "hold"): stale.append(f"non-passing report evidence: {rel(path, self.root)}")
            except Exception as exc: stale.append(f"required report unavailable: {rel(path, self.root)}: {exc}")
        release_doc = self.root / f"docs/releases/RELEASE-{self.config['version']}-VALIDATION.md"
        claims = []
        text = release_doc.read_text(encoding="utf-8").lower() if release_doc.is_file() else ""
        for phrase in self.config["claim_boundary_phrases"]:
            if phrase.lower() not in text: claims.append(f"claim-boundary statement missing: {phrase}")
        checks = {"claim_boundaries": claims, "evidence_freshness": stale, "lts_hold": self.lts_errors(), "manifest": self.manifest_errors(), "metadata": self.metadata_errors()}
        return self.emit("release-gate", checks, "hold", ["Repository checks pass; release eligibility and LTS designation remain HOLD."], output)


def report_path(root: Path, config: dict[str, Any], key: str, explicit: Path | None) -> Path | None:
    return explicit or root / config["reports"][key]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["verify-config", "validate", "regression", "audit", "health", "release"])
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--config", type=Path, default=CONFIG_PATH)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--machine", action="store_true", default=os.environ.get("AHIF_MACHINE") == "1")
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        config = load_config(args.config, root)
        if args.command == "verify-config":
            print(json.dumps({"status": "pass", "exit_code": 0}, separators=(",", ":")) if args.machine else "PASS configuration")
            return 0
        engine = Engine(root, config, args.machine, args.verbose)
        key = {"validate": "validation", "regression": "regression", "audit": "completion_audit", "health": "health", "release": "release"}[args.command]
        return getattr(engine, args.command)(report_path(root, config, key, args.output))
    except ConfigError as exc:
        print(f"FAIL configuration: {exc}", file=sys.stderr); return 1
    except Exception as exc:
        print(f"INTERNAL_ERROR: {exc}", file=sys.stderr)
        if args.verbose: raise
        return 2


if __name__ == "__main__": raise SystemExit(main())
