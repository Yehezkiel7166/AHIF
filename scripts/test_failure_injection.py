#!/usr/bin/env python3
"""Prove isolated invalid repositories are rejected."""
import json, shutil, subprocess, tempfile
from pathlib import Path
root=Path(__file__).resolve().parents[1]
cases={}
def run(name, mutate, command='validate'):
 with tempfile.TemporaryDirectory() as d:
  dst=Path(d)/'repo'; shutil.copytree(root,dst,ignore=shutil.ignore_patterns('.git','reports','__pycache__'))
  mutate(dst)
  p=subprocess.run(['python3',str(root/'scripts/repository_checks.py'),command,'--root',str(dst)],cwd=root,capture_output=True,text=True)
  cases[name]=p.returncode != 0
run('malformed_json',lambda r:(r/'manifest.json').write_text('{'))
run('missing_manifest_target',lambda r:(lambda m:(m.update({'release_validation_report':'docs/releases/MISSING.md'}),(r/'manifest.json').write_text(json.dumps(m))))(json.loads((r/'manifest.json').read_text())))
run('broken_markdown_link',lambda r:(r/'BROKEN.md').write_text('[missing](no-such-file.md)'))
run('inconsistent_version_metadata',lambda r:(r/'VERSION.md').write_text('Current version: **0.0.0**'))
run('invalid_lts_status',lambda r:(lambda p,d:(d.update({'status':'designated'}),p.write_text(json.dumps(d))))(r/'21_LTS_GOVERNANCE/registry/LTS_STATUS.json',json.loads((r/'21_LTS_GOVERNANCE/registry/LTS_STATUS.json').read_text())),'regression')
run('claim_boundary_violation',lambda r:(r/'docs/releases/RELEASE-3.2.0-VALIDATION.md').write_text('# invalid\nProduction ready and deployed.\n'),'release')
failed=[n for n,ok in cases.items() if not ok]
for n,ok in cases.items(): print(f'{"PASS" if ok else "FAIL"} fixture {n}: invalid state rejected' if ok else f'FAIL fixture {n}: validator accepted invalid state')
raise SystemExit(1 if failed else 0)
