# Upload Update — AHIF 2.0.0-rc1

## Release

Sprint 010 introduces Machine-Readable Knowledge Expansion.

## Upload method

Use either the full repository archive or the Sprint 010 patch. Do not apply both.

## Verification

After upload, verify:

- `VERSION.md` reports `2.0.0-rc1`;
- `manifest.json` reports Sprint 010;
- `09_DECISION_ENGINE/knowledge_graph/KNOWLEDGE_REGISTRY.json` exists;
- all three initial package JSON files exist;
- no existing repository file was removed.
