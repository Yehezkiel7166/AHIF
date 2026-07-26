# Model Adapter Architecture

## Purpose

The Model Adapter Layer translates a released, model-neutral `Final Prompt Package` into a target-model request while preserving AHIF decisions, identity constraints, QA status, and provenance.

The adapter boundary begins only after Final Prompt release eligibility is established.

## Pipeline Position

```text
Final Prompt Package
→ Capability Resolution
→ Compatibility Assessment
→ Transformation Plan
→ Model Request Serialization
→ Adapter Conformance Validation
```

## Responsibilities

The adapter layer shall:

- resolve a declared target model profile;
- identify supported, degraded, emulated, and unsupported features;
- preserve mandatory identity directives;
- translate canonical prompt sections into model-specific syntax;
- map negative constraints only where supported;
- expose every lossy transformation;
- produce a machine-readable adapter result;
- fail closed when identity-critical meaning cannot be preserved.

## Non-Responsibilities

The adapter layer shall not:

- infer fashion, pose, camera, environment, or story decisions;
- repair upstream reasoning;
- rewrite canonical identity attributes;
- bypass QA release state;
- silently drop unsupported constraints.

## Core Components

### Adapter Registry

Maps stable adapter identifiers to versioned capability profiles and serialization contracts.

### Capability Resolver

Compares the canonical package requirements with target-model capabilities.

### Compatibility Assessor

Classifies each canonical directive as:

- `native`;
- `translated`;
- `degraded`;
- `unsupported`;
- `blocked`.

### Transformation Planner

Creates an ordered, auditable plan before serialization.

### Serializer

Produces the target request representation without changing the decision meaning.

### Conformance Validator

Checks identity preservation, required-field retention, declared capability use, and transformation trace completeness.

## Determinism

For the same final prompt package, adapter profile version, and adapter configuration, the transformation plan and serialized semantic content must be reproducible.

## Failure Policy

An adapter must return `blocked` when:

- the source package is not release eligible;
- the target model cannot preserve an identity-critical directive;
- a required capability is unsupported and no approved degradation exists;
- the transformation would contradict the canonical package;
- provenance cannot be retained.
