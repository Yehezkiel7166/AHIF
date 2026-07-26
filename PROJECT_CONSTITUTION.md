# AHIF Project Constitution

## Status

This document is the permanent architectural constitution of the Artificial Human Identity Framework. It constrains roadmap interpretation, sprint planning, implementation, documentation, and release acceptance.

## Mission

AHIF is a long-term software engineering framework for compiling high-quality prompts for AI image generators while preserving one human identity from a single canonical master photograph.

AHIF is not a prompt collection. It is a modular system with knowledge, inference, reasoning, compilation, validation, orchestration, and model adaptation responsibilities.

## Canonical Identity

The master photograph is the sole canonical identity authority.

No subsystem may introduce:

- identity drift;
- generic model substitution;
- facial redesign;
- ethnicity drift;
- age drift;
- untraceable identity reinterpretation.

Identity preservation has higher priority than realism, beauty, style, or model-specific optimization.

## Core Philosophy

1. Identity First
2. Human Second
3. Reality Third
4. Beauty Fourth

## Architectural Sequence

```text
Knowledge Graph
→ Decision Engine
→ Reasoning Engine
→ Prompt Compiler
→ Quality Assurance
→ Final Prompt
→ Model Adapter
```

A downstream layer may transform or validate upstream output, but it must not silently override upstream identity constraints or invent unsupported decisions.

## Engineering Principles

All framework behavior must be:

- explainable;
- modular;
- versioned;
- maintainable;
- reusable;
- scalable;
- deterministic where the same normalized input and configuration are used.

## Repository Governance

The repository is the source of truth. Every sprint must preserve established architecture unless a documented architectural decision justifies a change.

Each release must update:

- `README.md`;
- `VERSION.md`;
- `CHANGELOG.md`;
- `ROADMAP.md`;
- `manifest.json`;
- sprint documentation.

No completed sprint artifact may be deleted. New documentation must reference existing contracts instead of duplicating them.

## Sprint Completion Contract

A sprint is complete only when:

1. its scope follows the canonical roadmap;
2. all introduced contracts are linked from the repository;
3. machine-readable schemas are internally consistent;
4. regression or conformance documentation covers the new behavior;
5. no previous file is removed without an explicit migration decision;
6. the full repository and patch packages are reproducible.

## Adapter Boundary

Model adapters are downstream translators. They may convert canonical final prompt packages into model-specific syntax, weights, ordering, or parameter recommendations.

Adapters must not:

- change canonical identity facts;
- make new visual decisions;
- erase reasoning provenance;
- weaken blocking QA findings;
- claim support for a model capability that is not declared in its capability profile.
