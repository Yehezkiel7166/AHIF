# Adapter Profile Schema

## Canonical Shape

```json
{
  "schema_version": "1.0",
  "adapter_id": "ahif.adapter.example",
  "adapter_version": "1.0.0",
  "target_family": "example-model",
  "target_version_range": ">=1 <2",
  "status": "experimental",
  "capabilities": {
    "identity_reference": {
      "support": "native",
      "criticality": "identity_critical"
    },
    "negative_prompt": {
      "support": "translated",
      "criticality": "semantic_required"
    }
  },
  "schemas": {
    "request": "path/to/request-schema",
    "result": "16_MODEL_ADAPTERS/schemas/ADAPTER_RESULT_SCHEMA.md"
  },
  "conformance_suite": "14_TESTS/adapters/ADAPTER_CONFORMANCE_TEST.md"
}
```

## Validation Rules

- `adapter_id` and `adapter_version` are required.
- Every declared capability includes support and criticality.
- Unknown capabilities default to `unknown`, never `native`.
- Production status requires a conformance suite.
- Profile versions are immutable.
