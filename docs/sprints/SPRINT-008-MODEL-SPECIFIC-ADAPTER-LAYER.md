# Sprint 008 — Model-Specific Adapter Layer

## Release

Version: `1.8.0`

## Objective

Implement the first versioned target-model adapters on top of the Sprint 007 architecture while preserving the model-neutral Final Prompt Package and identity-first release rules.

## Delivered

- experimental OpenAI Images adapter;
- experimental Midjourney adapter;
- experimental SDXL Diffusers adapter;
- immutable date-stamped capability profiles;
- exact adapter registry;
- target request serialization contract;
- parameter and identity-reference mapping policies;
- target request schema;
- adapter-specific QA gates;
- contract and regression fixtures.

## Architectural Decision

Target integrations remain experimental in 1.8.0. AHIF does not claim semantic equivalence across models until Sprint 009 establishes cross-model compatibility contracts and comparison tests.

## Compatibility

Backward compatible with AHIF 1.7.0. No canonical upstream contract or existing file is removed.

## Acceptance Criteria

- all adapters resolve by exact version;
- every capability assumption is profile-backed;
- unsupported identity-critical mappings block;
- serializers reject unknown parameters;
- loss disclosure is complete;
- adapter outputs are deterministic;
- production support is not falsely claimed.
