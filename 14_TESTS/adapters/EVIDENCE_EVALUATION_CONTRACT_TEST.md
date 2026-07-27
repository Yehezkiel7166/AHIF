# Evidence Evaluation Contract Test

## Test matrix

1. Accepted record with complete pinned scope creates a deterministic `queued` job.
2. Missing or quarantined registry record returns `blocked` with `AHIF-EVAL-002`.
3. Artifact fingerprint mismatch returns `blocked` with `AHIF-EVAL-003`.
4. Missing adapter or protocol version returns `blocked` with `AHIF-EVAL-004`.
5. Existing identical scope fingerprint returns duplicate handling with `AHIF-EVAL-005`.
6. Direct `queued → completed` transition returns `AHIF-EVAL-006`.
7. Missing requested report returns `needs_revision` with `AHIF-EVAL-007`.
8. Same actor performing required independent review returns `AHIF-EVAL-008`.
9. Non-monotonic event sequence returns `AHIF-EVAL-009`.
10. Any adapter status mutation returns `blocked` with `AHIF-EVAL-010`.
11. Repeated resolution of identical inputs produces the same state and failure codes.

## Permanent assertions

- canonical identity authority never changes;
- generated outputs remain observations;
- queue events are append-only;
- evaluation cannot promote an adapter;
- repository baseline remains zero-evidence and zero-job.