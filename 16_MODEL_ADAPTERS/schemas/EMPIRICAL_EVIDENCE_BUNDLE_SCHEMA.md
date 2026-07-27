# Empirical Evidence Bundle Schema

## JSON shape

```json
{
  "schema_version": "1.0",
  "bundle_id": "AHIF-EVB-...",
  "status": "complete",
  "framework_version": "2.1.0",
  "final_prompt_package": {
    "id": "FPP-...",
    "sha256": "..."
  },
  "adapter": {
    "id": "...",
    "version": "...",
    "capability_profile_id": "..."
  },
  "execution": {
    "timestamp_utc": "...",
    "runtime_version": "unknown",
    "request_sha256": "...",
    "parameters": {},
    "seed_policy": "...",
    "retry_count": 0,
    "post_processing": "none"
  },
  "identity_reference": {
    "path": "assets/identity-reference/MASTER_PHOTO.jpg",
    "sha256": "..."
  },
  "outputs": [
    {
      "artifact_id": "...",
      "uri": "...",
      "sha256": "..."
    }
  ],
  "evaluations": {
    "identity_report_ids": [],
    "semantic_report_ids": []
  },
  "reproducibility_level": "R1_documented",
  "missing_metadata": [],
  "supersedes": null
}
```

## Validation rules

- all identifiers are non-empty and stable;
- all checksums use SHA-256;
- external URIs contain no credentials;
- `accepted` status requires linked evaluation reports;
- missing values are disclosed explicitly;
- generated outputs are never registered as canonical identity sources.
