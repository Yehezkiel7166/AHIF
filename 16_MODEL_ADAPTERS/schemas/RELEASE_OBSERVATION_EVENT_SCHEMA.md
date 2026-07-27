# Release Observation Event Schema

```json
{
  "schema_version": "1.0.0",
  "event_id": "ahif:release-observation-event:...",
  "observation_id": "ahif:release-observation:...",
  "sequence": 1,
  "event_type": "created|observation_started|signal_recorded|evaluated|rollback_verified|response_authorized|completed|blocked|cancelled|amended",
  "previous_state": "string|null",
  "resulting_state": "string",
  "actor_role": "string",
  "occurred_at": "RFC3339 timestamp",
  "payload_fingerprint": "sha256:<64 lowercase hex>",
  "previous_event_fingerprint": "sha256:<64 lowercase hex>|null",
  "event_fingerprint": "sha256:<64 lowercase hex>"
}
```

## Constraints

- sequence numbers are contiguous and unique per observation;
- event fingerprints form an append-only chain;
- amendments append corrections and never rewrite history;
- response authorization must reference the exact evaluated outcome fingerprint.
