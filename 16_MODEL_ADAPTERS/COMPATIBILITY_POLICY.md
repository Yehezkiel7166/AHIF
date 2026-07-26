# Multi-Model Compatibility Policy

## Canonical Meaning

The canonical Final Prompt Package is model neutral. Compatibility is measured by preserved meaning, not by identical text.

## Preservation Order

1. Canonical identity directives
2. Blocking negative constraints
3. Human plausibility and anatomy
4. Context and activity coherence
5. Camera, lighting, and composition intent
6. Story and aesthetic detail

## Loss Policy

Every lossy transformation must include:

- source directive identifier;
- affected semantic domain;
- reason for loss;
- criticality;
- approved fallback, when available;
- resulting release effect.

Silent omission is prohibited.

## Compatibility Result

An adapter result is:

- `compatible` when mandatory semantics are preserved;
- `compatible_with_degradation` when only declared non-critical loss exists;
- `incompatible` when mandatory semantics cannot be preserved;
- `blocked` when execution is not permitted.

## Cross-Model Consistency

Different adapters may use different syntax, but they must preserve the same canonical identity, scene decisions, and reasoning outcome within declared capability limits.
