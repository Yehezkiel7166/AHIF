# Release Observation Registry Regression

## Assertions

1. registry schema and framework versions are present;
2. baseline record count is zero;
3. every future observation ID and scope fingerprint is unique;
4. every event sequence is contiguous and append-only;
5. every record references one completed release;
6. `healthy` requires all QA gates and independent validation;
7. rollback recommendations do not mutate the repository;
8. unsupported empirical or production claims are rejected.

## Current baseline

```json
{
  "framework_version": "2.7.0",
  "records": []
}
```

Expected result: PASS with zero observation records.
