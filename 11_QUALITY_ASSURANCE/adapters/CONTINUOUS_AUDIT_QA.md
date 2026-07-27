# Continuous Audit QA

## Failure catalog

- `AHIF-AUD-001` repository identity or version cannot be resolved;
- `AHIF-AUD-002` audit scope fingerprint is absent or inconsistent;
- `AHIF-AUD-003` active rule-set cannot be resolved;
- `AHIF-AUD-004` governed snapshot is incomplete;
- `AHIF-AUD-005` canonical release files disagree;
- `AHIF-AUD-006` manifest path is unresolved;
- `AHIF-AUD-007` JSON parsing or baseline invariant fails;
- `AHIF-AUD-008` unexpected local Markdown link is broken;
- `AHIF-AUD-009` append-only registry integrity is not demonstrated;
- `AHIF-AUD-010` unsupported empirical or operational claim is detected;
- `AHIF-AUD-011` exception is expired, unapproved, or scope mismatched;
- `AHIF-AUD-012` auditor and exception approver violate role separation;
- `AHIF-AUD-013` remediation lacks validation or rollback boundary;
- `AHIF-AUD-014` adverse finding or residual risk was removed;
- `AHIF-AUD-015` closure evidence is incomplete;
- `AHIF-AUD-016` audit attempts an operational or adapter-state mutation.

Any critical integrity or fabrication failure blocks audit closure.
