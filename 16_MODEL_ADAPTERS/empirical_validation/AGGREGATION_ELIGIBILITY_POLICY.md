# Aggregation Eligibility Policy

An evidence bundle is eligible only when all mandatory conditions pass.

## Mandatory conditions

1. Bundle conforms to the empirical evidence schema.
2. Evidence QA result is `pass`.
3. Identity evaluation is complete and references the canonical identity asset.
4. Semantic evaluation is complete.
5. Adapter, model, and protocol versions are recorded.
6. Required artifact hashes are present.
7. No unresolved critical failure code exists.
8. Consent and storage metadata satisfy repository policy.

## Exclusions

Exclude duplicate bundles, superseded runs, unverifiable artifacts, mixed canonical identities, and manually altered outputs without declared provenance.

## Cohort rules

A cohort groups evidence by adapter profile, model family, major model version, protocol version, and scenario class. Cross-cohort summaries may be produced, but may not conceal cohort-level variance.
