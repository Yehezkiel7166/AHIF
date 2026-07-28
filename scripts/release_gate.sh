#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

scripts/validate_repository.sh
scripts/run_regression.sh

test "$(python3 -c 'import json; print(json.load(open("manifest.json"))["version"])')" = "3.1.0"
test -f docs/releases/RELEASE-3.1.0-VALIDATION.md
test -f docs/repository-health/SPRINT-026-HEALTH.md
echo "PASS release-gate: repository evidence is complete; external and operational claims remain out of scope"
