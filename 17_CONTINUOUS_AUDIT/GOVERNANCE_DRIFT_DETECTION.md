# Governance Drift Detection

## Drift classes

- `version_drift`: release identifiers disagree across canonical files;
- `manifest_drift`: declared paths, latest sprint, or status no longer match reality;
- `documentation_drift`: workflows and AI context describe different obligations;
- `registry_drift`: schema, counters, or append-only history diverges;
- `contract_drift`: compatibility or role-separation guarantees change silently;
- `claim_drift`: documentation implies evidence, execution, or certification not present.

## Detection method

1. Hash the governed baseline set.
2. Resolve current canonical values.
3. Compare structural and semantic invariants.
4. Record each difference with source, expected state, observed state, and confidence.
5. Classify intended, accepted-exception, unresolved, or blocked.

A changed hash alone is not a defect. A finding requires a violated rule or an undocumented contract change.
