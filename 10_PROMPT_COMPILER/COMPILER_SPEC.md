# Prompt Compiler Specification

## Responsibility

The Prompt Compiler converts a validated reasoning result into a coherent, model-neutral image-generation prompt. It is a deterministic expression layer, not a decision-making layer.

## Required input

- status: `compiler-ready`
- valid `REASONING_OUTPUT_SCHEMA.md`
- canonical identity confidence at or above the required floor
- accepted reasoning chains with compiler directives
- no unresolved material uncertainty

## Canonical process

```text
Reasoning Output
→ Input Validation
→ Directive Normalization
→ Section Planning
→ Dependency Ordering
→ Redundancy Control
→ Contradiction Gate
→ Natural-Language Rendering
→ Negative Constraint Synthesis
→ Metadata Emission
→ Compiler QA Handoff
```

## Canonical output order

1. identity lock
2. scene anchor
3. subject action
4. body language, gesture, eye focus, and expression
5. outfit, footwear, hair, makeup, and accessories
6. environmental interaction
7. camera, lens, viewpoint, composition, and depth
8. lighting and color
9. realism controls
10. negative constraints

## Output

A package conforming to `schemas/COMPILED_PROMPT_SCHEMA.md`.

## Non-negotiable rules

- produce one coherent scene, not disconnected keywords
- introduce no unsupported material fact
- preserve explicit user constraints unless they violate higher priorities
- never compile blocked or revision-required reasoning
- never hide contradictions through ambiguous language
- preserve identity protection before aesthetics
- retain traceability outside visible prompt text
