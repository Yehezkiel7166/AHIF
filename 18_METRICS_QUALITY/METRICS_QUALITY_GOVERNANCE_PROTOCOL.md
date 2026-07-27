# Metrics and Quality Governance Protocol

## Purpose

This protocol governs how AHIF defines, calculates, reviews, and publishes repository, adapter, and evidence-process metrics. It prevents attractive but misleading dashboards, denominator drift, target gaming, and unsupported quality claims.

## MQ0–MQ9 workflow

| Stage | Name | Required outcome |
|---|---|---|
| MQ0 | Metric request | Record decision purpose, owner, audience, and prohibited uses. |
| MQ1 | Definition resolution | Resolve the canonical metric identifier and active specification. |
| MQ2 | Source binding | Pin eligible source records, versions, time window, and exclusions. |
| MQ3 | Calculation plan | Declare formula, denominator, missing-data treatment, and precision. |
| MQ4 | Integrity checks | Check completeness, duplication, provenance, and source freshness. |
| MQ5 | Calculation | Produce deterministic values and an immutable calculation fingerprint. |
| MQ6 | Interpretation | Apply thresholds, confidence class, and limiting-dimension rules. |
| MQ7 | Independent review | Verify calculation, interpretation, and claim boundary. |
| MQ8 | Publication | Append a signed metric snapshot and dashboard manifest entry. |
| MQ9 | Retirement or supersession | Preserve history and identify the replacement specification. |

## Hard boundaries

Metrics governance does not automatically:

- create empirical evidence, audit findings, incidents, or telemetry;
- certify model output quality or production health;
- authorize adapter promotion, release, rollback, or tier mutation;
- treat missing data as success;
- combine incomparable cohorts or silently change denominators;
- permit a dashboard value to override source records.
