# Stable Release Contract Test

## Objective

Verify that AHIF 2.0 satisfies stable repository contracts without overstating external image-model evidence.

## Assertions

1. `VERSION.md`, `manifest.json`, `README.md`, and `CHANGELOG.md` identify version `2.0.0`.
2. `manifest.json` references only existing files.
3. all JSON files parse successfully;
4. stable knowledge and adapter identifiers remain unique;
5. canonical identity authority is unchanged;
6. support tiers distinguish contract validation from empirical validation;
7. adapter contracts require loss disclosure;
8. the release evidence register marks empirical image evidence as pending;
9. no document claims image-output parity;
10. Sprint 012 documentation and migration guidance are present.

## Expected result

All assertions pass before the stable archive is published.
