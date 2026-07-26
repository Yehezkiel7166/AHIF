# Cross-Model Compatibility QA

## Mandatory Gates

1. Same source Final Prompt Package for all compared adapters.
2. Exact adapter and profile resolution.
3. Valid adapter result and target request schemas.
4. Complete semantic-domain evidence.
5. Identity-domain confidence at or above `0.95`.
6. No identity-critical loss or fallback.
7. Complete negative-constraint preservation.
8. Complete loss and variance disclosure.
9. Deterministic compatibility report.
10. Correct release recommendation.

## Failure Codes

- `AHIF-COMP-001`: source package mismatch
- `AHIF-COMP-002`: unresolved adapter or profile
- `AHIF-COMP-003`: missing semantic evidence
- `AHIF-COMP-004`: identity preservation below floor
- `AHIF-COMP-005`: undeclared loss
- `AHIF-COMP-006`: incompatible negative-constraint mapping
- `AHIF-COMP-007`: nondeterministic comparison
- `AHIF-COMP-008`: invalid promotion recommendation

## Decision

Any identity failure is `blocked`. Missing evidence or undeclared loss is `fail`. Non-critical approved variance may pass with disclosure. Version 1.9.0 retains experimental adapter status regardless of request-level pass because empirical image-output validation is not yet complete.
