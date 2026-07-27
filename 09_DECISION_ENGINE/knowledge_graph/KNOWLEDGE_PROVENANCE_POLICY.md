# Knowledge Provenance Policy

## Required provenance

Every structured knowledge record must resolve to one or more canonical repository sources. Provenance must include:

- repository-relative source path;
- source section or semantic anchor;
- extraction method;
- package version;
- review status;
- last semantic review date;
- optional supersession reference.

## Evidence classes

- `constitutional` — project constitution or identity invariant;
- `canonical-module` — AHIF domain documentation;
- `derived-rule` — deterministic derivation from multiple canonical modules;
- `adapter-capability` — immutable target capability snapshot;
- `test-fixture` — non-production regression evidence.

## Integrity rule

Structured records cannot introduce new domain claims that are absent from their canonical sources. Derived rules must list every source used and state the deterministic transformation.

## Consumer disclosure

Decision, reasoning, QA, and compatibility outputs should include the selected knowledge identifiers and source paths when audit detail is requested. They must not expose private reasoning traces.
