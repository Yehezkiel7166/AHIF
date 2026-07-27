# Upload Update — AHIF 2.0.0-rc2

## Release

Sprint 011 — Cross-Model Validation

## Apply one package only

- Use the full repository package to replace the complete repository content.
- Use the Sprint 011 patch only when the repository is exactly at `2.0.0-rc1`.
- Do not apply both packages.

## Post-upload verification

Confirm:

- `VERSION.md` reports `2.0.0-rc2`;
- `manifest.json` reports Sprint 011;
- validation architecture and schemas resolve;
- both JSON fixtures parse;
- no previous file was removed;
- adapters remain `experimental` and empirical evidence remains `pending`.
