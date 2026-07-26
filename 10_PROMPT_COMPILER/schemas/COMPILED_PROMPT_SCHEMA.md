# Compiled Prompt Schema

```json
{
  "schema_version": "1.0",
  "compiler_version": "1.4.0",
  "status": "compiled",
  "scene_id": "stable-scene-identifier",
  "profile": "neutral-still-image-v1",
  "final_prompt": "complete model-neutral positive prompt",
  "negative_constraints": "relevant negative constraints",
  "metadata": {
    "identity_lock_present": true,
    "section_order_valid": true,
    "source_reasoning_chains": ["R-001"],
    "warnings": []
  },
  "qa_handoff": {
    "required": true,
    "checks": ["identity", "anatomy", "physics", "context", "camera", "lighting", "coherence"]
  }
}
```

## Validation

- `final_prompt` and `negative_constraints` cannot be empty
- identity lock must be present
- prompt content must match compiler metadata
- source reasoning chains must exist in the input record
- unresolved warnings must remain visible to QA
