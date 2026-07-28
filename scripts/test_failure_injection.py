#!/usr/bin/env python3
"""Isolated negative-path and deterministic-output self-tests."""
from __future__ import annotations
import copy, json, shutil, subprocess, tempfile
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; CONFIG=json.loads((ROOT/'automation.config.json').read_text()); CASES={}
def command(root, action, config=None, output=None):
 args=['python3',str(ROOT/'scripts/repository_checks.py'),action,'--root',str(root),'--machine']
 if config: args += ['--config',str(config)]
 if output: args += ['--output',str(output)]
 return subprocess.run(args,cwd=ROOT,text=True,capture_output=True)
def fixture(name, mutate, action='validate'):
 with tempfile.TemporaryDirectory() as temp:
  repo=Path(temp)/'repo'; shutil.copytree(ROOT,repo,ignore=shutil.ignore_patterns('.git','.artifacts','__pycache__')); mutate(repo)
  CASES[name]=command(repo,action,repo/'automation.config.json').returncode==1
fixture('malformed_repository_state',lambda r:(r/'manifest.json').write_text('{'))
fixture('unknown_required_path',lambda r:(lambda d:(d['required_scripts'].append('scripts/unknown.py'),(r/'automation.config.json').write_text(json.dumps(d))))(copy.deepcopy(CONFIG)))
fixture('duplicate_configuration_entry',lambda r:(lambda d:(d['required_scripts'].append(d['required_scripts'][0]),(r/'automation.config.json').write_text(json.dumps(d))))(copy.deepcopy(CONFIG)),'verify-config')
fixture('invalid_exit_code_mapping',lambda r:(lambda d:(d['exit_codes'].update({'FAIL':0}),(r/'automation.config.json').write_text(json.dumps(d))))(copy.deepcopy(CONFIG)),'verify-config')
fixture('invalid_lts_status',lambda r:(lambda p,d:(d.update({'status':'designated'}),p.write_text(json.dumps(d))))(r/'21_LTS_GOVERNANCE/registry/LTS_STATUS.json',json.loads((r/'21_LTS_GOVERNANCE/registry/LTS_STATUS.json').read_text())),'regression')
fixture('broken_markdown_link',lambda r:(r/'BROKEN.md').write_text('[missing](no-such-file.md)'))
with tempfile.TemporaryDirectory() as temp:
 repo=Path(temp)/'repo'; shutil.copytree(ROOT,repo,ignore=shutil.ignore_patterns('.git','.artifacts','__pycache__')); cfg=repo/'automation.config.json'
 for action,key in (('validate','validation'),('regression','regression'),('health','health')): command(repo,action,cfg,repo/CONFIG['reports'][key])
 report=repo/CONFIG['reports']['validation']; data=json.loads(report.read_text()); data['commit_sha']='stale'; report.write_text(json.dumps(data))
 CASES['stale_report_evidence']=command(repo,'release',cfg).returncode==1
with tempfile.TemporaryDirectory() as temp:
 one,two=Path(temp)/'one.json',Path(temp)/'two.json'; command(ROOT,'health',output=one); command(ROOT,'health',output=two)
 a,b=json.loads(one.read_text()),json.loads(two.read_text())
 for item in (a,b): item.pop('generated_at',None)
 CASES['deterministic_report_structure']=a==b and a['scripts']==sorted(a['scripts'])
 CASES['absolute_paths_not_emitted']=str(ROOT) not in one.read_text()+two.read_text()
before=subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True); command(ROOT,'health'); after=subprocess.check_output(['git','status','--porcelain'],cwd=ROOT,text=True)
CASES['generated_artifact_cleanliness']=before==after
failed=sorted(n for n,v in CASES.items() if not v)
for name in sorted(CASES): print(f"{'PASS' if CASES[name] else 'FAIL'} fixture {name}")
out=ROOT/CONFIG['reports']['failure_injection']; out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({'schema':'ahif.self-test-report','schema_version':'1.0','report_type':'failure-injection','commit_sha':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'generated_at':datetime.now(timezone.utc).isoformat().replace('+00:00','Z'),'status':'fail' if failed else 'pass','cases':[{'name':n,'status':'pass' if CASES[n] else 'fail'} for n in sorted(CASES)],'exit_code':1 if failed else 0},indent=2,sort_keys=True)+'\n')
raise SystemExit(1 if failed else 0)
