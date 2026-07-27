# Evidence Ingestion Contract Test

## Test matrix

1. Valid complete request with verified artifacts returns `accepted`.
2. Valid request with external, unavailable output bytes returns `quarantined`.
3. Digest mismatch returns `rejected` and `AHIF-ING-003`.
4. Absolute or traversal path returns `rejected` and `AHIF-ING-002`.
5. Existing exact fingerprint returns `duplicate` and `AHIF-ING-006`.
6. Missing identity evaluation link returns `quarantined`.
7. Any request to promote an adapter during ingestion returns `rejected`.
8. Repeated execution against the same inputs produces the same decision and failure codes.

## Permanent assertions

- canonical identity authority never changes;
- generated outputs are observations only;
- registry writes are append-only;
- ingestion cannot change adapter status.