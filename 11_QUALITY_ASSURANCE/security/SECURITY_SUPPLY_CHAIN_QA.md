# Security and Supply Chain QA

Stable failures:

- `AHIF-SEC-001` scope not pinned
- `AHIF-SEC-002` inventory incomplete
- `AHIF-SEC-003` provenance unknown
- `AHIF-SEC-004` integrity digest missing without reason
- `AHIF-SEC-005` suspected secret reproduced
- `AHIF-SEC-006` advisory evidence unverifiable
- `AHIF-SEC-007` reachability not assessed
- `AHIF-SEC-008` severity unsupported
- `AHIF-SEC-009` remediation lacks rollback
- `AHIF-SEC-010` remediation not independently validated
- `AHIF-SEC-011` exception expired or incomplete
- `AHIF-SEC-012` critical exposure improperly excepted
- `AHIF-SEC-013` append-only chain broken
- `AHIF-SEC-014` snapshot fingerprint mismatch
- `AHIF-SEC-015` release eligibility overclaimed
- `AHIF-SEC-016` external security certification fabricated

Any critical failure blocks security closure and release eligibility.
