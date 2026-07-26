# Alternative Evaluation

## Purpose

Alternative evaluation prevents arbitrary selection and improves explainability.

## Candidate comparison dimensions

- identity risk
- contextual fit
- physical realism
- cultural fit
- character continuity
- photographic suitability
- story coherence
- implementation clarity

## Evaluation process

1. generate only contextually plausible candidates
2. eliminate candidates that violate identity invariants
3. score remaining candidates using the decision scorecard
4. evaluate cross-domain consequences
5. select the highest-priority coherent candidate
6. retain meaningful rejected alternatives with reasons

## Rejection reason vocabulary

- `identity-risk`
- `weather-mismatch`
- `activity-mismatch`
- `cultural-mismatch`
- `physics-mismatch`
- `character-mismatch`
- `camera-distortion-risk`
- `lighting-incoherence`
- `story-conflict`
- `insufficient-evidence`

## Tie handling

When alternatives are materially equivalent:

1. prefer the lower identity risk
2. prefer the more realistic human behavior
3. prefer the simpler coherent scene
4. prefer the option requiring fewer unsupported assumptions
5. record the tie and selected tie-break rule
