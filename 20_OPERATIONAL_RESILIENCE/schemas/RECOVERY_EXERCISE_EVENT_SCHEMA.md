# Recovery Exercise Event Schema

Required fields:

- `event_id`, `exercise_id`, `plan_id`, `event_type`;
- `actor_role`, `occurred_at`, `sequence`;
- `input_digest`, `result`, `observations`;
- `evidence_references`, `previous_event_digest`, `event_digest`.

Events are append-only and ordered. Permitted result values are `pass`, `fail`, `blocked`, and `not-evaluated`; missing evidence cannot produce `pass`.
