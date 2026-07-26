# Explainable Result Summary

## Objective

The explainable result summary communicates why the released prompt was assembled without exposing internal chain-of-thought. It reports structured decisions, evidence classes, rejected alternatives, confidence, and validation outcomes.

## Required sections

### Identity

- canonical reference status;
- preserved invariants;
- identity risk level;
- identity recovery actions, if any.

### Context interpretation

- normalized location, place, time, season, weather, and atmosphere;
- explicit assumptions;
- unresolved optional inputs.

### Selected visual decisions

For fashion, hair, makeup, accessories, pose, gesture, expression, activity, environment interaction, camera, lens, lighting, composition, color, and story:

- selected directive;
- evidence category;
- confidence band;
- concise rationale;
- material rejected alternative when relevant.

### Validation

- mandatory gate outcomes;
- aggregate score;
- warning codes;
- recovery history;
- release eligibility.

## Prohibited content

The summary must not include hidden reasoning tokens, speculative personal attributes, unsupported demographic conclusions, or implementation secrets unrelated to the output contract.
