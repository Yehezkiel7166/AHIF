"""Final prompt packaging stage; callable only with a passing QA report."""
from typing import Any, Mapping
from .contracts import StageResult, require_mapping


def generate_final_prompt(payload: Mapping[str, Any]) -> StageResult:
    value = require_mapping(payload, "final_prompt_input")
    if value["qa"]["gate"] != "pass":
        return StageResult({"release_eligible": False, "final_prompt": None})
    compiled = value["compiled"]
    return StageResult({"release_eligible": True, "final_prompt": compiled["positive_prompt"],
                        "negative_constraints": compiled["negative_constraints"],
                        "identity_binding": compiled["identity_binding"], "qa_gate": "pass"})
