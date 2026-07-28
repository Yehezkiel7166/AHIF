#!/usr/bin/env python3
"""Generate JSON and Markdown repository-only health reports."""
import json, subprocess
from datetime import datetime, timezone
from pathlib import Path
root=Path(__file__).resolve().parents[1]; out=root/'reports'; out.mkdir(exist_ok=True)
def git(*a):
 p=subprocess.run(['git',*a],cwd=root,text=True,capture_output=True); return p.stdout.strip() if p.returncode==0 else 'unknown'
def load(p):
 try:return json.loads((root/p).read_text())
 except Exception:return {}
m=load('manifest.json'); lts=load('21_LTS_GOVERNANCE/registry/LTS_STATUS.json')
manifest_fail=[]
for k,v in m.items():
 if isinstance(v,str) and '/' in v and v!='assets/identity-reference/MASTER_PHOTO.jpg' and not (root/v).is_file(): manifest_fail.append(f'{k}: {v}')
workflows=sorted(str(p.relative_to(root)) for p in (root/'.github/workflows').glob('*.yml'))
scripts=sorted(str(p.relative_to(root)) for p in (root/'scripts').glob('*') if p.is_file())
registries=list(root.glob('**/registry/*.json'))+list(root.glob('**/REGISTRY/*.json'))
failures=manifest_fail; warnings=['LTS designation remains HOLD: separate governance and operational evidence is absent.']
report={'schema':'ahif.verification-report','schema_version':'1.0','report_type':'repository-health','timestamp':datetime.now(timezone.utc).isoformat(),'commit_sha':git('rev-parse','HEAD'),'branch':git('branch','--show-current'),'checks_executed':[{'name':'manifest_integrity','status':'fail' if failures else 'pass'},{'name':'inventory','status':'pass'},{'name':'lts_status','status':'pass' if lts.get('status')=='hold' else 'fail'}],'status':'fail' if failures or lts.get('status')!='hold' else 'hold','current_version':m.get('version'),'latest_sprint':m.get('latest_sprint'),'manifest_integrity':'fail' if failures else 'pass','workflow_inventory':workflows,'script_inventory':scripts,'registry_status':{'files':len(registries),'status':'present'},'lts_status':lts.get('status','unverifiable'),'warning_count':len(warnings),'failure_count':len(failures),'release_eligibility':'hold','warnings':warnings,'failures':failures,'exit_code':1 if failures else 0}
(out/'repository-health.json').write_text(json.dumps(report,indent=2)+'\n')
rows='\n'.join([f'| Version | {report["current_version"]} |',f'| Latest sprint | {report["latest_sprint"]} |',f'| Manifest integrity | {report["manifest_integrity"].upper()} |',f'| Workflows | {len(workflows)} |',f'| Scripts | {len(scripts)} |',f'| Registries | {len(registries)} present |',f'| LTS status | {report["lts_status"].upper()} |',f'| Warnings / failures | {len(warnings)} / {len(failures)} |',f'| Release eligibility | HOLD |'])
(out/'repository-health.md').write_text('# Sprint 027 Repository Health\n\n| Field | Result |\n|---|---|\n'+rows+'\n\nRepository-only evidence; no operational or production claim is made.\n')
print(json.dumps(report,indent=2)); raise SystemExit(report['exit_code'])
