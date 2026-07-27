# Release Package Manifest Schema

```json
{
  "schema_version": "1.0.0",
  "package_manifest_id": "ahif:release-package:...",
  "release_id": "ahif:adapter-release:...",
  "authorization_dossier_id": "string",
  "source_repository_fingerprint": "sha256:<64 lowercase hex>",
  "declared_mutations": [
    {
      "path": "string",
      "operation": "modify|add|remove",
      "before_sha256": "sha256:<64 lowercase hex>|null",
      "after_sha256": "sha256:<64 lowercase hex>|null",
      "purpose": "string"
    }
  ],
  "required_validations": [],
  "pre_change_snapshot_id": "string",
  "rollback_plan_id": "string",
  "package_fingerprint": "sha256:<64 lowercase hex>"
}
```

## Constraints

The package fingerprint covers canonical serialization of all fields except itself. Every repository mutation must be declared. Stable framework contract removals require a separately governed breaking release and are not permitted by the Sprint 018 backward-compatible workflow.
