# Reproducibility Protocol

## Objective

Provide sufficient evidence for a qualified reviewer to repeat the external execution or explain why exact repetition is impossible.

## Required controls

- immutable request checksum;
- adapter and capability-profile versions;
- complete parameter record;
- seed value or explicit non-deterministic seed policy;
- target runtime or service version when observable;
- execution date and region when material;
- output checksum;
- retry count;
- post-processing disclosure.

## Reproducibility levels

- `R0_unverifiable` — essential execution metadata is missing.
- `R1_documented` — request and environment are documented.
- `R2_repeatable_request` — request can be submitted again.
- `R3_repeated_semantics` — repeated executions preserve required semantics.
- `R4_repeated_identity` — repeated executions also meet identity thresholds.

## Promotion requirement

An adapter cannot be promoted beyond experimental status without at least `R3_repeated_semantics`. Production-certified identity fidelity requires `R4_repeated_identity` across the required scenario corpus.

## Non-deterministic services

When a target does not expose deterministic controls, reproducibility is measured through repeated semantic and identity outcomes, not pixel equality.
