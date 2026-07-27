# Evidence Registry Regression

## Baseline assertions

- registry JSON parses successfully;
- `append_only` is true;
- `record_count` equals `records.length`;
- all record IDs are unique;
- all bundle and execution IDs are present;
- all SHA-256 fingerprints use 64 lowercase hexadecimal characters;
- supersession links cannot form cycles;
- no record marks a generated output as canonical identity;
- no registry event directly promotes an adapter.

## Zero-evidence baseline

The repository baseline contains zero records. This is an intentional truthful state, not a test failure.