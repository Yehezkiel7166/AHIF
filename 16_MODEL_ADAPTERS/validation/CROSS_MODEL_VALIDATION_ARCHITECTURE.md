# Cross-Model Validation Architecture

## Purpose

Define the release-candidate validation layer that evaluates whether every registered adapter preserves the same canonical AHIF intent across target models without treating any target as the semantic authority.

## Authority order

1. Canonical master photo and identity invariants
2. Release-eligible Final Prompt Package
3. Canonical Markdown knowledge modules
4. Validated machine-readable knowledge packages
5. Adapter transformation plan
6. Target request
7. Generated-output evidence, when available

A downstream artifact cannot override an upstream authority.

## Validation planes

### Contract plane

Validates schemas, package binding, adapter version binding, capability snapshots, deterministic serialization, parameter legality, loss disclosure, and blocking behavior.

### Semantic plane

Compares required identity, scene, activity, styling, realism, camera, lighting, and negative-constraint semantics against the canonical package.

### Empirical plane

Evaluates generated-image evidence against the canonical master photo and scenario requirements. Empirical evidence is optional for contract execution but mandatory for stable production support.

## Validation states

- `not_run` — no evidence exists;
- `contract_validated` — request-level contracts pass;
- `empirical_partial` — image evidence exists but coverage is incomplete;
- `empirical_validated` — required image evidence and thresholds pass;
- `blocked` — a mandatory gate fails;
- `expired` — evidence references an obsolete adapter or capability profile.

## Identity-first release rule

Identity is non-compensatory. No aggregate score can offset a failed identity gate. Any identity-critical omission, unsupported reference path, or material face drift blocks release.

## Output

Every run emits a versioned Cross-Model Validation Report with exact package, adapter, profile, serializer, knowledge registry, test corpus, and evidence identifiers.
