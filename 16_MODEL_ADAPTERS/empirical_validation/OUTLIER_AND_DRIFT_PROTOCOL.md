# Outlier and Drift Protocol

## Outlier checks

Flag runs with identity score deviation, semantic score deviation, evaluator disagreement, hash mismatch, or unusual parameter mutation beyond configured tolerance.

## Drift checks

Compare cohorts across adapter version, model version, time window, and scenario class. Drift is material when a critical dimension crosses a governance threshold or when the confidence class decreases.

## Required response

- preserve the original evidence;
- record the detection rule;
- isolate affected cohorts;
- prohibit silent deletion;
- route material identity drift to adapter downgrade review;
- require new evidence before restoring confidence.
