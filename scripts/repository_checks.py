#!/usr/bin/env python3
"""Dependency-free repository checks used locally and in CI."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_VERSION = "3.1.0"
EXPECTED_SPRINT = "SPRINT-026-EXECUTABLE-REPOSITORY-AUTOMATION"
PLACEHOLDERS = {"assets/identity-reference/MASTER_PHOTO.jpg"}


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, check=True, capture_output=True
    )
    return [ROOT / p.decode() for p in result.stdout.split(b"\0") if p]


def check_json() -> list[str]:
    errors = []
    for path in tracked_files():
        if path.suffix == ".json":
            try:
                json.loads(path.read_text(encoding="utf-8"))
            except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
                errors.append(f"invalid JSON: {path.relative_to(ROOT)}: {exc}")
    return errors


def check_manifest() -> list[str]:
    errors = []
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    for key, value in manifest.items():
        if not isinstance(value, str) or "/" not in value:
            continue
        if value in PLACEHOLDERS:
            continue
        if not (ROOT / value).is_file():
            errors.append(f"manifest.{key} points to missing file: {value}")
    return errors


LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


def check_links() -> list[str]:
    errors = []
    for path in tracked_files():
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for raw in LINK.findall(text):
            target = raw.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith(("mailto:", "#")):
                continue
            target = target.replace("%20", " ")
            if not (path.parent / target).resolve().is_file():
                errors.append(f"broken link: {path.relative_to(ROOT)} -> {raw}")
    return errors


def check_metadata() -> list[str]:
    manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
    expected = {
        "version": EXPECTED_VERSION,
        "latest_sprint": EXPECTED_SPRINT,
        "latest_sprint_document": f"docs/sprints/{EXPECTED_SPRINT}.md",
        "release_validation_report": f"docs/releases/RELEASE-{EXPECTED_VERSION}-VALIDATION.md",
    }
    errors = [
        f"manifest.{key} must be {value!r}"
        for key, value in expected.items()
        if manifest.get(key) != value
    ]
    required = {
        "README.md": [EXPECTED_VERSION, "Sprint 026"],
        "VERSION.md": [EXPECTED_VERSION],
        "CHANGELOG.md": [EXPECTED_VERSION, "Sprint 026"],
        "ROADMAP.md": [EXPECTED_VERSION, "Sprint 026"],
        "00_CONTEXT/AHIF_AI_CONTEXT.md": ["Sprint 026"],
    }
    for name, tokens in required.items():
        text = (ROOT / name).read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                errors.append(f"{name} is missing synchronized token: {token}")
    return errors


def run(selected: list[str]) -> int:
    checks = {
        "json": check_json,
        "manifest": check_manifest,
        "links": check_links,
        "metadata": check_metadata,
    }
    unknown = sorted(set(selected) - checks.keys())
    if unknown:
        print(f"unknown checks: {', '.join(unknown)}", file=sys.stderr)
        return 2
    failures = 0
    for name in selected:
        errors = checks[name]()
        print(f"{'PASS' if not errors else 'FAIL'} {name}")
        for error in errors:
            print(f"  - {error}")
        failures += len(errors)
    return 1 if failures else 0


if __name__ == "__main__":
    requested = sys.argv[1:] or ["json", "manifest", "links", "metadata"]
    raise SystemExit(run(requested))
