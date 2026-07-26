# Adapter Result Schema

## Canonical Shape

```json
{
  "schema_version": "1.0",
  "source_package_id": "fpkg-0001",
  "adapter_id": "ahif.adapter.example",
  "adapter_version": "1.0.0",
  "compatibility": "compatible",
  "release_state": "released",
  "target_request": {},
  "transformation_plan": {},
  "conformance": {
    "identity_preserved": true,
    "mandatory_directives_preserved": true,
    "undeclared_loss_detected": false,
    "trace_complete": true
  },
  "warnings": [],
  "blocking_findings": []
}
```

## Release States

- `released`;
- `released_with_degradation`;
- `blocked`.

The result is blocked whenever identity preservation or mandatory directive preservation is false.
