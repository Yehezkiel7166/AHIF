#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
python3 scripts/repository_checks.py validate --output reports/validation.json
git diff --check
