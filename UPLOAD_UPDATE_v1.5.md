# Upload Update — AHIF 1.5.0

## Release

Sprint 005 adds the Quality Assurance Engine.

## Recommended upload

Replace the repository contents with the full `AHIF-v1.5.0-quality-assurance-full.zip`, preserving the repository root. Use the Sprint 005 patch only when the target repository is exactly version 1.4.0.

## Verification

After upload, confirm:

- `VERSION.md` reports 1.5.0
- `manifest.json` reports `quality-assurance-hardening`
- `docs/sprints/SPRINT-005-QUALITY-ASSURANCE-ENGINE.md` exists
- QA engine, lint catalog, report schema, and QA regression files are present
- no previous files were removed
