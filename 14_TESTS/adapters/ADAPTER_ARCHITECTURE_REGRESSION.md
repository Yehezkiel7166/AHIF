# Adapter Architecture Regression

## Regression Invariants

- Existing Final Prompt contracts remain model neutral.
- Adapter logic remains downstream of Final Prompt release.
- No adapter may modify Knowledge, Decision, Reasoning, or Compiler output.
- Identity-critical incompatibility blocks release.
- Unknown capability support is never assumed.
- Every transformation is represented in the execution trace.
- Adapter profile versions remain immutable.

## Sprint 007 Baseline

Sprint 007 validates architecture and contracts only. It does not claim conformance for any external image model. Model-specific implementations begin in Sprint 008.
