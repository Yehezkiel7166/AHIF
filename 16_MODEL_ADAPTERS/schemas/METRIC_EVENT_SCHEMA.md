# Metric Event Schema

Append-only events require:

- `event_id`, `metric_id`, `specification_version`;
- `event_type`, `previous_state`, `new_state`;
- `actor_role`, `timestamp`, `reason`;
- `related_snapshot_id`, `related_finding_ids`;
- `previous_event_hash`, `event_hash`.

Allowed event types include specification-created, approved, snapshot-calculated, review-blocked, published, superseded, and retired.
