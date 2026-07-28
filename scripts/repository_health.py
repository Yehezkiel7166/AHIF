#!/usr/bin/env python3
"""Emit a machine-readable repository-only health assessment."""
import json
import subprocess
from pathlib import Path

root = Path(__file__).resolve().parents[1]
commands = {
    "validation": ["scripts/validate_repository.sh"],
    "regression": ["scripts/run_regression.sh"],
}
checks = {}
for name, command in commands.items():
    completed = subprocess.run(command, cwd=root, text=True, capture_output=True)
    checks[name] = {"status": "pass" if completed.returncode == 0 else "fail"}

report = {
    "schema_version": "1.0",
    "scope": "repository-only",
    "status": "pass" if all(v["status"] == "pass" for v in checks.values()) else "fail",
    "checks": checks,
    "claim_boundary": (
        "This report does not certify production health, deployment, external telemetry, "
        "empirical model quality, operational readiness, LTS designation, or adapter-tier changes."
    ),
}
print(json.dumps(report, indent=2))
raise SystemExit(0 if report["status"] == "pass" else 1)
