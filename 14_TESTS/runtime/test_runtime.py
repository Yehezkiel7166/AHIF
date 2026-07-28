import copy
import json
import unittest
from pathlib import Path

from RUNTIME import RuntimeContractError, execute_framework

ROOT = Path(__file__).resolve().parents[2]


class RuntimeEndToEndTest(unittest.TestCase):
    def request(self):
        return {"user_request": {"location": "Kyoto, Japan", "place": "Gion district",
                "atmosphere": "calm autumn morning"},
                "identity": {"canonical_asset": "assets/identity-reference/MASTER_PHOTO.jpg"},
                "adapter_id": "ahif.openai-images.v1", "execution_timestamp": "2026-07-28T00:00:00Z"}

    def test_pipeline_is_complete_sequential_and_deterministic(self):
        first = execute_framework(self.request())
        second = execute_framework(copy.deepcopy(self.request()))
        self.assertEqual(first, second)
        self.assertEqual([x["stage"] for x in first["execution_trace"]["stages"]],
                         ["context", "identity", "knowledge", "decision", "reasoning", "compiler", "qa", "final_prompt", "adapter"])
        self.assertEqual(first["validation_state"]["status"], "pass")
        self.assertEqual(first["pipeline_state"]["identity"]["lock_status"], "locked")
        self.assertTrue(first["pipeline_state"]["decision"]["decisions"])
        self.assertTrue(first["pipeline_state"]["reasoning"]["decision_record"])
        self.assertEqual(first["pipeline_state"]["qa"]["gate"], "pass")
        self.assertTrue(first["final_prompt_package"]["final_prompt"])
        self.assertEqual(first["adapter_package"]["adapter_status"], "prepared")

    def test_existing_examples_are_executable(self):
        for path in sorted((ROOT / "13_EXAMPLES/runtime").glob("*.json")):
            result = execute_framework(json.loads(path.read_text()))
            self.assertEqual(result["validation_state"]["status"], "pass", path.name)

    def test_invalid_input_fails_closed(self):
        request = self.request(); del request["user_request"]["place"]
        with self.assertRaises(RuntimeContractError): execute_framework(request)


if __name__ == "__main__": unittest.main()
