# Upload Update — AHIF 1.7.0

## Release

Sprint 007 — Adapter Architecture Foundation

## Upload Options

### Full Repository

Use the full repository package to replace the repository working tree while preserving Git history in the target clone.

### Sprint Patch

Apply the patch only when the repository is exactly at AHIF 1.6.0.

## Required Verification

Confirm after upload:

- `VERSION.md` reports 1.7.0;
- `manifest.json` reports Sprint 007;
- `PROJECT_CONSTITUTION.md` is present;
- `16_MODEL_ADAPTERS/` contracts are present;
- no model-specific adapter is marked supported;
- no previous file was removed.
