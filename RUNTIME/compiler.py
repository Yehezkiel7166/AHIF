"""Canonical prompt compiler stage."""
from typing import Any, Mapping
from .contracts import StageResult, require_mapping


def compile_prompt(reasoning: Mapping[str, Any]) -> StageResult:
    value = require_mapping(reasoning, "reasoning")
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
    }
    prompt = "\n".join(f"{name.upper()}: {text}" for name, text in sections.items())
    return StageResult({"positive_prompt": prompt, "negative_constraints": sorted(set(negatives)),
                        "identity_binding": value["identity"], "sections": sections})
