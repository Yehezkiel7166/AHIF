# Promotion Decision Event Schema

```json
{
  "schema_version": "1.0.0",
  "event_id": "ahif:promotion-event:...",
  "dossier_id": "ahif:promotion-dossier:...",
  "sequence": 1,
  "event_type": "created|review_started|finding_added|recommendation_recorded|authorization_recorded|revision_requested|blocked|cancelled|superseded",
  "actor_role": "string",
  "previous_state": "string|null",
  "next_state": "string",
  "payload_fingerprint": "sha256:<64 lowercase hex>",
  "previous_event_fingerprint": "sha256:<64 lowercase hex>|null",
  "event_fingerprint": "sha256:<64 lowercase hex>",
  "external_timestamp": "string|null"
}
```

## Constraints

- sequence values are strictly monotonic per dossier;
- previous-event fingerprints form an unbroken chain;
- events are never overwritten or removed;
- external timestamps and actor identities are supplied by the operating owner;
- the event cannot mutate the adapter registry.
