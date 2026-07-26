# Compiler Plan Schema

```json
{
  "schema_version": "1.0",
  "scene_id": "stable-scene-identifier",
  "status": "planned",
  "profile": "neutral-still-image-v1",
  "sections": [
    {
      "name": "identity",
      "order": 1,
      "units": [
        {
          "id": "C-001",
          "source_reasoning_chain": "R-001",
          "priority": 100,
          "statement": "normalized compiler instruction",
          "required": true,
          "confidence": 0.98,
          "provenance": ["02_CORE_IDENTITY/CANONICAL_IDENTITY.md"]
        }
      ]
    }
  ],
  "contradictions": [],
  "warnings": []
}
```

## Validation

- all required canonical sections must exist
- section order must match `SECTION_ORDERING.md`
- unit IDs must be unique
- every unit must reference an accepted reasoning chain
- blocked or revision-required reasoning input cannot produce `planned`
- unresolved contradictions prohibit serialization
