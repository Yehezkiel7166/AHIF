# Adapter Promotion Dossier Contract Test

## Test matrix

1. Completed evaluations with pinned policies create a deterministic draft dossier.
2. Missing adapter version or requested tier returns `AHIF-PROMO-002`.
3. Incomplete evaluation job returns `needs_revision` with `AHIF-PROMO-003`.
4. Ineligible aggregate returns `blocked` with `AHIF-PROMO-004`.
5. Undisclosed missing scenario coverage returns `AHIF-PROMO-005`.
6. Omitted adverse evidence or unresolved drift returns `AHIF-PROMO-006`.
7. Same role performing required independent reviews returns `AHIF-PROMO-007`.
8. Invalid direct `draft → authorized` transition returns `AHIF-PROMO-008`.
9. Promotion recommendation above evidence threshold returns `AHIF-PROMO-009`.
10. Any adapter registry mutation during dossier review returns `AHIF-PROMO-010`.
11. Duplicate active scope fingerprint returns `AHIF-PROMO-011`.
12. Stale policy or evidence cutoff returns `AHIF-PROMO-012`.
13. Identical pinned inputs and review decisions resolve to the same recommendation and failure codes.

## Permanent assertions

- canonical identity authority never changes;
- generated outputs remain observations;
- adverse evidence remains visible;
- dossier and event records are append-only;
- authorization and registry mutation remain separate;
- baseline remains zero-evidence, zero-job, and zero-dossier.
