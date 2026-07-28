#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
test -f reports/validation.json && test -f reports/regression.json && test -f reports/repository-health.json
python3 scripts/repository_checks.py release --output reports/release-gate.json
