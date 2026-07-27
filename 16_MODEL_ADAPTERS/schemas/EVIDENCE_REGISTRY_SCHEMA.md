# Evidence Registry Schema

The machine-readable registry contains:

```json
{
  "schema_version": "1.0.0",
  "registry_id": "ahif:empirical-evidence-registry",
  "policy_version": "2.3.0",
  "append_only": true,
  "record_count": 0,
  "records": []
}
```

Each record must include stable IDs, status, adapter/model versions, fingerprints, provenance, report links, decision timestamp, and governance relationships. `record_count` must equal the length of `records`.

The zero-record registry is a valid baseline and makes no empirical claims.