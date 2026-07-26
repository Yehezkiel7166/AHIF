# Evidence and Provenance

## Objective

Every material reasoning conclusion must be traceable to its origin.

## Evidence classes

1. **Canonical identity evidence** — master photo and identity protocols
2. **User evidence** — explicit request fields
3. **Knowledge evidence** — graph nodes, relationships, and domain rules
4. **Derived evidence** — normalized or inferred facts supported by prior evidence
5. **Constraint evidence** — architecture, constitution, safety, and QA requirements

## Provenance record

Each accepted decision should record:

- decision identifier
- evidence class
- source file or graph identifier
- evidence statement
- derivation rule
- confidence

## Evidence priority

```text
Canonical identity
> Explicit user instruction
> Safety and cultural constraints
> Verified contextual knowledge
> Character continuity
> Visual preference
```

An explicit request cannot override canonical identity or safety constraints.

## Unsupported evidence

When evidence is absent:

- omit nonessential detail
- choose a neutral, low-risk default defined by policy
- expose the uncertainty
- block compilation when the missing fact is identity-critical

The engine must never fabricate provenance.
