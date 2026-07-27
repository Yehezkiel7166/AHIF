# Evidence Aggregate Schema

```json
{
  "aggregate_id": "agg.<adapter>.<date>.<revision>",
  "schema_version": "1.0.0",
  "adapter_profile_id": "string",
  "model_scope": ["string"],
  "protocol_versions": ["string"],
  "source_bundle_ids": ["string"],
  "cohorts": [{
    "cohort_id": "string",
    "bundle_count": 0,
    "scenario_classes": ["string"],
    "metrics": {
      "identity": 0.0,
      "semantic": 0.0,
      "reproducibility": 0.0
    }
  }],
  "confidence": {
    "score": 0.0,
    "class": "C0|C1|C2|C3|C4",
    "limiting_dimensions": ["string"]
  },
  "outliers": ["string"],
  "drift_findings": ["string"],
  "claim_boundary": "string",
  "provenance": {"generated_at": "ISO-8601", "generator_version": "string"}
}
```

All source bundle identifiers are mandatory. Aggregates containing no eligible source bundles are invalid.
