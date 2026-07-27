# Audit Finding Event Schema

Required fields:

- `event_id`, `audit_id`, `finding_id`, `event_type`, `occurred_at`;
- `rule_id`, `severity`, `affected_paths[]`, `evidence_refs[]`;
- `previous_state`, `new_state`, `reason`;
- `actor_role`, `scope_fingerprint`, `previous_event_hash`, `event_hash`.

Allowed finding states: `open`, `accepted_exception`, `remediation_pending`, `validation_pending`, `closed`, and `blocked`.
