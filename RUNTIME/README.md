# AHIF Runtime Execution Layer

`RUNTIME.engine.execute_framework()` is the single canonical executable path for AHIF 3.4.0. It executes context normalization, identity locking, registered knowledge loading, priority-ordered decision selection, explainable reasoning handoff, prompt compilation, mandatory QA, final prompt packaging, and adapter preparation in that order.

The runtime is dependency-free and deterministic. Callers may supply `execution_timestamp`; when absent, the stable epoch value is used so identical inputs produce identical structured results. Execution identifiers are SHA-256-derived from canonical input JSON. Trace summaries contain field metadata rather than private chain-of-thought.

The adapter stage prepares a request under the existing adapter registry contract. It does not contact or execute a model. Runtime conformance is not empirical model validation, production readiness, release eligibility, or an LTS designation.

## Contract

Each stage accepts a mapping and returns `StageResult`, containing an output mapping, one of `pass`, `warning`, `blocked`, or `fail`, warnings, and errors. Invalid boundary input raises `RuntimeContractError`. A stage-level block is recorded and escalated; recovery requires correcting the earliest responsible stage and starting a new deterministic execution.

Run the executable examples and end-to-end checks with:

```sh
make runtime-test
```
