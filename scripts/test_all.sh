#!/usr/bin/env bash
# Exit codes: 0 all repository checks passed (release remains HOLD); 1 check failure; 2 invocation/internal error.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
rm -rf reports; mkdir -p reports
steps=()
run(){ echo "==> $1"; shift; "$@"; steps+=("$1"); }
run validation scripts/validate_repository.sh
run regression scripts/run_regression.sh
run failure-injection python3 scripts/test_failure_injection.py
run repository-health python3 scripts/repository_health.py >/dev/null
run release-gate scripts/release_gate.sh
run python-syntax python3 -m compileall -q scripts
run shell-syntax bash -n scripts/*.sh
python3 - "${steps[@]}" <<'PY'
import json,subprocess,sys
from datetime import datetime,timezone
from pathlib import Path
p=Path('reports/full-test-run.json'); steps=sys.argv[1:]
data={'schema':'ahif.verification-report','schema_version':'1.0','report_type':'full-test-run','timestamp':datetime.now(timezone.utc).isoformat(),'commit_sha':subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),'branch':subprocess.check_output(['git','branch','--show-current'],text=True).strip(),'checks_executed':[{'name':x,'status':'pass'} for x in steps],'status':'hold','warnings':['All executable repository checks pass; LTS designation and release eligibility remain HOLD.'],'failures':[],'exit_code':0}
p.write_text(json.dumps(data,indent=2)+'\n')
PY
echo "SUMMARY: PASS ${#steps[@]} checks; release eligibility HOLD; reports in reports/"
