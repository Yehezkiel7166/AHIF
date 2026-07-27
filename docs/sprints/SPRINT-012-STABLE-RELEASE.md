# Sprint 012 — Stable Release

## Release

- Version: `2.0.0`
- Base: `2.0.0-rc2`
- Status: Completed

## Objective

Promote the AHIF framework core and adapter contract system to a stable 2.0 release while preserving an explicit boundary between repository-level validation and external image-output evidence.

## Delivered

- release governance;
- compatibility guarantees;
- stable adapter support policy;
- adapter contract freeze;
- release evidence register;
- stable release QA;
- stable release contract and regression tests;
- 2.0 migration guide;
- consolidated release metadata and documentation.

## Release decision

The framework core, schemas, registries, deterministic pipelines, QA gates, final-prompt packaging, and adapter contracts are stable.

OpenAI Images, Midjourney, and SDXL/Diffusers remain contract-validated experimental targets. Empirical image-output equivalence is not claimed.

## Backward compatibility

No canonical file, schema, adapter, knowledge package, or previous test is removed.
