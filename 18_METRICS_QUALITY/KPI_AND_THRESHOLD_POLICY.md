# KPI and Threshold Policy

## Rules

1. A metric becomes a KPI only through a recorded decision purpose and accountable owner.
2. Thresholds must be versioned independently from observations.
3. Targets may not rewrite historical results.
4. Green status requires all mandatory data-quality gates to pass.
5. Empty populations resolve to `not-evaluated`, never automatic compliance.
6. Threshold breaches create review work; they do not directly mutate adapters or release state.
7. Composite scores must expose every component and weighting.
8. Quality gates must retain limiting dimensions instead of averaging them away.

## Threshold states

- `within-boundary`
- `attention-required`
- `breach`
- `not-evaluated`
- `invalid-source`

Thresholds are governance aids, not empirical certification.
