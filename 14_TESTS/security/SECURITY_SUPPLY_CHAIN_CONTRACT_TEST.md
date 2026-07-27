# Security and Supply Chain Contract Test

## Required assertions

1. S0–S9 stages exist and remain ordered.
2. Empty registries contain zero records and status is `not-evaluated`.
3. Findings never include raw secrets.
4. Unknown executable provenance blocks release eligibility.
5. Missing checksums remain explicitly unavailable, not fabricated.
6. Critical secret exposure cannot receive an exception.
7. Finding events are append-only and fingerprint chained.
8. Remediation requires independent validation.
9. Repository review does not claim infrastructure penetration testing.
10. Security status cannot mutate adapter tier or execute a release.

Expected baseline result: structural conformance only; no security certification.
