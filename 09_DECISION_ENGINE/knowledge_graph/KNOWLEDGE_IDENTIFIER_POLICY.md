# Knowledge Identifier Policy

## Objective

Provide stable, auditable identifiers for reusable AHIF knowledge.

## Format

```text
AHIF-KG-<DOMAIN>-<FOUR_DIGIT_SEQUENCE>
```

Examples:

- `AHIF-KG-FASHION-0001`
- `AHIF-KG-TRAVEL-0001`
- `AHIF-KG-PHOTO-0001`

## Rules

1. Identifiers are globally unique within AHIF.
2. Published identifiers are never reused.
3. Semantic replacement creates a new identifier and deprecates the old record.
4. Deprecated records retain provenance and replacement references.
5. Package ordering does not define priority; the explicit `priority` field does.
6. Consumers must log identifiers used in a decision or compatibility report.
7. Human-readable labels may change without changing the identifier when semantics remain identical.

## Lifecycle states

- `draft` — not consumable outside validation fixtures;
- `candidate` — schema-valid and available for release-candidate evaluation;
- `active` — approved for stable inference;
- `deprecated` — retained for compatibility but not selected for new decisions;
- `blocked` — invalid or unsafe.

Version `2.0.0-rc1` publishes initial records as `candidate`. Stable promotion is deferred to the `2.0.0` release gate.
