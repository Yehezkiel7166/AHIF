# Evidence Evaluation Job Schema

```json
{
  "schema_version": "1.0.0",
  "job_id": "ahif:eval:...",
  "record_id": "string",
  "scope_fingerprint": "sha256:<64 lowercase hex>",
  "policy_version": "2.4.0",
  "state": "queued|in_review|completed|needs_revision|blocked|cancelled",
  "dimensions": ["identity", "semantics", "reproducibility"],
  "pinned_inputs": {
    "adapter_id": "string",
    "adapter_version": "string",
    "capability_profile_version": "string",
    "scenario_id": "string",
    "canonical_package_id": "string",
    "identity_protocol_version": "string",
    "semantic_protocol_version": "string"
  },
  "required_reports": {
    "identity": "string|null",
    "semantic": "string|null",
    "reproducibility": "string|null"
  },
  "review": {
    "primary_actor_role": "string|null",
    "independent_actor_role": "string|null",
    "independent_review_required": true
  },
  "supersedes_job_id": "string|null",
  "events": [],
  "adapter_status_changed": false
}
```

## Constraints

- `record_id` must resolve to an accepted evidence registry record.
- `scope_fingerprint` must be derived from canonical governed inputs.
- all pinned versions are immutable after the first queue event;
- `completed` requires all requested reports and required independent review;
- `adapter_status_changed` must always be false.