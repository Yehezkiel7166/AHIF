# Adapter Incident Event Schema

```json
{
  "event_id": "AHIF-INC-EVT-YYYY-NNNN",
  "incident_id": "AHIF-INC-YYYY-NNNN",
  "sequence": 1,
  "event_type": "incident_opened",
  "from_status": null,
  "to_status": "opened",
  "actor_role": "incident_commander",
  "actor_id": "external-or-user-provided",
  "occurred_at": "RFC3339",
  "previous_event_hash": null,
  "payload_hash": "sha256:<hex>",
  "notes": "string"
}
```

Valid event types include intake, classification, authorization, containment, recovery, validation, resolution, closure, block, cancel, and correction events.
