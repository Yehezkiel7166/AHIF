# Evidence Ingestion Request Schema

```json
{
  "schema_version": "1.0.0",
  "request_id": "ahif-ingestion-request:<uuid>",
  "submitted_at": "RFC3339 timestamp",
  "submitted_by": {"type": "owner|operator|reviewer", "identifier": "string"},
  "bundle": {
    "bundle_id": "string",
    "execution_id": "string",
    "adapter_id": "string",
    "adapter_version": "string",
    "model_id": "string",
    "model_version": "string",
    "prompt_package_id": "string",
    "target_request_sha256": "64 lowercase hex"
  },
  "artifacts": [
    {
      "artifact_id": "string",
      "role": "canonical_input_reference|prompt_package|target_request|generated_output|execution_log|evaluation_report",
      "path": "relative path or governed reference",
      "media_type": "string",
      "size_bytes": 0,
      "sha256": "64 lowercase hex",
      "availability": "available|external|missing"
    }
  ],
  "evaluation_reports": {
    "identity_report_id": "string|null",
    "semantic_report_id": "string|null"
  },
  "declarations": {
    "external_execution": true,
    "generated_output_is_not_canonical_identity": true,
    "no_secrets_included": true
  }
}
```

## Validation rules

- IDs are non-empty and stable.
- Digests use lowercase SHA-256 hexadecimal format.
- Paths cannot be absolute or contain traversal segments.
- At least one `generated_output` and one `target_request` declaration are required for empirical acceptance.
- All declarations must be true.