# Security Audit Report Schema

Required top-level fields:

```json
{
  "schema_version": "1.0.0",
  "run_id": "security-run-id",
  "scope": {},
  "ruleset_version": "1.0.0",
  "inventory_snapshot_fingerprint": "sha256:...",
  "finding_ids": [],
  "exception_ids": [],
  "release_eligibility": "eligible|blocked|not-evaluated",
  "limitations": [],
  "review": {},
  "report_fingerprint": "sha256:..."
}
```

The report must never contain raw secret values or imply external infrastructure coverage beyond its declared scope.
