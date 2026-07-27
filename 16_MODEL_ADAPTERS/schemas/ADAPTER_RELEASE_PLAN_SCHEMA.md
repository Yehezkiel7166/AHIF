# Adapter Release Plan Schema

```json
{
  "schema_version": "1.0.0",
  "release_id": "ahif:adapter-release:...",
  "release_scope_fingerprint": "sha256:<64 lowercase hex>",
  "framework_version": "2.6.0",
  "state": "planned|candidate_ready|approved|executing|completed|rolled_back|blocked|failed|cancelled",
  "authorization": {
    "dossier_id": "string",
    "dossier_fingerprint": "sha256:<64 lowercase hex>",
    "recommendation": "promote|downgrade",
    "authorization_event_id": "string"
  },
  "adapter": {
    "adapter_id": "string",
    "adapter_version": "string",
    "from_tier": "string",
    "to_tier": "string"
  },
  "pinned_versions": {
    "adapter_registry_version": "string",
    "support_policy_version": "string",
    "capability_profile_version": "string",
    "compatibility_contract_version": "string"
  },
  "package_manifest_id": "string",
  "pre_change_snapshot_id": "string",
  "post_change_snapshot_id": "string|null",
  "roles": {
    "release_owner_role": "string",
    "approver_role": "string",
    "validator_role": "string",
    "rollback_owner_role": "string",
    "separation_satisfied": false
  },
  "validation": {
    "candidate_passed": false,
    "post_change_passed": false,
    "failure_codes": []
  },
  "rollback": {
    "plan_id": "string",
    "ready": false,
    "executed": false
  },
  "changed_paths": [],
  "events": []
}
```

## Constraints

- the dossier must be authorized and recommend `promote` or `downgrade`;
- all governed versions and the pre-change snapshot are immutable after `candidate_ready`;
- `approved` requires candidate validation, rollback readiness, and role separation;
- `completed` requires exact declared mutations, successful post-change validation, and signoff;
- any undeclared mutation blocks completion;
- canonical identity authority cannot be changed by this schema.
