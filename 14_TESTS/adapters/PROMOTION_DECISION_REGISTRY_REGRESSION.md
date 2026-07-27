# Promotion Decision Registry Regression

## Baseline assertions

- registry schema version is `1.0.0`;
- policy version is `2.5.0`;
- dossier count is zero;
- authorized count is zero;
- applied registry change count is zero;
- dossier array is empty;
- append-only events are enabled;
- no adapter support tier changes are implied.

## Mutation tests

1. Reject duplicate active scope fingerprints.
2. Reject non-monotonic event sequences.
3. Reject broken previous-event fingerprint chains.
4. Reject authorization without independent roles.
5. Reject applied-registry-change claims without a separate release record.
6. Preserve rejected, cancelled, blocked, and superseded dossiers.
7. Preserve adverse evidence and dissenting review events.
8. Recalculate counts deterministically from canonical entries.
