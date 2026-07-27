# Rollback Assurance Report Schema

```json
{
  "schema_version": "1.0.0",
  "assurance_id": "ahif:rollback-assurance:...",
  "observation_id": "ahif:release-observation:...",
  "release_id": "ahif:adapter-release:...",
  "status": "ready|degraded|invalid|not_applicable",
  "pinned_fingerprints": {
    "pre_change_snapshot": "sha256:<64 lowercase hex>",
    "post_change_snapshot": "sha256:<64 lowercase hex>",
    "package_manifest": "sha256:<64 lowercase hex>",
    "rollback_plan": "sha256:<64 lowercase hex>"
  },
  "reconstruction_checks": [],
  "role_separation_satisfied": false,
  "failure_codes": [],
  "report_fingerprint": "sha256:<64 lowercase hex>"
}
```

## Constraints

- all source fingerprints must resolve to the same completed release;
- `ready` requires exact reconstruction coverage for every declared changed path;
- this report cannot execute rollback or mutate the adapter registry.
