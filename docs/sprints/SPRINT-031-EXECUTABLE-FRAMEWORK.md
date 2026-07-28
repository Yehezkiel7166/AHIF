# Sprint 031 — Executable AHIF Framework

Version 3.5.0 establishes `Framework.execute()` as the sole canonical execution method. The compatibility function and CLI delegate to it. Its explicit state machine executes context, identity, knowledge, decision, reasoning, compilation, mandatory QA, final packaging, and adapter preparation without external API or image-model execution.

The backward-compatible result now includes decision and reasoning outputs, compiled prompt, QA report, final prompt, adapter request, metadata, complete trace, pipeline state, and a deterministic machine-readable execution report. Tests cover normal, input and identity validation, compiler and QA failures, blocked release, recovery, scenarios, and identical-input reproducibility.

This sprint does not change canonical identity, governance, adapter contracts, Release Eligibility, or LTS. It supplies no empirical validation and makes no production-readiness claim.
