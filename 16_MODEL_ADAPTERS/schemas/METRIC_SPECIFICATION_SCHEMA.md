# Metric Specification Schema

Required fields:

- `metric_id`, `name`, `specification_version`, `status`;
- `decision_purpose`, `owner_role`, `audience`;
- `formula`, `unit`, `numerator_definition`, `denominator_definition`;
- `eligible_sources`, `exclusions`, `deduplication_key`;
- `missing_data_policy`, `precision_policy`, `freshness_limit`;
- `threshold_policy_reference`, `claim_boundary`;
- `created_at`, `approved_by`, `supersedes`.

Published specifications are immutable. Any semantic change creates a new version.
