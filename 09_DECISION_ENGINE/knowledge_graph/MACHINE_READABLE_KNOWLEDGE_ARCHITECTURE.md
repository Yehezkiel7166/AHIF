# Machine-Readable Knowledge Architecture

## Purpose

AHIF knowledge must be usable by humans, decision services, reasoning services, prompt compilation, QA, and model adapters without creating parallel sources of truth. Version `2.0.0-rc1` introduces structured knowledge packages that encode selected canonical rules in deterministic, versioned, machine-readable form.

## Authority model

The canonical Markdown modules remain the normative source for domain meaning. Structured packages are executable representations derived from those modules. Every record must include provenance that resolves to a repository path and a stable knowledge identifier.

A package must never silently override its canonical source. When a conflict is detected, validation fails and the Markdown source remains authoritative.

## Processing sequence

```text
Canonical domain module
→ package extraction
→ identifier assignment
→ provenance binding
→ schema validation
→ semantic validation
→ registry publication
→ Decision Engine consumption
→ Reasoning evidence
→ Adapter capability consumption
```

## Knowledge package requirements

Every package must declare:

- package identifier;
- package version;
- lifecycle status;
- domain;
- canonical source paths;
- schema version;
- records with stable identifiers;
- machine-readable conditions and effects;
- priority and confidence policy;
- provenance metadata;
- validation state.

## Stable identifiers

Knowledge identifiers use this form:

```text
AHIF-KG-<DOMAIN>-<NUMBER>
```

Initial domain codes:

- `IDENTITY`
- `HUMAN`
- `FASHION`
- `TRAVEL`
- `PHOTO`
- `STORY`
- `ADAPTER`

Identifiers are immutable after publication. A changed meaning requires a new identifier. Editorial corrections that do not change semantics may retain the identifier and increment the package patch version.

## Record model

A knowledge record contains:

- `id`
- `label`
- `domain`
- `type`
- `status`
- `conditions`
- `effects`
- `constraints`
- `priority`
- `confidence`
- `provenance`
- `consumer_hints`

Records describe reusable decision evidence. They do not contain hidden chain-of-thought, model-specific prompt syntax, or unsupported factual claims.

## Consumer rules

The Decision Engine may select a record only when its conditions are satisfied and no higher-priority invariant blocks it. The Reasoning Engine must cite the record identifier as evidence. The Prompt Compiler receives only accepted directives, not raw package records. Model adapters may consume `consumer_hints.adapter_capabilities` but may not reinterpret identity or semantic meaning.

## Failure behavior

A package is blocked when:

- its schema is invalid;
- a knowledge identifier is duplicated;
- provenance cannot be resolved;
- a condition or effect uses an undefined vocabulary term;
- a record conflicts with canonical identity rules;
- lifecycle status is unsupported;
- declared package checksum or version metadata is inconsistent.

Blocked packages must not enter inference, reasoning, compilation, QA, or adapter execution.
