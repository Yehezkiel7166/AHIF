# Target Request Schema

## Required Fields

```json
{
  "schema_version": "1.0.0",
  "adapter_id": "string",
  "adapter_version": "string",
  "profile_id": "string",
  "source_package_hash": "sha256",
  "target_family": "string",
  "target_request": {},
  "semantic_map": [],
  "parameter_map": [],
  "loss_report": [],
  "identity_preservation_status": "preserved | degraded | blocked",
  "adapter_status": "experimental | supported",
  "reproducibility": {}
}
```

## Validation

Unknown top-level fields are rejected in strict mode. A `blocked` identity status requires an empty executable target request. Every loss entry identifies source directive, criticality, mapping outcome, reason, and release effect.
