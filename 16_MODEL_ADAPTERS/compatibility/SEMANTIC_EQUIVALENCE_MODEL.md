# Semantic Equivalence Model

## Semantic Domains

AHIF compares adapter results across the following domains:

| Domain | Criticality | Required comparison |
|---|---:|---|
| Identity binding | Critical | exact source reference and invariant retention |
| Identity description | Critical | no weakening, replacement, or demographic drift |
| Scene anchor | Required | same location and environmental context |
| Activity | Required | same primary action and intent |
| Human behavior | Required | equivalent pose, gesture, gaze, and expression intent |
| Styling | Required | equivalent climate, culture, and activity response |
| Camera | Quality | equivalent framing and perspective intent |
| Lighting and color | Quality | equivalent physical and narrative lighting intent |
| Realism | Critical | anatomy, physics, contact, and compositing controls retained |
| Negative constraints | Critical | all blocking constraints retained or safely translated |
| Story | Required | same dominant story beat |

## Equivalence Record

Each domain comparison records:

- canonical directive identifiers;
- adapter evidence paths;
- preservation status;
- variance type;
- loss identifier, when applicable;
- fallback identifier, when applicable;
- confidence;
- release effect.

## Allowed Variance

Allowed variance includes target-native syntax, parameter naming, sampler implementation, quality controls, and rendering style that does not alter canonical meaning.

## Prohibited Variance

Prohibited variance includes identity weakening, changed activity, incompatible weather response, omitted blocking negatives, invented props, altered story, or target-specific beautification that redesigns the person.

## Confidence Floor

- Identity domains: `>= 0.95`
- Critical realism domains: `>= 0.90`
- Required semantic domains: `>= 0.85`
- Quality domains: `>= 0.75`

Any identity-domain result below the floor is `blocked`.
