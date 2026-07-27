# Metrics and Quality Governance Contract Test

A conforming implementation must demonstrate that:

1. MQ0–MQ9 stages are ordered and state transitions are recorded;
2. metric definitions contain explicit numerator and denominator rules;
3. empty populations produce `not-evaluated`, not zero or pass;
4. source records and fingerprints are pinned;
5. duplicate, excluded, blocked, and missing records remain disclosed;
6. threshold versions are independent from observations;
7. composite metrics expose components and weights;
8. snapshots are reproducible and append-only;
9. dashboard panels link to signed snapshots;
10. publication cannot mutate adapters, releases, incidents, audits, or empirical evidence.

Baseline expectation for AHIF 2.10.0: zero registered specifications, zero snapshots, and zero dashboards.
