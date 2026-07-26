# QA Scorecard

Use the scoring model defined in `QA_SCORING_MODEL.md`.

| Category | Weight | Minimum |
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

A release requires aggregate score at least 90, every category minimum, all mandatory gates, and no blocking finding. Identity fidelity below 100 always blocks release.
