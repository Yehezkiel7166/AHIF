# LTS Release Record Schema

Required fields:

- `release_id`, `version`, `release_line`, `status`;
- `scope`, `exclusions`, `claim_boundary`;
- `contract_inventory_digest`, `documentation_set_digest`;
- `migration_required`, `migration_document`;
- `author`, `independent_reviewer`, `release_authorizer`;
- `review_findings`, `residual_risk`, `decision`;
- `created_at`, `reviewed_at`, `accepted_at`, `next_review_at`;
- `previous_record_digest`, `record_digest`.

Permitted status values are `draft`, `review`, `accepted`, `held`, `rejected`, `superseded`, and `retired`.

An accepted record proves only that repository-level LTS governance gates were satisfied. It does not prove production deployment, empirical model performance, security certification, or operational resilience execution.
