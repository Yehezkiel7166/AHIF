# Target Profile Recommendation Schema

```json
{
  "recommendation_id": "tpr.<adapter>.<revision>",
  "schema_version": "1.0.0",
  "aggregate_id": "string",
  "adapter_profile_id": "string",
  "model_version_scope": ["string"],
  "recommended_defaults": {},
  "required_constraints": ["string"],
  "unsupported_scenarios": ["string"],
  "confidence_class": "C0|C1|C2|C3|C4",
  "decision": "hold|candidate|approve|deprecate",
  "requires_human_approval": true,
  "rationale": ["string"],
  "provenance": {"aggregate_id": "string", "review_id": "string"}
}
```

`requires_human_approval` must always be true for approval or deprecation decisions.
