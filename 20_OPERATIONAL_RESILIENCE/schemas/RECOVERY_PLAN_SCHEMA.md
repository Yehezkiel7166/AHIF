# Recovery Plan Schema

Required fields:

- `plan_id`, `schema_version`, `plan_version`, `status`;
- `scope`, `criticality_tier`, `owners`, `approvers`;
- `dependencies`, `rto`, `rpo`, `mtd`;
- `prerequisites`, `ordered_steps`, `stop_conditions`;
- `validation_checks`, `rollback_or_abort`;
- `communications`, `residual_risk`;
- `scope_fingerprint`, `created_at`, `review_due_at`.

Status values: `draft`, `review`, `approved`, `expired`, `blocked`, `retired`. Approval does not equal successful execution.
