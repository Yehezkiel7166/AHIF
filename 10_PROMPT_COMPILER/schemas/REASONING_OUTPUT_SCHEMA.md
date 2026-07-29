# Reasoning Output Schema

## Purpose

This schema defines the machine-readable handoff from the Reasoning Engine to the Prompt Compiler.

```json
{
  "schema_version": "1.0",
  "scene_id": "stable-scene-identifier",
  "status": "compiler-ready",
  "premises": [
    {
      "id": "P-001",
      "type": "user|identity|knowledge|derived|constraint",
      "statement": "normalized factual statement",
      "source": "repository path or graph identifier",
      "confidence": 0.95
    }
  ],
  "reasoning_chains": [
    {
      "id": "R-001",
      "domain": "fashion",
      "decision": "accepted decision",
      "premise_ids": ["P-001"],
      "constraints": ["identity-visibility"],
      "reason": "causal explanation",
      "cross_domain_effects": ["behavior", "camera"],
      "confidence": 0.90,
      "compiler_directive": "ordered prompt instruction"
    }
  ],
  "rejected_alternatives": [
    {
      "alternative": "rejected option",
      "code": "weather-mismatch",
      "reason": "concise explanation"
    }
  ],
  "uncertainties": [],
  "confidence": {
    "identity": 0.98,
    "context": 0.90,
    "aggregate": 0.91
  },
  "qa_flags": []
  ,"realism": {
    "contract_version": "1.0",
    "compiler_ready": true,
    "intended_photographic_capture": "context-derived capture intent",
    "human_surface_realism": [],
    "anatomical_realism": [],
    "lighting_model": [],
    "camera_plausibility": [],
    "environmental_integration": [],
    "controlled_imperfections": [],
    "artifact_risks": [],
    "confidence": "high",
    "unresolved_uncertainties": [],
    "compiler_directives": {},
    "qa_flags": []
  }
}
```

## Validation rules

- `status` must be `compiler-ready`, `revision-required`, or `blocked`.
- every reasoning chain must reference at least one premise
- every compiler directive must derive from an accepted decision
- identity confidence below `0.85` requires `blocked`
- unsupported facts must not appear in compiler directives
- realism directives compile only when `compiler_ready` is true and material uncertainties are resolved
- camera, lens, optics, or styling absent from accepted reasoning must not be invented
