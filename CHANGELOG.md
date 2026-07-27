# Changelog

## 2.11.0 — Security and Supply Chain Governance

Added:
- S0–S9 security and supply-chain governance workflow
- dependency and artifact provenance policy
- secret and sensitive-data handling policy
- vulnerability risk, exception, and immutable snapshot governance
- security report, finding event, provenance record, and exception schemas
- append-only security findings and provenance registries with a `not-evaluated` baseline
- AHIF-SEC QA catalog, contract test, registry regression, and blocked example
- Sprint 023 and release validation documentation

Changed:
- release metadata, roadmap, manifest, README, and AI contexts synchronized to 2.11.0
- post-2.0 governance chain extended from metrics governance to security and supply-chain governance

Claim boundary:
- no external scan, vulnerability absence, production-security certification, secret revocation proof, deployment, rollback, empirical certification, or adapter-tier change is asserted

## 2.10.0 — Metrics, KPI, and Quality Governance

Added:
- MQ0–MQ9 metric definition, calculation, review, publication, and retirement workflow
- canonical AHIF-MET catalog and versioned KPI threshold policy
- denominator, missing-data, deduplication, cohort, and freshness controls
- metric specification, snapshot, and event schemas
- append-only metric registries and empty dashboard manifest
- AHIF-METRIC QA catalog, contract test, registry regression, and blocked example
- Sprint 022 and release validation documentation

Changed:
- release metadata, roadmap, manifest, README, and AI context synchronized to 2.10.0
- post-2.0 governance chain extended from compliance audit to metric and quality governance

Claim boundary:
- no observed metric value, KPI achievement, external telemetry, empirical certification, production-health certification, deployment, rollback, or adapter-tier change is asserted


## 2.9.0 — Continuous Compliance and Governance Audit

Added:
- CA0–CA9 repository compliance audit workflow
- stable AHIF-COMP rule-set and governance-drift taxonomy
- immutable audit snapshot and bounded exception policy
- append-only audit findings and compliance status registries
- audit report and event schemas
- AHIF-AUD QA catalog, contract test, and registry regression
- Sprint 021 and release validation documentation

Changed:
- release metadata, roadmap, manifest, README, and AI context synchronized to 2.9.0
- post-2.0 governance chain extended from incident response to continuous repository audit

Claim boundary:
- no real audit finding, empirical certification, production-health certification, deployment, rollback, or adapter-tier change is asserted

## 2.8.0 — Adapter Incident Response and Recovery Governance

Added:
- IR0–IR9 incident response protocol;
- bounded severity, containment, recovery, and closure governance;
- append-only incident registry, schemas, QA, contract tests, and regression baseline;
- Sprint 020 documentation and release validation.

Claim boundary:
- no real incident, external telemetry, executed containment, recovery, rollback, deployment, production-health certification, or adapter-tier change is included.

## 2.7.0 — Adapter Release Observation and Rollback Assurance Governance

Added:
- O0–O9 post-release observation protocol;
- declared-signal and observation-window governance;
- rollback assurance and reconstruction verification policy;
- append-only observation registry, schemas, QA, contract tests, and regression baseline;
- Sprint 019 documentation and release validation.

Corrected:
- stale `manifest.json` `latest_sprint` field from Sprint 017 to Sprint 019;
- latest sprint, upload guide, and release validation pointers.

Claim boundary:
- no completed release, real observation, telemetry, health certification, incident, rollback recommendation, rollback execution, or adapter-tier change is included.

## 2.6.0 — Sprint 018: Adapter Release Execution Governance

### Added
- R0–R9 adapter release execution protocol.
- Immutable release package, pre-change/post-change snapshot, and rollback governance.
- Release plan, package manifest, event, and snapshot schemas.
- Append-only release execution registry with zero-release baseline.
- `AHIF-REL-001` through `AHIF-REL-014` QA failure codes.
- Contract and registry regression tests.

### Changed
- Synchronized the stale README version header.
- Corrected latest-sprint, upload-guide, and release-validation manifest pointers.

### Governance
- Promotion authorization remains separate from repository mutation.
- No release may complete without exact declared mutations, independent approval, post-change validation, rollback readiness, and signoff.
- No empirical support claim or adapter-tier change is introduced.

## 2.5.0 — Sprint 017: Adapter Promotion Decision Dossier Governance

### Added
- P0–P9 promotion decision dossier workflow.
- Append-only promotion decision registry and event-chain governance.
- Promotion dossier and decision event schemas.
- Independent technical, governance, and authorization role requirements.
- `AHIF-PROMO-001` through `AHIF-PROMO-012` QA failure codes.
- Contract and registry regression tests with a zero-dossier baseline.

### Governance
- Authorization is explicitly separated from adapter-registry mutation.
- Promotion, hold, downgrade, and block recommendations must retain adverse evidence and drift findings.
- No empirical support claim or adapter-tier change is introduced.

