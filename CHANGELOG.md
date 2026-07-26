# Changelog

## [1.9.0] — Sprint 009: Multi-Model Compatibility Contracts

### Added

- Formal request-level multi-model compatibility contract.
- Semantic equivalence model with identity-first confidence floors.
- Compatibility matrix for OpenAI Images, Midjourney, and SDXL Diffusers.
- Variance and tolerance policy for target-native differences.
- Deterministic cross-model comparison protocol.
- Compatibility report and interoperability result schemas.
- Cross-model compatibility QA with stable failure codes.
- Equivalence, interoperability, and contract regression tests.
- Kyoto cross-model comparison scenario.

### Changed

- Extended the experimental adapter layer with auditable cross-adapter comparison.
- Updated repository metadata, roadmap, context, and release documentation for Sprint 009.

### Compatibility

- Backward compatible with AHIF 1.8.0.
- No previous files or canonical contracts were removed.
- Request-level compatibility does not claim empirical image-output parity.
- All model adapters remain experimental pending Sprint 011 cross-model validation.

## [1.8.0] — Sprint 008: Model-Specific Adapter Layer

### Added

- Experimental OpenAI Images, Midjourney, and SDXL Diffusers adapters.
- Exact machine-readable adapter registry.
- Immutable, date-stamped target capability profiles.
- Target request serialization and parameter mapping contracts.
- Canonical identity-reference mapping policy.
- Target request schema, adapter QA, contract tests, and regression fixtures.

### Changed

- Advanced the adapter layer from architecture-only contracts to executable target-specific serialization specifications.
- Updated repository metadata and operational context for Sprint 008.

### Compatibility

- Backward compatible with AHIF 1.7.0.
- No previous files or canonical contracts were removed.
- All target adapters remain experimental until cross-model compatibility validation in Sprint 009.

## [1.7.0] — Sprint 007: Adapter Architecture Foundation

### Added

- Permanent AHIF Project Constitution.
- Formal Model Adapter architecture and lifecycle.
- Adapter registry and immutable capability profile contracts.
- Multi-model compatibility, degradation, and loss-disclosure policy.
- Adapter profile, transformation plan, and adapter result schemas.
- Adapter QA gates and conformance test specifications.
- Staged release roadmap from 1.7.0 to 2.0.0.

### Changed

- Extended the canonical architectural sequence with a downstream Model Adapter layer.
- Updated repository metadata and documentation for Sprint 007.

### Compatibility

- Backward compatible with AHIF 1.6.0.
- No existing file or canonical contract was removed.
- No external image model is declared supported in this release.


## 1.6.0 — Final Prompt Orchestration

Added:
- formal Final Prompt Engine architecture
- deterministic F0–F7 execution orchestration
- final prompt release contract and eligibility states
- bounded correction and identity recovery budgets
- explainable result summary contract
- execution trace contract
- machine-readable execution request, execution trace, and final prompt package schemas
- final prompt request and response templates
- Kyoto cold-morning and Tokyo rain release-level scenarios
- final prompt contract, regression, and scenario-corpus acceptance tests
- Sprint 006 documentation and upload guide

Changed:
- framework pipeline now completes the canonical path through Final Prompt release
- README now documents the Final Prompt Engine responsibility and repository module
- roadmap now marks v1.6 complete and advances to v2.0 model-specific adapters
- manifest now identifies Final Prompt orchestration as the latest sprint
- AI context now requires release eligibility, explainable summaries, and traceable final packaging

## 1.5.0 — Quality Assurance Engine Hardening

Added:
- formal Quality Assurance Engine architecture and execution pipeline
- deterministic prompt lint rule catalog with stable AHIF-L identifiers
- failure taxonomy with stable codes and severity levels
- mandatory identity, anatomy, context, compiler-integrity, and output-contract gates
- weighted QA scoring model with non-negotiable identity override
- recovery orchestration with R0–R6 escalation levels
- QA report contract and machine-readable schema
- end-to-end validation contract
- QA contract, regression, recovery, and end-to-end test suites
- Sprint 005 documentation and upload guide

Changed:
- final validation now operates as a release gate rather than a simple checklist
- QA scorecard now uses category scores, mandatory minimums, and aggregate release thresholds
- prompt lint checklist now references the stable lint rule catalog
- AI context now requires formal QA reporting, failure codes, recovery routing, and release eligibility
- roadmap now marks Quality Assurance Engine hardening complete and advances to Final Prompt orchestration

## 1.4.0 — Prompt Compiler Hardening

Added:
- formal Prompt Compiler pipeline
- normalized compiler-unit contract
- deterministic section ordering
- directive dependency and priority rules
- semantic redundancy control
- compiler contradiction detection and blocking behavior
- risk-based negative constraint synthesis
- model-neutral prompt serialization profile
- compiler metadata and provenance contract
- machine-readable compiler plan schema
- machine-readable compiled prompt schema
- compiler QA gate and scorecard
- compiler contract, regression, and golden-case tests
- Sprint 004 documentation

Changed:
- compiler specification now defines a deterministic reasoning-to-prompt pipeline
- master prompt template now covers full human, environment, photography, lighting, realism, and story handoff
- AI context now requires compiler planning, contradiction gating, metadata, and QA handoff
- roadmap now marks Prompt Compiler hardening complete and advances to Quality Assurance Engine hardening

## 1.3.0 — Reasoning Engine

Added:
- formal reasoning engine architecture
- reasoning state model and lifecycle
- causal reasoning protocol
- evidence and provenance policy
- alternative evaluation and canonical rejection reasons
- confidence propagation and identity-confidence floor
- identity-first reasoning protocol
- cross-domain coherence validation
- reasoning trace template and execution pipeline
- machine-readable reasoning output schema
- compiler reasoning handoff contract
- reasoning QA, scorecard, and regression tests
- Sprint 003 documentation

Changed:
- architecture now includes Reasoning Engine as a dedicated layer
- AI context now requires a compiler-ready reasoning record
- roadmap now preserves the sequence from reasoning to compiler hardening and QA hardening

## 1.2.0 — Knowledge Graph and Decision Engine

Added:
- knowledge graph node and edge schemas
- relationship vocabulary and graph priorities
- structured context model and normalization
- confidence and missing-input policies
- inference pipeline
- weather, activity, fashion, pose, camera, lighting, and story inference
- rule resolver and conflict detection
- weighted decision scoring
- Why Engine and decision trace
- compiler input and output schemas
- decision QA and regression cases
- Sprint 002 documentation

## 1.1.0 — Core Identity Hardening

Added:
- identity invariants and identity signature
- identity entropy controls
- master-photo and reference hierarchy protocols
- age, skin, expression, and pose continuity rules
- identity conflict matrix
- identity risk scoring
- identity recovery workflow
- identity QA checklist and failure codes
- baseline and stress tests
- Sprint 001 documentation

## 1.0.0 — Initial foundation release

Added:
- Canonical identity constitution
- Human realism hierarchy
- Context-aware styling rules
- Travel and cultural adaptation rules
- Photography decision framework
- Prompt compiler specification
- Quality assurance scorecard
- Quick, core, and full AI context packs
- Templates, examples, and regression tests
