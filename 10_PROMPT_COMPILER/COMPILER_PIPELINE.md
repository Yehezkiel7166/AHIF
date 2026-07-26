# Prompt Compiler Pipeline

## Purpose

The Prompt Compiler transforms a validated `compiler-ready` reasoning record into one coherent image-generation prompt without introducing new material decisions.

## Pipeline stages

1. **Input validation** — verify schema version, status, identity confidence, evidence links, and required compiler directives.
2. **Directive normalization** — convert accepted directives into normalized compiler units while preserving provenance.
3. **Section planning** — allocate every unit to one canonical prompt section.
4. **Dependency ordering** — resolve identity, scene, human action, styling, environment, photography, realism, and exclusions in deterministic order.
5. **Semantic consolidation** — merge equivalent instructions and preserve the strongest non-conflicting formulation.
6. **Contradiction gate** — stop compilation when two accepted directives cannot coexist.
7. **Natural-language rendering** — serialize the plan into readable visual instructions rather than keyword fragments.
8. **Negative constraint synthesis** — select only constraints relevant to identified risks and known failure modes.
9. **Metadata emission** — return traceable compiler metadata beside the prompt.
10. **Compiler QA handoff** — submit the compiled artifact to the Quality Assurance layer.

## Invariants

- canonical identity directives are first and non-negotiable
- each material statement must map to an accepted reasoning directive
- one dominant activity and one dominant story beat are allowed
- the compiler cannot resolve missing evidence by invention
- blocked or revision-required reasoning records cannot produce a final prompt
- deterministic input must produce semantically equivalent output

## Result states

- `compiled` — a complete prompt and metadata package is available
- `revision-required` — recoverable input, dependency, or contradiction issue
- `blocked` — identity safety, schema integrity, or unsupported-fact failure
