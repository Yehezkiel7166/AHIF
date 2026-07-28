"""Rule-priority decision stage."""
from typing import Any, Mapping
from .contracts import StageResult, require_mapping


def run_decision(payload: Mapping[str, Any]) -> StageResult:
    value = require_mapping(payload, "decision_input")
    context, knowledge = value["context"], value["knowledge"]
    decisions = []
    for record in knowledge["records"]:
        decisions.append({"rule_id": record["id"], "priority": record["priority"],
                          "effects": record["effects"], "constraints": record["constraints"]})
    return StageResult({"context": context, "decisions": decisions,
                        "resolution": "priority-descending-then-identifier"})
