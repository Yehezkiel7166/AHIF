# LTS Maintenance Event Schema

Required fields:

- `event_id`, `lts_release_id`, `schema_version`, `sequence`;
- `event_type`, `change_class`, `source_change`, `target_line`;
- `scope`, `compatibility_assessment`, `test_evidence`;
- `approval_references`, `rollback_instructions`, `result`;
- `occurred_at`, `previous_event_digest`, `event_digest`;
- `claim_boundary`.

Permitted `event_type` values are `review`, `correction`, `security-fix`, `compatibility-fix`, `backport`, `deprecation`, `supersession`, and `retirement`. Permitted results are `accepted`, `hold`, `rejected`, `reverted`, and `not-evaluated`. Events are append-only and digest-linked.
