import copy
import json
import unittest
from pathlib import Path
from unittest.mock import patch

from RUNTIME import Framework, RuntimeContractError, execute_framework
from RUNTIME.contracts import StageResult, Status

ROOT = Path(__file__).resolve().parents[2]


class RuntimeEndToEndTest(unittest.TestCase):
    def request(self):
        return {"user_request": {"location": "Kyoto, Japan", "place": "Gion district",
                "atmosphere": "calm autumn morning"},
                "identity": {"canonical_asset": "assets/identity-reference/MASTER_PHOTO.jpg"},
                "adapter_id": "ahif.openai-images.v1",
                "execution_timestamp": "2026-07-28T00:00:00Z"}

    def test_normal_execution_state_machine_and_determinism(self):
        first = Framework.execute(self.request())
        second = Framework.execute(copy.deepcopy(self.request()))
        self.assertEqual(first, second)
        self.assertEqual(first, execute_framework(self.request()))
        self.assertEqual(first["execution_trace"]["final_state"], "FINISHED")
        self.assertEqual([x["execution_state"] for x in first["execution_trace"]["stages"]],
                         ["CONTEXT_READY", "IDENTITY_LOCKED", "KNOWLEDGE_READY",
                          "DECISION_COMPLETE", "REASONING_COMPLETE", "PROMPT_COMPILED",
                          "QA_COMPLETE", "FINAL_PACKAGE_READY", "ADAPTER_READY",
                          "EMPIRICAL_VALIDATION_READY"])
        self.assertEqual(first["execution_report"]["validation"]["status"], "pass")
        self.assertTrue(first["final_prompt"])
        self.assertTrue(first["adapter_request"])
        empirical = first["empirical_validation"]
        self.assertEqual(empirical["execution_record"]["execution_id"], first["execution_id"])
        self.assertEqual(empirical["evidence_record"]["execution_id"], first["execution_id"])
        self.assertEqual(empirical["report"]["claim_boundary"], "NO_PRODUCTION_CLAIM")
        self.assertFalse(empirical["persisted"])

    def test_complete_flow_has_no_qa_or_adapter_bypass(self):
        result = Framework.execute(self.request())
        stages = result["execution_trace"]["stages"]
        order = {stage["stage"]: stage["execution_order"] for stage in stages}
        self.assertLess(order["qa"], order["final_prompt"])
        self.assertLess(order["final_prompt"], order["adapter"])
        self.assertLess(order["adapter"], order["empirical_validation"])
        self.assertEqual(result["pipeline_state"]["qa"]["gate"], "pass")
        self.assertEqual(result["empirical_validation"]["status"], "NOT_EVALUATED")

    def test_existing_examples_are_executable(self):
        for path in sorted((ROOT / "13_EXAMPLES/runtime").glob("*.json")):
            result = Framework.execute(json.loads(path.read_text()))
            self.assertEqual(result["validation_state"]["status"], "pass", path.name)

    def test_validation_failure(self):
        request = self.request(); del request["user_request"]["place"]
        with self.assertRaises(RuntimeContractError):
            Framework.execute(request)

    def test_identity_failure(self):
        request = self.request(); request["identity"] = {}
        with self.assertRaisesRegex(RuntimeContractError, "canonical_asset"):
            Framework.execute(request)

    def test_compiler_failure_is_reported_and_blocks_release(self):
        failed = StageResult({}, Status.FAIL, errors=("AHIF-COMPILER-INJECTED",))
        with patch("RUNTIME.engine.compile_prompt", return_value=failed):
            result = Framework.execute(self.request())
        self.assertIn("AHIF-COMPILER-INJECTED", result["execution_report"]["errors"])
        self.assertFalse(result["final_prompt_package"]["release_eligible"])
        self.assertIsNone(result["adapter_request"])

    def test_qa_failure_and_blocked_release_have_no_bypass(self):
        blocked = StageResult({"gate": "blocked", "checks": {}}, Status.BLOCKED,
                              errors=("AHIF-QA-INJECTED",))
        with patch("RUNTIME.engine.run_quality_assurance", return_value=blocked):
            result = Framework.execute(self.request())
        self.assertEqual(result["execution_report"]["validation"]["status"], "blocked")
        self.assertIsNone(result["final_prompt"])
        self.assertEqual(result["adapter_package"]["adapter_status"], "blocked")

    def test_unknown_adapter_blocks_without_external_execution(self):
        request = self.request(); request["adapter_id"] = "unknown"
        result = Framework.execute(request)
        self.assertEqual(result["validation_state"]["status"], "blocked")
        self.assertIsNone(result["adapter_request"])
        self.assertFalse(result["metadata"]["external_model_invoked"])

    def test_recovery_path_is_machine_readable_and_deterministic(self):
        request = self.request()
        request["user_request"]["constraints"] = [" no text ", "no text"]
        first = Framework.execute(request)
        second = Framework.execute(copy.deepcopy(request))
        self.assertEqual(first, second)
        self.assertEqual(first["execution_report"]["recovery_events"],
                         ["AHIF-RECOVERY-CONTEXT-CONSTRAINTS-NORMALIZED"])


if __name__ == "__main__":
    unittest.main()
