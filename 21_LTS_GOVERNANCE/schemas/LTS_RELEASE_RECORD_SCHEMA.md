# LTS Release Record Schema

Required fields:

- `lts_release_id`, `schema_version`, `release_version`, `source_commit`;
- `decision`, `support_level`, `scope`, `exclusions`;
- `compatibility_baseline`, `supported_predecessors`, `artifact_inventory`;
- `validation_evidence`, `unverified_requirements`, `blocking_findings`;
- `maintenance_policy_version`, `change_policy_version`;
- `review_cadence`, `planned_end_conditions`;
- `owner_roles`, `reviewer_roles`, `authorizer_roles`;
- `created_at`, `review_due_at`, `previous_record_digest`, `record_digest`;
- `claim_boundary`.

`decision` is one of `candidate`, `hold`, `designated`, `rejected`, `superseded`, or `retired`. A record with missing required evidence or any blocking finding cannot use `designated`.
