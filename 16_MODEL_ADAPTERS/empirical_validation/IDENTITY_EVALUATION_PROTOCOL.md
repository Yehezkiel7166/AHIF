# Identity Evaluation Protocol

## Goal

Evaluate whether a generated output preserves the canonical human identity under the requested context.

## Mandatory dimensions

- facial geometry continuity;
- eye shape and spacing;
- nose and mouth structure;
- apparent age continuity;
- ethnicity continuity;
- skin-tone continuity within lighting tolerance;
- characteristic feature continuity;
- body-proportion plausibility;
- absence of generic-model substitution.

## Rating scale

Each dimension uses:

- `pass` — consistent within declared tolerance;
- `warning` — uncertain or minor deviation;
- `fail` — material identity drift;
- `not_assessable` — evidence does not permit assessment.

## Blocking rules

The result is blocked when:

- generic-model substitution is observed;
- ethnicity or age materially drifts;
- facial structure is redesigned;
- the canonical reference is missing or checksum-mismatched;
- more than two mandatory dimensions are `not_assessable`;
- any critical dimension is `fail`.

## Evaluator independence

Promotion evidence requires at least two independent evaluation records. Automated similarity scores may assist but cannot replace structured human review unless a future validated evaluator profile is explicitly approved.

## Output

The evaluator emits an Identity Evaluation Report conforming to the repository schema and linked to one immutable evidence bundle.
