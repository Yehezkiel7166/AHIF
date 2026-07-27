# Release Execution Event Schema

```json
{
  "schema_version": "1.0.0",
  "event_id": "ahif:release-event:...",
  "release_id": "ahif:adapter-release:...",
  "sequence": 0,
  "event_type": "planned|candidate_built|validated|approved|execution_started|mutation_applied|post_validated|completed|rollback_started|rolled_back|blocked|failed|cancelled|amended",
  "actor_role": "string",
  "occurred_at": "RFC-3339 timestamp",
  "previous_state": "string|null",
  "resulting_state": "string",
  "release_scope_fingerprint": "sha256:<64 lowercase hex>",
  "artifact_fingerprints": [],
  "failure_codes": [],
  "notes": "string|null"
}
```

## Constraints

Sequence numbers are contiguous and immutable. The event fingerprint and release scope must remain consistent. Amendments append corrective information and never rewrite prior events.
