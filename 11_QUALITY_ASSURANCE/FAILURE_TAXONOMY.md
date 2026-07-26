# QA Failure Taxonomy

## Severity levels

| Severity | Definition | Required action |
|---|---|---|
| critical | Canonical identity, safety, or trusted-output boundary is violated. | reject |
| error | A mandatory contract or realism rule is violated. | repair or reject |
| warning | Coherence or quality is materially reduced but recoverable. | revise |
| info | Non-blocking refinement opportunity. | optional |

## Failure families

### Identity

- `ID-LOCK-MISSING`
- `ID-DRIFT-RISK`
- `ID-AGE-DRIFT`
- `ID-ETHNICITY-DRIFT`
- `ID-FACE-REDESIGN`
- `ID-VISIBILITY-INSUFFICIENT`

### Human realism

- `HR-ANATOMY-INVALID`
- `HR-BALANCE-INVALID`
- `HR-GRIP-INVALID`
- `HR-CONTACT-INVALID`
- `HR-FABRIC-PHYSICS-INVALID`

### Context and culture

- `CX-WEATHER-CONFLICT`
- `CX-TIME-CONFLICT`
- `CX-ACTIVITY-CONFLICT`
- `CX-CULTURAL-INACCURACY`
- `CX-LOCATION-INACCURACY`

### Photography and lighting

- `PH-LENS-DISTORTION-RISK`
- `PH-CAMERA-IMPOSSIBLE`
- `PH-LIGHTING-CONFLICT`
- `PH-SHADOW-CONFLICT`
- `PH-COMPOSITION-CONFLICT`

### Compiler integrity

- `CP-UNSUPPORTED-DIRECTIVE`
- `CP-UNRESOLVED-CONTRADICTION`
- `CP-DUPLICATE-DIRECTIVE`
- `CP-SECTION-ORDER-INVALID`
- `CP-METADATA-INCOMPLETE`

### Output contract

- `OUT-PROMPT-MISSING`
- `OUT-NEGATIVE-MISSING`
- `OUT-QA-REPORT-MISSING`
- `OUT-ADAPTER-SYNTAX-PREMATURE`

## Stability rule

Failure codes are public repository contracts. Their meaning may be clarified but must not be silently changed.
