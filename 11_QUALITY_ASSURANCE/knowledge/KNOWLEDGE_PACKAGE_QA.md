# Knowledge Package Quality Assurance

## Mandatory gates

| Gate | Blocking condition |
|---|---|
| Schema | package or registry does not match the declared schema |
| Identifier | duplicate, malformed, or reused identifier |
| Provenance | unresolved canonical path or missing semantic anchor |
| Vocabulary | undefined condition, effect, domain, or lifecycle value |
| Identity | rule weakens or conflicts with canonical identity invariants |
| Semantics | structured record adds meaning absent from canonical sources |
| Registry | package path, version, status, or record count is inconsistent |
| Consumer safety | adapter hint authorizes semantic redesign or unsupported inference |

## Status model

- `pass` — all mandatory gates pass;
- `revise` — non-blocking metadata or clarity issue;
- `fail` — one or more blocking gates fail.

## Stable failure codes

- `AHIF-KNOW-001` — invalid package schema
- `AHIF-KNOW-002` — duplicate knowledge identifier
- `AHIF-KNOW-003` — unresolved provenance
- `AHIF-KNOW-004` — canonical semantic mismatch
- `AHIF-KNOW-005` — identity invariant conflict
- `AHIF-KNOW-006` — registry inconsistency
- `AHIF-KNOW-007` — unsupported lifecycle status
- `AHIF-KNOW-008` — unsafe consumer hint

## Release-candidate rule

Packages in version `2.0.0-rc1` remain `candidate`. They may participate in deterministic release-candidate evaluation but cannot be promoted to `active` until Sprint 011 cross-model validation and Sprint 012 stable-release review pass.
