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
    prompt = str(value.get("positive_prompt", "")).lower()
    if "waxy" in prompt or "plastic skin" in prompt or "porcelain skin" in prompt:
        errors.append("AHIF-QA-REALISM-SKIN-SYNTHETIC")
    if "perfect symmetry" in prompt or "hyper-symmetry" in prompt:
        errors.append("AHIF-QA-REALISM-EXCESSIVE-SYMMETRY")
    if "empirically validated" in prompt or "generated image passed" in prompt:
        errors.append("AHIF-QA-REALISM-EMPIRICAL-CLAIM")
    if "incoherent lighting" in prompt or "contradictory light direction" in prompt:
        errors.append("AHIF-QA-REALISM-LIGHTING-INCOHERENT")
    if "pasted subject" in prompt or "composited cutout" in prompt:
        errors.append("AHIF-QA-REALISM-ENVIRONMENT-INTEGRATION")
    sections = value.get("sections", {})
    if isinstance(sections, Mapping) and value.get("realism_contract") and not sections.get("realism"):
        errors.append("AHIF-QA-REALISM-COMPILER-INTEGRITY")
    status = Status.BLOCKED if errors else Status.PASS
    return StageResult({"gate": "pass" if not errors else "blocked", "checks": {
        "identity_preserved": not any("IDENTITY" in x for x in errors),
        "compiler_output_present": bool(value.get("positive_prompt")),
        "negative_constraints_present": bool(value.get("negative_constraints")),
        "photographic_realism_present": bool(value.get("realism_contract")),
    }}, status=status, errors=tuple(errors))
