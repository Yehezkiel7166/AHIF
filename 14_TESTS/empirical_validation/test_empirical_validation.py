import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location("empirical_framework",ROOT/"22_EMPIRICAL_VALIDATION/framework.py")
f=importlib.util.module_from_spec(spec); spec.loader.exec_module(f)

def read(path): return json.loads((ROOT/path).read_text())

class EmpiricalValidationTests(unittest.TestCase):
 def setUp(self):
  self.scenario=read("22_EMPIRICAL_VALIDATION/scenarios/kyoto-autumn-morning.json")
  self.execution={'schema_version':'1.0','execution_id':'exec-001','framework_version':'3.6.0','scenario_id':'kyoto-autumn-morning','timestamp':'2026-07-28T00:00:00Z','model_adapter':'ahif.openai-images.v1','prompt_package_hash':'sha256:'+'a'*64,'image_hash':None,'evaluation_status':'NOT_EVALUATED','evidence_status':'MISSING','reviewer':None,'comments':'No run performed.'}
 def test_schema_validation_and_report(self):
  f.validate_record('scenario',self.scenario); f.validate_record('execution',self.execution)
  report=f.build_report(self.execution,self.scenario,{'sha256':self.execution['prompt_package_hash']})
  self.assertEqual(report['claim_boundary'],'NO_PRODUCTION_CLAIM')
 def test_execution_available_requires_image_hash(self):
  self.execution['evidence_status']='AVAILABLE'
  with self.assertRaises(f.ValidationError): f.validate_record('execution',self.execution)
 def test_missing_evidence_is_valid_and_explicit(self):
  evidence={'schema_version':'1.0','evidence_id':'e-1','execution_id':'exec-001','status':'MISSING','artifacts':[],'collected_at':None,'collector':None,'comments':'Not collected.'}
  f.validate_record('evidence',evidence)
 def test_invalid_evaluation_rejected(self):
  dimensions={d:'NOT_EVALUATED' for d in read('22_EMPIRICAL_VALIDATION/metrics/EVALUATION_CRITERIA.json')['dimensions']}
  evaluation={'schema_version':'1.0','evaluation_id':'v-1','execution_id':'exec-001','status':'APPROVED','dimensions':dimensions,'reviewer':None,'reviewed_at':None,'comments':''}
  with self.assertRaises(f.ValidationError): f.validate_record('evaluation',evaluation)
 def test_evidence_integrity_and_hash_verification(self):
  with tempfile.TemporaryDirectory() as td:
   artifact=Path(td)/'real-output.bin'; artifact.write_bytes(b'externally supplied bytes')
   record={'schema_version':'1.0','evidence_id':'e-2','execution_id':'exec-001','status':'AVAILABLE','artifacts':[{'artifact_type':'IMAGE','path':'real-output.bin','sha256':f.sha256_file(artifact)}],'collected_at':'2026-07-28T01:00:00Z','collector':'reviewer-id','comments':''}
   f.verify_evidence(record,td)
   record['artifacts'][0]['sha256']='sha256:'+'0'*64
   with self.assertRaises(f.IntegrityError): f.verify_evidence(record,td)
 def test_unknown_and_numeric_evaluation_values_rejected(self):
  dimensions={d:'PENDING' for d in read('22_EMPIRICAL_VALIDATION/metrics/EVALUATION_CRITERIA.json')['dimensions']}; dimensions['overall']=5
  evaluation={'schema_version':'1.0','evaluation_id':'v-2','execution_id':'exec-001','status':'PENDING','dimensions':dimensions,'reviewer':None,'reviewed_at':None,'comments':''}
  with self.assertRaises(f.ValidationError): f.validate_record('evaluation',evaluation)
 def test_empty_canonical_registries_are_consistent(self):
  self.assertEqual(f.validate_registries(), {'execution':0,'evaluation':0,'evidence':0,'report':0,'comparison':0})

if __name__=='__main__': unittest.main()
