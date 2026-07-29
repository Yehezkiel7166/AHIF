"""Canonical prompt compiler stage."""
from typing import Any, Mapping
from .contracts import StageResult, Status, require_mapping


def compile_prompt(reasoning: Mapping[str, Any]) -> StageResult:
    value = require_mapping(reasoning, "reasoning")
    realism = value.get("realism")
    if not isinstance(realism, Mapping) or realism.get("compiler_ready") is not True:
        return StageResult({}, Status.BLOCKED, errors=("AHIF-COMPILER-REALISM-NOT-READY",))
    if realism.get("unresolved_uncertainties"):
        return StageResult({}, Status.BLOCKED,
                           errors=("AHIF-COMPILER-REALISM-MATERIAL-CONFLICT",))
    realism_directives = realism.get("compiler_directives", {})
    camera = {str(x).lower() for x in realism_directives.get("camera", [])}
    if "deep depth of field" in camera and "shallow depth of field" in camera:
        return StageResult({}, Status.BLOCKED,
                           errors=("AHIF-COMPILER-REALISM-OPTICS-CONTRADICTION",))
    context = value["context"]
    scene = f"{context['atmosphere']} in {context['place']}, {context['location']}"
    effects, negatives = [], list(context["constraints"])
    for directive in value["directives"]:
        effects.extend(f"{key}: {item}" for key, item in sorted(directive["effects"].items()))
        negatives.extend(directive["constraints"])
    sections = {
        "identity": "Preserve the bound canonical identity; do not substitute identity.",
        "scene": scene,
        "directives": "; ".join(sorted(set(effects))),
        "realism": "; ".join(dict.fromkeys(
            item for group in ("capture", "human", "lighting", "camera", "environment",
                               "controlled_imperfections")
            for item in realism_directives.get(group, [])
        )),
    }
    prompt = "\n".join(f"{name.upper()}: {text}" for name, text in sections.items())
    negatives.extend(realism.get("negative_constraints", []))
    return StageResult({"positive_prompt": prompt, "negative_constraints": sorted(set(negatives)),
                        "identity_binding": value["identity"], "sections": sections,
                        "realism_contract": {"contract_version": realism["contract_version"],
                            "required_semantics": list(realism_directives)}})
