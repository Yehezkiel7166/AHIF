# Metric Snapshot Schema

Required fields:

- `snapshot_id`, `metric_id`, `specification_version`;
- `source_record_ids`, `source_fingerprints`, `source_window`;
- `numerator`, `denominator`, `value`, `unit`;
- `calculation_state`, `threshold_state`, `data_quality_state`;
- `exclusions`, `warnings`, `precision`;
- `calculation_fingerprint`, `calculated_at`;
- `reviewer`, `reviewed_at`, `publication_state`;
- `claim_boundary`.

When the denominator is undefined or the population is empty, `value` must be null and `calculation_state` must be `not-evaluated`.
