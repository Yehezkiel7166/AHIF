#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

python3 scripts/repository_checks.py json manifest links
python3 - <<'PY'
import json
from pathlib import Path

root = Path('.')
registry_files = sorted(root.glob('**/registry/*.json')) + sorted(root.glob('**/REGISTRY/*.json'))
for path in registry_files:
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, (dict, list)):
        raise SystemExit(f"registry root must be an object or array: {path}")

status = json.loads(Path('21_LTS_GOVERNANCE/registry/LTS_STATUS.json').read_text())
if status.get('status') != 'hold':
    raise SystemExit('LTS designation boundary changed: expected hold')

print(f"PASS regression: {len(registry_files)} registries parse; LTS remains hold")
PY
