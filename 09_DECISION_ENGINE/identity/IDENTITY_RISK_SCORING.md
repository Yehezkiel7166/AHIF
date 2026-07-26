# Identity Risk Scoring

Score each factor from 0 to 2.

| Factor | 0 | 1 | 2 |
|---|---|---|---|
| Face angle | frontal | moderate | extreme |
| Facial obstruction | none | partial | major |
| Lighting | clear | challenging | identity-obscuring |
| Makeup | natural | strong | transformative |
| Expression | mild | strong | distorting |
| Lens | moderate | mildly risky | extreme |
| Stylization | low | medium | high |
| Motion | still | moderate | heavy blur |

## Interpretation

- 0–4: low risk
- 5–9: medium risk
- 10–16: high risk

High-risk prompts must simplify at least two risk factors before generation.
