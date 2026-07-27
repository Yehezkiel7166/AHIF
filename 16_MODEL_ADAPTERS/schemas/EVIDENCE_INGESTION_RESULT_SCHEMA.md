# Evidence Ingestion Result Schema

```json
{
  "schema_version": "1.0.0",
  "request_id": "string",
  "decision": "accepted|quarantined|rejected|duplicate",
  "record_id": "string|null",
  "policy_version": "2.3.0",
  "failure_codes": ["AHIF-ING-..."],
  "warnings": ["string"],
  "integrity_summary": {
    "verified": 0,
    "declared_only": 0,
    "mismatch": 0,
    "unavailable": 0
  },
  "duplicate_match": {"record_id": "string|null", "match_type": "none|exact|related"},
  "required_actions": ["string"],
  "adapter_status_changed": false
}
```

`adapter_status_changed` must always be false for ingestion operations.