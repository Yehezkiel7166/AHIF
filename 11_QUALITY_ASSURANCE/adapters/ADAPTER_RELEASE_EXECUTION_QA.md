# Adapter Release Execution QA

## Mandatory gates

1. release plan and scope fingerprint are valid;
2. source dossier is authorized, current, and recommends promote or downgrade;
3. exact adapter, from-tier, to-tier, registry, policy, profile, and contract versions are pinned;
4. pre-change snapshot and package manifest are complete and immutable;
5. declared mutation set is minimal and contains no unrelated path;
6. candidate contract, compatibility, regression, and claim-boundary tests pass;
7. release owner, approver, validator, and rollback roles satisfy separation rules;
8. rollback procedure is complete, deterministic, and executable;
9. state transitions and append-only event chain are valid;
10. post-change snapshot exactly matches declared mutations and authorized tier;
11. README, VERSION, CHANGELOG, ROADMAP, manifest, AI context, and release record agree;
12. no empirical or production-support claim exceeds the authorized evidence.

## Failure codes

| Code | Meaning | Default outcome |
|---|---|---|
| `AHIF-REL-001` | release plan or scope fingerprint invalid | blocked |
| `AHIF-REL-002` | authorization missing, stale, rejected, or superseded | blocked |
| `AHIF-REL-003` | adapter or governed version not pinned | blocked |
| `AHIF-REL-004` | pre-change snapshot incomplete or mismatched | blocked |
| `AHIF-REL-005` | package manifest missing or contains undeclared mutation | blocked |
| `AHIF-REL-006` | candidate validation failed | needs_revision |
| `AHIF-REL-007` | role separation conflict | needs_revision |
| `AHIF-REL-008` | rollback plan unavailable or non-reproducible | blocked |
| `AHIF-REL-009` | invalid state transition or event chain | blocked |
| `AHIF-REL-010` | post-change snapshot or tier mismatched | rollback_required |
| `AHIF-REL-011` | documentation or manifest state inconsistent | needs_revision |
| `AHIF-REL-012` | duplicate active release scope | cancelled |
| `AHIF-REL-013` | support claim exceeds evidence or authorization | blocked |
| `AHIF-REL-014` | canonical identity or unrelated stable contract changed | rollback_required |

## Completion gate

A release may become `completed` only when every mandatory gate passes, the final event chain is valid, and the post-change snapshot is signed by the validator. AHIF 2.6.0 includes no completed release.
