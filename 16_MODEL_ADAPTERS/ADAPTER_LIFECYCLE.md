# Adapter Lifecycle

## States

```text
registered
→ resolved
→ assessed
→ planned
→ serialized
→ validated
→ released | degraded | blocked
```

## State Contracts

### Registered

A stable adapter ID, adapter version, target family, and capability profile are available.

### Resolved

The target adapter and exact capability profile version are selected.

### Assessed

Every canonical requirement has a compatibility classification.

### Planned

All transformations, degradations, omissions, and parameter mappings are declared before serialization.

### Serialized

The target request is generated from the approved plan.

### Validated

Conformance checks confirm semantic preservation and trace completeness.

### Released

No blocking finding exists and no undeclared loss occurred.

### Degraded

The request remains usable but contains declared, non-identity-critical degradation.

### Blocked

The adapter cannot preserve mandatory semantics or the source package is ineligible.

## Transition Rules

- State transitions are forward-only within one execution.
- A blocked state is terminal.
- Degradation must be explicit and must include affected directives.
- Identity-critical degradation is always blocking.
- Adapter retries may change configuration but may not alter canonical decisions.
