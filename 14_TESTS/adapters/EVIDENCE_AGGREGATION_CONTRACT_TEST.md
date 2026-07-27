# Evidence Aggregation Contract Test

## Positive cases

- two eligible bundles from one explicit cohort aggregate reproducibly;
- multiple cohorts remain separately visible;
- limiting confidence dimensions are recorded;
- recommendation remains advisory until governance approval.

## Negative cases

- missing source bundle fails `AHIF-AGG-002`;
- duplicate bundle fails `AHIF-AGG-003`;
- hidden cohort merge fails `AHIF-AGG-004`;
- non-reproducible confidence fails `AHIF-AGG-005`;
- critical identity failure with approval decision fails `AHIF-AGG-006`;
- absent provenance fails `AHIF-AGG-010`.
