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
  "registry_status": "experimental",
  "realism_mapping": {
    "semantic_preservation": "verbatim-prompt",
    "lossy_mappings": [],
    "unsupported_parameters": [],
    "empirical_quality": "NOT_EVALUATED"
  },
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
Realism mapping reports semantic transport only. Unsupported parameters and lossy mappings must be
explicit; the field never certifies generated-image quality or promotes an adapter tier.
