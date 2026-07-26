# Upload Update — v1.6.0

## Full repository

Upload the complete v1.6.0 repository when replacing an earlier local copy or when repository state is uncertain.

## Sprint patch

Apply the Sprint 006 patch only to an exact v1.5.0 repository. The patch contains every new or modified project file required for v1.6.0.

## Required verification

After upload, confirm:

- `VERSION.md` reports 1.6.0;
- `manifest.json` reports `SPRINT-006-FINAL-PROMPT-ORCHESTRATION`;
- `15_FINAL_PROMPT/` exists;
- the Sprint 006 documentation and final-prompt tests are present;
- no pre-existing repository file was removed.
