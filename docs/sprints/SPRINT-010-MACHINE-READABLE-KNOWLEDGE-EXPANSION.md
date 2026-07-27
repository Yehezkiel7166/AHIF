# Sprint 010 — Machine-Readable Knowledge Expansion

## Release

Version: `2.0.0-rc1`

## Objective

Create the first validated machine-readable knowledge layer for AHIF while preserving canonical Markdown modules as the normative source of domain meaning.

## Delivered

- machine-readable knowledge architecture;
- stable knowledge identifier policy;
- provenance policy;
- package and registry schemas;
- central knowledge package registry;
- candidate fashion, travel, and photography packages;
- adapter-consumable capability hints;
- knowledge-package QA gates and stable failure codes;
- contract and provenance regression tests.

## Architectural decision

Structured packages are executable representations of canonical modules, not a second source of truth. A conflict always resolves in favor of the canonical Markdown source and blocks the structured package.

## Compatibility

Backward compatible with AHIF `1.9.0`. No canonical module, adapter contract, or existing file is removed.

## Acceptance criteria

- all package and registry JSON parses;
- all identifiers are unique and stable;
- every provenance path resolves;
- every package passes identity and semantic validation;
- adapter hints cannot authorize new visual decisions;
- release-candidate status is retained until cross-model validation.
