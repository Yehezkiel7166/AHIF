"""Explainable, non-chain-of-thought reasoning handoff stage."""
from typing import Any, Mapping
from .contracts import StageResult, require_mapping


def run_reasoning(payload: Mapping[str, Any]) -> StageResult:
    value = require_mapping(payload, "reasoning_input")
    items = [{"rule_id": d["rule_id"], "outcome": "accepted", "basis": "registered-rule"}
             for d in value["decision"]["decisions"]]
    return StageResult({"context": value["decision"]["context"], "identity": value["identity"],
                        "decision_record": items, "directives": value["decision"]["decisions"]})
