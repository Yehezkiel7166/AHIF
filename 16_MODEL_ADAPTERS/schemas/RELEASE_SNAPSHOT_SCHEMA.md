# Release Snapshot Schema

```json
{
  "schema_version": "1.0.0",
  "snapshot_id": "ahif:release-snapshot:...",
  "release_id": "ahif:adapter-release:...",
  "snapshot_type": "pre_change|post_change|rollback",
  "repository_version": "string",
  "captured_at": "RFC-3339 timestamp",
  "registry_state": {
    "path": "16_MODEL_ADAPTERS/ADAPTER_REGISTRY.md",
    "sha256": "sha256:<64 lowercase hex>",
    "adapter_id": "string",
    "adapter_version": "string",
    "support_tier": "string"
  },
  "affected_paths": [
    {
      "path": "string",
      "sha256": "sha256:<64 lowercase hex>|absent"
    }
  ],
  "snapshot_fingerprint": "sha256:<64 lowercase hex>"
}
```

## Constraints

The snapshot fingerprint covers canonical serialization except itself. A rollback snapshot must equal the pre-change snapshot for every affected path unless an independently authorized containment record documents an exception.
