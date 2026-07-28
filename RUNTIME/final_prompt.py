"""Final prompt packaging stage; callable only with a passing QA report."""
from typing import Any, Mapping
from .contracts import StageResult, Status, require_mapping


def generate_final_prompt(payload: Mapping[str, Any]) -> StageResult:
    value = require_mapping(payload, "final_prompt_input")
    if value["qa"]["gate"] != "pass":
        return StageResult({"release_eligible": False, "final_prompt": None,
                            "negative_constraints": [], "identity_binding": None,
                            "qa_gate": "blocked"}, Status.BLOCKED,
                           errors=("AHIF-FINAL-QA-BLOCKED",))
    compiled = value["compiled"]
    return StageResult({"release_eligible": True, "final_prompt": compiled["positive_prompt"],
                        "negative_constraints": compiled["negative_constraints"],
                        "identity_binding": compiled["identity_binding"], "qa_gate": "pass"})
