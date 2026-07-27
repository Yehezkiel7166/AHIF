# Sprint 018 — Adapter Release Execution Governance

## Version

2.6.0

## Objective

Add the deterministic and auditable release-action layer required to apply an authorized adapter promotion or downgrade decision without permitting automatic, undeclared, or non-reproducible registry mutation.

## Delivered

- R0–R9 adapter release execution protocol;
- release package, immutable snapshot, rollback, and registry governance;
- release plan, package manifest, event, and snapshot schemas;
- append-only zero-release execution registry baseline;
- adapter release execution QA with `AHIF-REL-001` through `AHIF-REL-014`;
- contract and registry regression tests;
- illustrative blocked release-plan example.

## Source-of-truth decision

Sprint 017 completed the governance boundary between evaluation evidence and an authorized adapter-tier recommendation. The next unresolved boundary is applying such an authorization to the repository safely. Sprint 018 therefore defines release execution while preserving a zero-release baseline because the repository includes no real evidence, completed evaluations, authorized promotion dossiers, or owner-approved adapter mutations.

## Corrections

- synchronized the README version header from stale `2.4.0` to `2.6.0`;
- corrected manifest pointers for the latest sprint, upload guide, and release validation report.

## Claim boundary

No real release plan, approval, deployment, rollback, adapter-tier change, or production-support certification is included.

## Compatibility

Backward compatible with AHIF 2.5.0. No previous contract or repository file is removed.
