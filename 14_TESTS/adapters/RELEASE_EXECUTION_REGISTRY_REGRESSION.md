# Release Execution Registry Regression

## Invariants

1. registry JSON parses successfully;
2. baseline record count is zero;
3. release IDs and scope fingerprints are unique when records exist;
4. events are contiguous and append-only;
5. completed records have authorization, package manifest, both snapshots, rollback readiness, approval, validation, and signoff;
6. every changed path is declared in the package manifest;
7. final tier equals the authorized tier;
8. failed or rolled-back history is retained;
9. no release changes canonical identity authority;
10. no support claim exceeds recorded evidence.

## Current baseline

Expected counts for AHIF 2.6.0:

```json
{
  "release_plans": 0,
  "approved_releases": 0,
  "executed_releases": 0,
  "completed_releases": 0,
  "rolled_back_releases": 0,
  "adapter_tier_changes": 0
}
```
