"""Explainable, non-chain-of-thought reasoning handoff stage."""
from typing import Any, Mapping
from .contracts import StageResult, require_mapping


def _realism_contract(context: Mapping[str, Any]) -> dict[str, Any]:
    """Resolve auditable realism semantics from capture context, not aesthetics."""
    joined = " ".join(str(context.get(k, "")) for k in
                      ("location", "place", "atmosphere", "activity", "weather", "time")).lower()
    surface = ["natural skin texture with restrained visible pores",
               "subtle tonal variation and natural fine lines",
               "realistic under-eye transition and lip texture",
               "realistic skin highlights without beautification",
               "natural hair strand separation with context-driven flyaways"]
    anatomy = ["natural facial asymmetry and expression tension",
               "anatomically plausible posture, hands, joints, gravity, balance, and contact pressure"]
    lighting = ["one coherent key, fill, and environmental lighting model",
                "physically plausible shadows, skin response, reflections, and color temperature"]
    camera = ["realistic optical depth", "natural dynamic range and highlight roll-off",
              "restrained sharpening with plausible shadow detail"]
    environment = ["subject and background share light direction and atmospheric perspective",
                   "believable edge transitions, scale, contact shadows, and environmental color bounce"]
    styling = ["pose, fashion, accessories, hairstyle, expression, and framing follow current context, not master-photo appearance"]
    capture = "contextual environmental portrait"
    if any(x in joined for x in ("night", "neon", "evening")):
        capture = "available-light urban night photograph"
        lighting += ["practical neon and ambient fill with coherent neon reflections"]
        camera += ["plausible low-light exposure with motion handling appropriate to the activity"]
    elif "sunset" in joined:
        capture = "available-light sunset environmental portrait"
        lighting += ["physically coherent sunset key light with plausible shadow softness"]
    if any(x in joined for x in ("beach", "shore", "coast")):
        styling += ["functional modest tropical clothing and a natural beach activity pose",
                    "hair responds naturally to coastal wind"]
    if any(x in joined for x in ("swiss", "alps", "mountain", "cool", "cold")):
        styling += ["functional cool-weather layers appropriate to café activity"]
        camera += ["moderate depth of field retaining readable mountain-café context"]
    risks = ["waxy or plastic skin", "porcelain face", "excessive facial symmetry",
             "oversized artificial eyes", "over-smoothed skin", "fake pore texture",
             "excessive sharpening", "edge halos", "synthetic bokeh", "incoherent shadows",
             "pasted subject", "inconsistent reflections", "malformed hands",
             "floating accessories", "duplicated people", "text artifacts", "watermark"]
    return {"contract_version": "1.0", "compiler_ready": True,
            "intended_photographic_capture": capture,
            "human_surface_realism": surface, "anatomical_realism": anatomy,
            "lighting_model": lighting, "camera_plausibility": camera,
            "environmental_integration": environment, "controlled_imperfections": styling,
            "artifact_risks": risks, "negative_constraints": risks,
            "confidence": "high", "unresolved_uncertainties": [], "qa_flags": [],
            "compiler_directives": {"capture": [capture], "human": surface + anatomy,
                "lighting": lighting, "camera": camera, "environment": environment,
                "controlled_imperfections": styling}}


def run_reasoning(payload: Mapping[str, Any]) -> StageResult:
    value = require_mapping(payload, "reasoning_input")
    items = [{"rule_id": d["rule_id"], "outcome": "accepted", "basis": "registered-rule"}
             for d in value["decision"]["decisions"]]
    context = value["decision"]["context"]
    return StageResult({"context": context, "identity": value["identity"],
                        "decision_record": items, "directives": value["decision"]["decisions"],
                        "realism": _realism_contract(context)})
