# Variance and Tolerance Policy

## Purpose

Different image models produce different visual distributions. AHIF distinguishes acceptable model-native variance from semantic drift.

## Variance Categories

- `syntax_variance`: target-specific wording or parameter format.
- `control_variance`: different mechanisms for expressing the same intent.
- `rendering_variance`: texture, micro-detail, or aesthetic distribution differences.
- `declared_capability_loss`: unsupported non-critical control with an approved fallback.
- `semantic_drift`: changed canonical meaning; never acceptable.
- `identity_drift`: changed person or identity relationships; always blocking.

## Tolerance Rules

Allowed variance must:

- preserve every critical directive;
- preserve the same dominant scene and activity;
- remain within the capability profile;
- be declared in the adapter result;
- avoid new material visual decisions;
- remain reproducible from recorded inputs.

## Non-Tolerable Conditions

- generic-model substitution;
- demographic, age, or facial redesign;
- removal of identity reference;
- opposite or incompatible activity;
- climate-inappropriate styling;
- omitted blocking negative constraints;
- fabricated model capability;
- undeclared semantic loss.
