# Release Observation Plan Schema

```json
{
  "schema_version": "1.0.0",
  "observation_id": "ahif:release-observation:...",
  "observation_scope_fingerprint": "sha256:<64 lowercase hex>",
  "framework_version": "2.7.0",
  "state": "planned|observing|evaluated|healthy|watch|contain|rollback_recommended|blocked|cancelled",
  "release": {
    "release_id": "string",
    "release_fingerprint": "sha256:<64 lowercase hex>",
    "package_manifest_fingerprint": "sha256:<64 lowercase hex>",
    "pre_change_snapshot_fingerprint": "sha256:<64 lowercase hex>",
    "post_change_snapshot_fingerprint": "sha256:<64 lowercase hex>"
  },
  "adapter": {
    "adapter_id": "string",
    "adapter_version": "string",
    "support_tier": "string"
  },
  "observation_window": {
    "opened_at": "RFC3339 timestamp",
    "closes_at": "RFC3339 timestamp",
    "window_policy_version": "string"
  },
  "declared_signals": [],
  "roles": {
    "observation_owner_role": "string",
    "validator_role": "string",
    "rollback_verifier_role": "string",
    "response_authorizer_role": "string",
    "separation_satisfied": false
  },
  "rollback_assurance": {
    "status": "ready|degraded|invalid|not_applicable",
    "verification_fingerprint": "sha256:<64 lowercase hex>|null"
  },
  "outcome": "null|healthy|watch|contain|rollback_recommended|blocked|cancelled",
  "failure_codes": [],
  "events": []
}
```

## Constraints

- the source release must be completed and signed;
- scope and governed references become immutable after `observing`;
- undeclared signals cannot influence the outcome;
- `healthy` requires all mandatory gates and valid role separation;
- `rollback_recommended` cannot mutate the repository;
- model-output claims require accepted external evidence records.
