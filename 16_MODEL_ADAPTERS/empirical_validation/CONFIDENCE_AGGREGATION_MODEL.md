# Confidence Aggregation Model

## Dimensions

- identity preservation;
- semantic preservation;
- reproducibility;
- scenario coverage;
- model-version coverage;
- evaluator agreement;
- evidence integrity.

## Calculation principles

Each dimension is normalized to `[0,1]`. The aggregate confidence is a conservative weighted result bounded by the weakest critical dimension. Critical identity failures force confidence to zero for promotion purposes.

## Confidence classes

| Class | Range | Meaning |
|---|---:|---|
| C0 | 0.00–0.39 | insufficient |
| C1 | 0.40–0.59 | exploratory |
| C2 | 0.60–0.74 | provisional |
| C3 | 0.75–0.89 | strong |
| C4 | 0.90–1.00 | high confidence |

A class is descriptive evidence, not an adapter support tier.
