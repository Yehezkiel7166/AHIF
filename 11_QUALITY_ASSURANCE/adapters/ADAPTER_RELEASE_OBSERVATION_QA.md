# Adapter Release Observation QA

## Mandatory gates

1. observation plan and scope fingerprint are valid;
2. source release is completed, signed, and not superseded by rollback;
3. adapter, release, package, snapshots, policies, and observation window are pinned;
4. declared signal inventory is explicit and provenance-bounded;
5. observation baseline matches the signed post-change snapshot;
6. repository, contract, compatibility, and claim-boundary checks pass;
7. observation owner, validator, rollback verifier, and response authorizer satisfy separation rules;
8. rollback assurance covers every changed path and reconstructs the pre-change state;
9. state transitions and append-only event chain are valid;
10. evaluated outcome follows deterministic thresholds;
11. response authorization references the exact outcome fingerprint;
12. documentation, manifest, registries, and adapter tier remain consistent;
13. no health, empirical, or production claim exceeds available evidence;
14. observation does not mutate the adapter registry or execute rollback.

## Failure codes

| Code | Meaning | Default outcome |
|---|---|---|
| `AHIF-OBS-001` | observation plan or scope fingerprint invalid | blocked |
| `AHIF-OBS-002` | source release missing, incomplete, unsigned, or rolled back | blocked |
| `AHIF-OBS-003` | governed release reference or observation window not pinned | blocked |
| `AHIF-OBS-004` | undeclared or unverifiable signal source | blocked |
| `AHIF-OBS-005` | observation baseline mismatches post-change snapshot | contain |
| `AHIF-OBS-006` | contract, compatibility, or repository regression detected | contain |
| `AHIF-OBS-007` | role separation conflict | blocked |
| `AHIF-OBS-008` | rollback assurance degraded or invalid | watch |
| `AHIF-OBS-009` | invalid state transition or event chain | blocked |
| `AHIF-OBS-010` | outcome does not follow declared thresholds | blocked |
| `AHIF-OBS-011` | response authorization fingerprint mismatch | blocked |
| `AHIF-OBS-012` | duplicate active observation scope | cancelled |
| `AHIF-OBS-013` | documentation, manifest, registry, or tier inconsistency | contain |
| `AHIF-OBS-014` | unsupported empirical, health, or production claim | blocked |
| `AHIF-OBS-015` | observation attempted repository mutation or rollback execution | blocked |

## Completion gate

An observation may become `healthy` only when every mandatory gate passes and the final event chain is signed by the independent validator. AHIF 2.7.0 includes no completed observation.
