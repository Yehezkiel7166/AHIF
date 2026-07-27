# Security Finding Event Schema

Required fields:

- `event_id`, `finding_id`, `event_type`, `sequence`;
- `previous_event_fingerprint`;
- `actor_role` and signed timestamp;
- redacted `locator`;
- `severity`, `confidence`, `status`;
- evidence references and remediation references;
- event fingerprint.

Allowed states: `open`, `triaged`, `remediation-planned`, `remediated`, `validated`, `accepted-risk`, `rejected`, `closed`. Events are append-only.
