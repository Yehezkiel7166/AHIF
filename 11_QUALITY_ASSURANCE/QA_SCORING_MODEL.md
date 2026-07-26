# QA Scoring Model

## Principle

Scoring summarizes quality after mandatory gates. Scores do not override critical or error findings.

## Categories

| Category | Weight | Minimum release score |
|---|---:|---:|
| Identity fidelity | 25 | 100 |
| Human anatomy and physics | 20 | 90 |
| Context and environmental truth | 15 | 85 |
| Cultural appropriateness | 10 | 90 |
| Camera, composition, and lighting | 10 | 85 |
| Styling and character continuity | 8 | 80 |
| Story coherence | 5 | 80 |
| Compiler integrity | 5 | 90 |
| Output completeness | 2 | 100 |

## Aggregate score

```text
aggregate = Σ(category_score × category_weight) / 100
```

Release targets:

- `pass`: aggregate at least 90, all category minimums met, no blocking finding
- `revise`: aggregate 75–89 or a repairable blocking finding exists
- `fail`: aggregate below 75 or any unrecoverable critical/error finding exists

## Identity override

Identity fidelity must be 100 for release. A lower identity score always blocks output regardless of aggregate score.

## Evidence requirement

Each category score must reference concrete checks. Unsupported scores are invalid and trigger `CP-METADATA-INCOMPLETE`.
