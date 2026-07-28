# LTS Status Schema

Required fields:

- `schema_version`, `status`, `release_version`, `source_commit`;
- `repository_validation`, `governance_validation`, `operational_validation`;
- `registered_releases`, `maintenance_events`, `open_blockers`;
- `last_assessed_at`, `claim_boundary`.

`status` is `not-evaluated`, `hold`, `candidate`, `designated`, `superseded`, or `retired`. Repository, governance, and operational validation are reported separately. A repository pass must not overwrite an unverified governance or operational plane.
