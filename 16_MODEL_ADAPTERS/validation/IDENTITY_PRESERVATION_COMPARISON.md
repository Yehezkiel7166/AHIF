# Identity Preservation Comparison

## Objective

Evaluate whether model-specific execution preserves the person represented by the canonical master photo.

## Required evidence

- canonical identity asset identifier and hash;
- generated output identifier and hash;
- exact target adapter and profile versions;
- scenario and prompt package identifiers;
- evaluator version and timestamp;
- angle, obstruction, lighting, expression, and stylization risk annotations.

## Comparison dimensions

| Dimension | Requirement |
|---|---|
| Face silhouette | Stable global facial outline under allowed pose variance |
| Eye system | Stable spacing, shape relationships, and gaze anatomy |
| Central proportions | Stable nose, midface, and eye-to-nose relationships |
| Lower face | Stable mouth, jaw, and chin relationships |
| Age presentation | No material age shift |
| Ethnicity presentation | No ethnicity drift or generic replacement |
| Recognizability | Same-person judgment remains unambiguous |

## Scoring

Each dimension uses `0.00–1.00`. The identity aggregate is the minimum mandatory dimension score, not the arithmetic mean.

Release-candidate thresholds:

- every mandatory dimension `>= 0.85`;
- recognizability `>= 0.90`;
- no critical drift finding;
- evidence quality at least `sufficient`.

## Evidence modes

- `human_review` — structured review by a named evaluator role;
- `approved_metric` — a documented metric approved by AHIF governance;
- `hybrid` — metric assistance plus human release decision.

Automated similarity alone cannot authorize stable support.

## Missing evidence

When image evidence is unavailable, report `empirical_pending`. Do not infer preservation from prompt or request text.
