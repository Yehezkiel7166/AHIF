#!/usr/bin/env python3
"""AHIF dependency-free executable verification and reporting library."""
from __future__ import annotations

import argparse, json, os, re, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "3.2.0"
SPRINT = "SPRINT-027-EXECUTABLE-VERIFICATION-HARDENING"
REPORT_DIR = ROOT / "reports"
PLACEHOLDERS = {"assets/identity-reference/MASTER_PHOTO.jpg"}
LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")

def git(*args: str, root: Path = ROOT) -> str:
    p = subprocess.run(["git", *args], cwd=root, text=True, capture_output=True)
    return p.stdout.strip() if p.returncode == 0 else "unknown"

def files(root: Path) -> list[Path]:
    if root == ROOT:
        out = subprocess.run(["git", "ls-files", "-z"], cwd=root, check=True, capture_output=True).stdout
        return [root / x.decode() for x in out.split(b"\0") if x and (root / x.decode()).is_file()]
    return sorted(p for p in root.rglob("*") if p.is_file())

def context(root: Path) -> dict:
    return {"timestamp": datetime.now(timezone.utc).isoformat(), "commit_sha": git("rev-parse", "HEAD", root=root),
            "branch": git("branch", "--show-current", root=root)}

def check_json(root: Path) -> list[str]:
    errors=[]
    for p in files(root):
        if p.suffix == ".json":
            try: json.loads(p.read_text(encoding="utf-8"))
            except (OSError, UnicodeError, json.JSONDecodeError) as e: errors.append(f"invalid JSON: {p.relative_to(root)}: {e}")
    return errors

def manifest(root: Path) -> dict:
    return json.loads((root / "manifest.json").read_text(encoding="utf-8"))

def check_manifest(root: Path) -> list[str]:
    errors=[]
    try: data=manifest(root)
    except Exception as e: return [f"manifest unreadable: {e}"]
    for key,value in data.items():
        if isinstance(value,str) and "/" in value and value not in PLACEHOLDERS and not (root/value).is_file():
            errors.append(f"manifest.{key} points to missing file: {value}")
    return errors

def check_links(root: Path) -> list[str]:
    errors=[]
    for p in files(root):
        if p.suffix.lower() != ".md": continue
        for raw in LINK.findall(p.read_text(encoding="utf-8")):
            target=raw.strip().split("#",1)[0].replace("%20"," ")
            if target and "://" not in target and not target.startswith(("mailto:","#")) and not (p.parent/target).resolve().is_file():
                errors.append(f"broken link: {p.relative_to(root)} -> {raw}")
    return errors

def check_metadata(root: Path) -> list[str]:
    try: data=manifest(root)
    except Exception as e: return [f"metadata unavailable: {e}"]
    expected={"version":VERSION,"latest_sprint":SPRINT,"latest_sprint_document":f"docs/sprints/{SPRINT}.md",
              "release_validation_report":f"docs/releases/RELEASE-{VERSION}-VALIDATION.md"}
    errors=[f"manifest.{k} must be {v!r}" for k,v in expected.items() if data.get(k)!=v]
    required={"README.md":[VERSION,"Sprint 027"],"VERSION.md":[VERSION],"CHANGELOG.md":[VERSION,"Sprint 027"],
              "ROADMAP.md":[VERSION,"Sprint 027"],"00_CONTEXT/AHIF_AI_CONTEXT.md":["Sprint 027"]}
    for name,tokens in required.items():
        try: text=(root/name).read_text(encoding="utf-8")
        except OSError as e: errors.append(f"missing metadata file: {name}: {e}"); continue
        errors += [f"{name} is missing synchronized token: {t}" for t in tokens if t not in text]
    return errors

def check_lts(root: Path) -> list[str]:
    try: status=json.loads((root/"21_LTS_GOVERNANCE/registry/LTS_STATUS.json").read_text()).get("status")
    except Exception as e: return [f"LTS status unverifiable: {e}"]
    return [] if status == "hold" else [f"invalid LTS status: expected hold, got {status!r}"]

def check_claims(root: Path) -> list[str]:
    p=root/f"docs/releases/RELEASE-{VERSION}-VALIDATION.md"
    if not p.is_file(): return [f"release validation missing: {p.relative_to(root)}"]
    text=p.read_text(encoding="utf-8").lower()
    required=["does not claim production readiness","does not claim deployment success","lts status"]
    return [f"claim-boundary statement missing: {x}" for x in required if x not in text]

def report(kind: str, checks: dict[str,list[str]], output: Path|None, status: str|None=None, warnings: list[str]|None=None) -> int:
    failures=[f"{name}: {e}" for name,errs in checks.items() for e in errs]
    code=1 if failures else 0
    final=status or ("fail" if failures else "pass")
    data={"schema":"ahif.verification-report","schema_version":"1.0","report_type":kind,**context(ROOT),
          "checks_executed":[{"name":n,"status":"fail" if e else "pass"} for n,e in checks.items()],
          "status":final,"warnings":warnings or [],"failures":failures,"exit_code":code}
    if output:
        output.parent.mkdir(parents=True,exist_ok=True); output.write_text(json.dumps(data,indent=2)+"\n")
    print(f"{final.upper()} {kind}: {len(checks)} checks, {len(failures)} failures, {len(data['warnings'])} warnings")
    for x in failures: print(f"  - {x}")
    return code

def validation(root: Path, output: Path|None) -> int:
    return report("repository-validation", {"json":check_json(root),"manifest":check_manifest(root),"links":check_links(root),"metadata":check_metadata(root)},output)

def regression(root: Path, output: Path|None) -> int:
    regs=[]
    for p in files(root):
        if p.suffix==".json" and ("registry" in p.parts or "REGISTRY" in p.parts):
            try:
                if not isinstance(json.loads(p.read_text()),(dict,list)): regs.append(f"registry root is not object/array: {p.relative_to(root)}")
            except Exception as e: regs.append(f"registry invalid: {p.relative_to(root)}: {e}")
    return report("governance-regression",{"registries":regs,"lts_hold":check_lts(root)},output)

def release(root: Path, output: Path|None) -> int:
    checks={"version_and_sprint":check_metadata(root),"manifest_paths":check_manifest(root),"claim_boundaries":check_claims(root),"lts_hold":check_lts(root),
            "release_validation":[] if (root/f"docs/releases/RELEASE-{VERSION}-VALIDATION.md").is_file() else ["release validation absent"],
            "required_reports":[f"required report missing: {p}" for p in ["validation.json","regression.json","repository-health.json"] if not (REPORT_DIR/p).is_file()]}
    return report("release-gate",checks,output,"fail" if any(checks.values()) else "hold",["Repository checks pass, but absent separate operational LTS evidence requires HOLD."])

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("command",choices=["validate","regression","release"]); ap.add_argument("--root",type=Path,default=ROOT); ap.add_argument("--output",type=Path)
    a=ap.parse_args(); root=a.root.resolve()
    return {"validate":validation,"regression":regression,"release":release}[a.command](root,a.output)
if __name__=="__main__": raise SystemExit(main())