## 2.4.0 — Sprint 016: Evidence Evaluation and Review Queue Governance

### Added
- deterministic E0–E9 evidence evaluation workflow;
- append-only evaluation queue governance and state model;
- immutable evaluation job and event schemas;
- reviewer-separation, duplicate-scope, and report-completion gates;
- evidence evaluation QA and stable AHIF-EVAL failure codes;
- contract tests, queue regression, illustrative blocked job, and zero-job baseline.

### Claim boundary
- no external image evidence, empirical scores, or reviewer identities are included;
- evidence registry and evaluation queue baselines remain empty;
- evaluation cannot promote adapters or alter canonical identity authority.


## 2.3.0 — Sprint 015: Evidence Ingestion and Registry Governance

### Added
- deterministic I0–I8 evidence ingestion pipeline;
- artifact integrity and SHA-256 verification policy;
- append-only evidence registry governance;
- ingestion request, result, and registry schemas;
- evidence ingestion QA and stable AHIF-ING failure codes;
- contract tests, registry regression, and zero-evidence baseline.

### Claim boundary
- no external image evidence or empirical scores are included;
- registry baseline contains zero accepted records;
- ingestion cannot promote adapters or alter canonical identity authority.


## 2.2.0 — Sprint 014: Evidence Aggregation and Target Profile Governance

### Added
- governed evidence aggregation architecture and eligibility policy;
- confidence aggregation, outlier detection, and drift protocol;
- target-profile recommendation governance;
- aggregate, recommendation, and governance report schemas;
- aggregation QA, contract tests, regression tests, and zero-evidence baseline.

### Claim boundary
- no external image evidence or empirical scores are included;
- no adapter status changes automatically;
- canonical identity authority is unchanged.


## [2.1.0] — Sprint 013: Empirical Validation Evidence Pipeline

### Added
- Empirical validation architecture for externally generated image evidence.
- Immutable evidence bundle contract.
- Identity and semantic evaluation protocols.
- Reproducibility levels R0–R4.
- Adapter promotion and downgrade gates.
- Evidence bundle, identity report, semantic report, and promotion report schemas.
- Empirical evidence QA with stable AHIF-EV failure codes.
- Evidence contract and adapter promotion regression tests.
- Evidence capture example and Sprint 013 documentation.

### Changed
- README, roadmap, version, manifest, and AI operational context now describe the post-2.0 evidence workflow.

### Compatibility
- Backward compatible with AHIF 2.0.0.
- No stable framework or adapter contract was removed.
- Existing adapters remain contract-validated experimental targets until accepted external evidence is supplied.

## [2.0.0] — Sprint 012: Stable Release

### Added
- Stable release governance and release-decision policy.
- 2.0 compatibility guarantees and semantic-versioning rules.
- Stable adapter support tiers and promotion requirements.
- Adapter contract freeze for the 2.0 line.
- Release evidence register with explicit evidence boundaries.
- Stable release QA, contract tests, and regression requirements.
- Migration guide from 1.9.0, 2.0.0-rc1, and 2.0.0-rc2.

### Changed
- Promoted the AHIF framework core and adapter contracts to stable 2.0.
- Consolidated README, roadmap, version, manifest, and AI operational context.
- Defined OpenAI Images, Midjourney, and SDXL/Diffusers as contract-validated experimental targets.

### Compatibility
- Backward compatible with 2.0.0-rc2.
- No canonical file, schema, adapter, knowledge package, or previous test was removed.
- No empirical image-output equivalence or production-certified target support is claimed.

## [2.0.0-rc2] — Sprint 011: Cross-Model Validation

### Added
- Cross-model validation architecture and deterministic V0–V7 execution protocol.
- Identity preservation comparison and machine-readable report schema.
- Degradation audit, evidence integrity, and reproducibility policies.
- Release-candidate conformance matrix and validation baseline.
- Cross-model validation QA with stable AHIF-VAL failure codes.
- Contract tests, release-candidate regression suite, and Kyoto/Tokyo fixtures.

### Changed
- README, roadmap, version, manifest, and AI operational context now distinguish contract validation from empirical image validation.

### Compatibility
- Backward compatible with 2.0.0-rc1. No canonical module, structured knowledge package, adapter, or previous test was removed.
- All adapters remain experimental. No generated-image equivalence or production support is claimed without external empirical evidence.

## [2.0.0-rc1] — Sprint 010: Machine-Readable Knowledge Expansion

### Added
- Machine-readable knowledge architecture and authority model.
- Stable knowledge identifier and provenance policies.
- Knowledge package and registry schemas.
- Central package registry.
- Candidate fashion, travel, and photography knowledge packages.
- Knowledge package QA gates and stable failure codes.
- Contract and provenance regression tests.

### Changed
- README, roadmap, version, manifest, and AI operational context now describe release-candidate structured knowledge consumption.

### Compatibility
- Backward compatible with 1.9.0. No existing canonical file or adapter contract was removed.

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
