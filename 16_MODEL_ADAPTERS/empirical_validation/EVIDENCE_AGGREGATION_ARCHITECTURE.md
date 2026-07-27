# Evidence Aggregation Architecture

## Purpose

Convert multiple accepted empirical evidence bundles into reproducible, auditable summaries without changing canonical identity or adapter support status.

## Pipeline

```text
Accepted Evidence Bundles
→ Eligibility Filter
→ Cohort Normalization
→ Metric Aggregation
→ Confidence Calculation
→ Drift and Outlier Audit
→ Target Profile Recommendation
→ Governance Review
```

## Invariants

- only evidence that passed empirical-evidence QA may enter aggregation;
- canonical master-photo authority is never replaced by generated outputs;
- aggregation never promotes an adapter automatically;
- every aggregate must retain source-bundle identifiers and provenance;
- missing or heterogeneous evidence must reduce confidence, not be silently imputed;
- model versions, adapter versions, scenario identifiers, and evaluation protocol versions remain explicit.

## Outputs

The pipeline emits an evidence aggregate, target-profile recommendation, and governance decision record. These artifacts are advisory until a human-approved adapter promotion report accepts them.
