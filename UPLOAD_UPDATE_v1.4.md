# Upload Update — Version 1.4.0

## Recommended method

Replace the repository contents with the full `AHIF-v1.4.0` package while preserving the `.git` directory in the local clone, then review, commit, and push.

## Patch method

Apply the Sprint 004 patch only when the target repository is exactly version `1.3.0` and contains Sprint 003 without local divergence.

## Verification

Confirm:

- `VERSION.md` reports `1.4.0`
- `manifest.json` reports `1.4.0`
- latest sprint is `SPRINT-004-PROMPT-COMPILER`
- `ROADMAP.md` marks version 1.4 complete
- `10_PROMPT_COMPILER/COMPILER_PIPELINE.md` exists
- `14_TESTS/compiler/COMPILER_CONTRACT_TEST.md` exists
