# Sprint 004 — Prompt Compiler Hardening

## Release

- Version: `1.4.0`
- Base version: `1.3.0`
- Status: completed

## Objective

Build a deterministic, traceable Prompt Compiler that transforms compiler-ready reasoning output into one coherent, model-neutral image-generation prompt without inventing new visual decisions.

## Scope delivered

- formal compiler pipeline
- normalized compiler-unit contract
- deterministic section ordering
- directive dependency handling
- semantic redundancy control
- contradiction detection and blocking behavior
- risk-based negative constraint synthesis
- prompt serialization contract
- compiler metadata and provenance
- machine-readable compiler plan and output schemas
- compiler QA gate and scorecard
- contract, regression, and golden-case tests

## Architectural boundary

The Decision Engine selects. The Reasoning Engine validates and explains. The Prompt Compiler expresses accepted decisions. Quality Assurance validates the compiled artifact. Model-specific adapters remain outside this sprint.

## Completion criteria

- no previous repository file removed
- canonical structure retained
- required project documents updated
- compiler contract linked to reasoning handoff and QA
- deterministic and contradiction cases documented
- version and manifest aligned at `1.4.0`
