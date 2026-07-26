# Sprint 009 — Multi-Model Compatibility Contracts

## Release

Version: `1.9.0`

## Objective

Define deterministic, identity-first contracts for evaluating whether different target-model adapters preserve the same canonical Final Prompt Package semantics.

## Delivered

- formal compatibility contract;
- semantic equivalence model;
- adapter compatibility matrix;
- variance and tolerance policy;
- cross-model comparison protocol;
- compatibility and interoperability schemas;
- cross-model QA gates and stable failure codes;
- equivalence, interoperability, and contract regression tests;
- worked Kyoto cross-model comparison scenario.

## Architectural Decision

Version 1.9.0 validates request-level semantic compatibility. It does not claim pixel-level or empirical generated-image equivalence. All adapters remain experimental until Sprint 011 performs end-to-end cross-model validation.

## Compatibility

Backward compatible with AHIF 1.8.0. No canonical upstream contract or existing file is removed.

## Acceptance Criteria

- every comparison uses one canonical source package;
- exact adapter and profile versions are recorded;
- identity-domain confidence is at least 0.95;
- all losses and variances are disclosed;
- compatibility reports are deterministic;
- interoperability regressions cover all registered adapters;
- production promotion remains blocked pending empirical validation.
