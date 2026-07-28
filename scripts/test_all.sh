#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
rm -rf .artifacts/reports; mkdir -p .artifacts/reports
steps=(verify-config validate regression runtime framework-audit failure-injection health release-check python-syntax shell-syntax)
run(){ [[ "${AHIF_MACHINE:-0}" == 1 ]] || printf '==> %s\n' "$1"; shift; "$@"; }
run verify-config python3 scripts/repository_checks.py verify-config
run validate scripts/validate_repository.sh
run regression scripts/run_regression.sh
run runtime python3 -m unittest discover -s 14_TESTS/runtime -p 'test_*.py' -v
run framework-audit python3 scripts/repository_checks.py audit
run failure-injection python3 scripts/test_failure_injection.py
run health python3 scripts/repository_health.py
run release-check scripts/release_gate.sh
run python-syntax python3 -m compileall -q scripts RUNTIME 14_TESTS/runtime
run shell-syntax bash -n scripts/release_gate.sh scripts/run_regression.sh scripts/test_all.sh scripts/validate_repository.sh
python3 - "${steps[@]}" <<'PY'
import json,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
cfg=json.loads(Path('automation.config.json').read_text()); steps=sys.argv[1:]
data={'schema':'ahif.verification-report','schema_version':'2.0','report_type':'full-test-run','generated_at':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),'commit_sha':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'checks_executed':[{'name':x,'status':'pass'} for x in sorted(steps)],'status':'hold','warnings':['Repository checks pass; LTS designation remains HOLD.'],'failures':[],'exit_code':0}
Path(cfg['reports']['full_test']).write_text(json.dumps(data,indent=2,sort_keys=True)+'\n')
PY
[[ "${AHIF_MACHINE:-0}" == 1 ]] || echo 'SUMMARY: PASS; release eligibility HOLD; reports in .artifacts/reports/'
