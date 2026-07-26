# Compiler Metadata

## Purpose

Compiler metadata makes the final prompt reproducible, auditable, and suitable for QA without exposing private reasoning.

## Required fields

```json
{
  "compiler_version": "1.4.0",
  "profile": "neutral-still-image-v1",
  "scene_id": "stable-scene-identifier",
  "source_schema_version": "1.0",
  "identity_lock_present": true,
  "sections": ["identity", "scene", "activity", "human", "styling", "environment", "photography", "lighting", "realism", "negative"],
  "directive_count": 0,
  "consolidated_directive_count": 0,
  "source_reasoning_chains": [],
  "warnings": [],
  "checksum_basis": "normalized compiler plan"
}
```

## Constraints

- metadata must not contain hidden chain-of-thought
- source IDs may be recorded without reproducing private reasoning text
- every visible material instruction must be traceable to at least one source chain
- metadata warnings must be passed to QA unchanged
