# Empirical Evidence Contract Test

## Test objective

Verify that empirical evidence records remain complete, immutable, identity-safe, and auditable.

## Acceptance cases

1. Complete bundle passes all EV-QA gates.
2. Missing canonical checksum fails with `AHIF-EV-001`.
3. Missing Final Prompt Package reference fails with `AHIF-EV-002`.
4. Credential-bearing output URI fails with `AHIF-EV-008`.
5. A generated output declared as canonical identity fails with `AHIF-EV-010`.
6. An accepted bundle without two independent identity reports cannot support promotion.
7. A corrected accepted bundle creates a superseding identifier rather than mutating history.
8. Unknown runtime version is accepted only when disclosed.
9. Promotion to preview fails below reproducibility level R3.
10. Production certification fails below reproducibility level R4.

## Pass condition

All blocking cases produce the documented failure code and no unsupported support-tier claim is emitted.
