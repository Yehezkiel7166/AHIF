# Continuous Audit Report Schema

Required fields:

- `audit_id`, `schema_version`, `repository_version`, `source_fingerprint`;
- `scope`, `ruleset_version`, `scope_fingerprint`;
- `snapshot_id`, `started_at`, `completed_at`;
- `checks[]`, `findings[]`, `exceptions[]`, `residual_risks[]`;
- `auditor_role`, `reviewer_role`, `closure_authority_role`;
- `status`: `passed`, `passed_with_findings`, `blocked`, or `cancelled`;
- `claim_boundaries` and append-only event references.

Actor identifiers may be absent in templates and baselines. They must never be fabricated.
