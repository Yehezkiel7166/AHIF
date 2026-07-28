"""Mandatory runtime quality-assurance gate."""
from typing import Any, Mapping
from .contracts import StageResult, Status, require_mapping


def run_quality_assurance(compiled: Mapping[str, Any]) -> StageResult:
    value = require_mapping(compiled, "compiled_prompt")
    errors = []
    for field in ("positive_prompt", "negative_constraints", "identity_binding"):
        if not value.get(field): errors.append(f"AHIF-QA-MISSING-{field.upper()}")
    if value.get("identity_binding", {}).get("lock_status") != "locked":
        errors.append("AHIF-QA-IDENTITY-NOT-LOCKED")
    status = Status.BLOCKED if errors else Status.PASS
    return StageResult({"gate": "pass" if not errors else "blocked", "checks": {
        "identity_preserved": not any("IDENTITY" in x for x in errors),
        "compiler_output_present": bool(value.get("positive_prompt")),
        "negative_constraints_present": bool(value.get("negative_constraints")),
    }}, status=status, errors=tuple(errors))
