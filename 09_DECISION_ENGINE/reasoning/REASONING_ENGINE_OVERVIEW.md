# Reasoning Engine Overview

## Purpose

The AHIF Reasoning Engine converts resolved context and candidate decisions into an explainable, identity-safe reasoning record before prompt compilation.

It does not replace the Decision Engine. The Decision Engine proposes and resolves decisions; the Reasoning Engine verifies causal coherence, records evidence, compares alternatives, propagates confidence, and prepares a compiler-ready reasoning result.

## Position in the pipeline

```text
Knowledge Graph
→ Context Normalization
→ Decision Inference
→ Conflict Resolution
→ Reasoning Engine
→ Prompt Compiler
→ Quality Assurance
→ Final Prompt
```

## Core responsibilities

1. preserve canonical identity constraints as non-negotiable premises
2. connect each decision to contextual and knowledge evidence
3. test causal coherence across fashion, behavior, environment, camera, and story
4. expose rejected alternatives and the reason for rejection
5. propagate uncertainty without inventing facts
6. produce a deterministic reasoning result for the compiler

## Non-responsibilities

The Reasoning Engine must not:

- redesign the canonical face or body identity
- invent unsupported demographic attributes
- override identity invariants for aesthetics
- generate the final prose prompt
- conceal material uncertainty
- select randomly between incompatible alternatives

## Required reasoning domains

- identity preservation
- weather response
- activity suitability
- fashion and accessory suitability
- pose, gesture, and expression coherence
- environment interaction
- camera and lens suitability
- lighting and composition coherence
- story continuity

## Output contract

Every reasoning result must include:

- normalized premises
- identity invariants
- accepted decisions
- evidence links
- causal reasons
- rejected alternatives
- confidence values
- unresolved uncertainties
- compiler directives
- QA flags

The canonical machine-readable structure is defined in `10_PROMPT_COMPILER/schemas/REASONING_OUTPUT_SCHEMA.md`.
