# Confidence Propagation

## Purpose

Confidence expresses how strongly a reasoning result is supported. It is not an aesthetic score.

## Domain confidence

Each reasoning domain reports a value from `0.00` to `1.00`:

- identity
- context
- weather
- activity
- fashion
- behavior
- photography
- story

## Aggregate confidence

Aggregate confidence is constrained by the weakest material dependency. High confidence in camera selection cannot compensate for low confidence in identity preservation.

Recommended calculation:

```text
aggregate = weighted_mean(domain_confidence)
aggregate = min(aggregate, identity_confidence + 0.10)
aggregate = min(aggregate, lowest_material_dependency + 0.15)
```

Values are bounded to `0.00–1.00`.

## Thresholds

| Range | Interpretation | Action |
|---|---|---|
| `0.85–1.00` | strongly supported | compile normally |
| `0.70–0.84` | supported with limited uncertainty | compile and retain uncertainty notes |
| `0.50–0.69` | materially uncertain | revise or request missing input |
| below `0.50` | insufficient support | block final compilation |

## Identity floor

Identity confidence below `0.85` is always a blocking condition for identity-sensitive image generation.
