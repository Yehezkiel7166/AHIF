# Upload Update — AHIF 2.6.0

## Release

- Version: 2.6.0
- Sprint: 018
- Type: backward-compatible framework expansion

## Upload scope

Upload the complete repository to replace the previous working copy, or apply the Sprint 018 patch while preserving all existing files.

## New capabilities

- governed R0–R9 adapter release execution workflow;
- immutable release package and before/after snapshot contracts;
- approval and role-separation gates;
- deterministic rollback requirements;
- append-only release execution registry;
- release QA and regression contracts.

## Important boundary

This release does not authorize or execute any real adapter change. Evidence, evaluation, promotion, and release registries remain empty. Existing adapter support tiers remain unchanged.

## Verification

After upload, verify:

1. `VERSION.md` reports 2.6.0;
2. `manifest.json` parses and reports 2.6.0;
3. `docs/sprints/SPRINT-018-ADAPTER-RELEASE-EXECUTION-GOVERNANCE.md` exists;
4. `16_MODEL_ADAPTERS/release_execution/registry/RELEASE_EXECUTION_REGISTRY.json` contains zero records;
5. no existing file was removed;
6. all JSON files parse and local Markdown links resolve.
