# Sprint 007 — Adapter Architecture Foundation

## Release

Version: `1.7.0`

## Objective

Establish the governed architecture, lifecycle, capability model, compatibility policy, schemas, QA gates, and conformance baseline required before AHIF implements model-specific adapters.

## Scope

- permanent project constitution;
- formal adapter boundary after Final Prompt release;
- adapter lifecycle and registry contract;
- model capability classification;
- multi-model compatibility and loss policy;
- transformation plan and result schemas;
- adapter QA gates;
- conformance and regression specifications;
- staged roadmap from 1.7 through 2.0.

## Architectural Decision

Sprint 007 does not implement a target-model adapter. This separation prevents model-specific syntax from defining the canonical architecture and preserves the model-neutral Final Prompt contract.

## Compatibility

The release is backward compatible with AHIF 1.6.0. Existing identity, knowledge, decision, reasoning, compiler, QA, and Final Prompt contracts remain unchanged.

## Acceptance Criteria

- the adapter boundary is explicit;
- identity-critical loss always blocks release;
- capability support cannot be assumed;
- every transformation is auditable;
- schemas cover profile, planning, and results;
- adapter QA and conformance requirements are documented;
- all previous repository files remain present.
