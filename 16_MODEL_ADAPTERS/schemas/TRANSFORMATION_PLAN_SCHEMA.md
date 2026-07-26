# Transformation Plan Schema

## Canonical Shape

```json
{
  "schema_version": "1.0",
  "source_package_id": "fpkg-0001",
  "adapter": {
    "id": "ahif.adapter.example",
    "version": "1.0.0"
  },
  "operations": [
    {
      "operation_id": "op-001",
      "source_directive_id": "identity.face-001",
      "action": "map",
      "target_field": "prompt.identity",
      "compatibility": "native",
      "loss": false,
      "reason": "Direct semantic mapping is supported."
    }
  ],
  "degradations": [],
  "blocking_findings": [],
  "plan_status": "ready"
}
```

## Plan Status

- `ready`;
- `degraded`;
- `blocked`.

All source directives must be accounted for by an operation, an explicit degradation, or a blocking finding.
