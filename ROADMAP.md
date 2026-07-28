# Roadmap

## Architectural sequence

```text
Knowledge Graph
→ Decision Engine
→ Reasoning Engine
→ Prompt Compiler
→ Quality Assurance
→ Final Prompt
→ Model Adapter
```

## Path to 2.0

### 1.7 — Sprint 007: Adapter Architecture Foundation
- Adapter boundary and lifecycle
- Registry and capability profile contracts
- Compatibility and degradation policy
- Transformation and result schemas
- Adapter QA and conformance baseline

### 1.8 — Sprint 008: Model-Specific Adapter Layer — Completed
- Experimental OpenAI Images, Midjourney, and SDXL Diffusers adapters
- Exact registry and immutable capability snapshots
- Target request serializers and parameter mapping
- Identity-reference mapping and loss disclosure
- Adapter-specific QA and regression fixtures

### 1.9 — Sprint 009: Multi-Model Compatibility Contracts — Completed
- Cross-adapter semantic equivalence contract
- Compatibility matrix and variance tolerance
- Deterministic cross-model comparison reports
- Adapter interoperability regression

### 2.0.0-rc1 — Sprint 010: Machine-Readable Knowledge Expansion — Completed
- Structured knowledge packages
- Stable knowledge identifiers
- Knowledge provenance and validation
- Adapter-consumable capability metadata

### 2.0.0-rc2 — Sprint 011: Cross-Model Validation — Completed
- End-to-end contract and semantic conformance architecture
- Identity preservation comparison and evidence schema
- Degradation and reproducibility audits
- Release candidate regression suite and fixtures

### 2.0.0 — Sprint 012: Stable Release — Completed
- Stable framework and adapter contracts
- Contract-validated multi-model support with explicit empirical-evidence boundary
- Consolidated release governance and documentation
- 2.0 migration and compatibility guarantees

## Completed

### 1.1
- Core identity hardening
- Identity risk scoring
- Identity failure recovery
- Identity regression testing

### 1.2
- Knowledge graph foundation
- Context normalization
- Decision inference pipeline
- Conflict resolution
- Why Engine
- Compiler schemas
- Decision regression testing

### 1.3
- Formal Reasoning Engine
- Causal reasoning and evidence provenance
- Alternative evaluation
- Confidence propagation
- Identity-first reasoning
- Cross-domain coherence
- Reasoning output schema
- Reasoning QA and regression testing

### 1.4
- Formal Prompt Compiler pipeline
- Directive normalization and deterministic section ordering
- Redundancy and contradiction control
- Risk-based negative constraint synthesis
- Prompt serialization and compiler metadata
- Compiler plan and output schemas
- Compiler QA, contract, regression, and golden-case testing

### 1.5
- Quality Assurance Engine hardening
- Automated prompt linting
- Identity, anatomy, context, compiler, and output validation gates
- Stable failure classification and severity model
- Recovery orchestration and escalation
- Machine-readable QA report schema
- End-to-end QA regression suite

### 1.6
- Final Prompt Engine orchestration
- Unified F0–F7 execution contract from compact input to validated output
- Release eligibility and bounded recovery
- Explainable result summary
- Execution trace and final prompt package schemas
- Final request and response templates
- Release-level scenario corpus
- Final prompt contract and regression testing

### 1.7
- Project Constitution
- Adapter Architecture Foundation
- Capability and compatibility contracts
- Transformation planning schemas
- Adapter QA and conformance baseline

### 1.8
- First versioned model-specific adapters
- Target request serialization contracts
- Capability snapshots and parameter mappings
- Identity-safe degradation and blocking
- Adapter QA and regression fixtures


### 1.9
- Multi-model compatibility contract
- Semantic equivalence model
- Adapter compatibility matrix
- Variance and tolerance policy
- Cross-model comparison protocol
- Compatibility and interoperability schemas
- Cross-model QA and regression testing


### 2.0.0-rc1
- Machine-readable knowledge architecture
- Stable knowledge identifiers and provenance
- Package and registry schemas
- Candidate fashion, travel, and photography packages
- Knowledge QA and provenance regression testing


### 2.0.0-rc2
- Cross-model validation architecture and V0–V7 protocol
- Identity preservation comparison protocol
- Degradation audit and evidence reproducibility policy
- Validation and identity comparison schemas
- Cross-model QA with stable AHIF-VAL failure codes
- Release-candidate regression fixtures and baseline

### 2.0.0
- Stable release governance and compatibility guarantees
- Stable adapter support tiers and contract freeze
- Release evidence register and claim boundary
- Stable release QA and regression gates
- 2.0 migration guide and consolidated release documentation

## Post-2.0 roadmap

### 2.1.0 — Sprint 013: Empirical Validation Evidence Pipeline — Completed
- External execution evidence bundle contract
- Identity and semantic evaluation protocols
- Reproducibility levels and evidence integrity gates
- Adapter promotion and downgrade governance
- Empirical evidence schemas, QA, and regression tests

### 2.2.0 — Sprint 014: Evidence Aggregation and Target Profile Governance — Completed
- Evidence eligibility, cohorting, and aggregation architecture
- Conservative confidence classes and limiting-dimension reporting
- Outlier and model-version drift protocol
- Evidence-backed target-profile recommendation governance
- Aggregation schemas, QA, contract tests, and baseline

### 2.3.0 — Sprint 015: Evidence Ingestion and Registry Governance — Completed
- Deterministic external evidence intake and classification
- SHA-256 artifact integrity and provenance validation
- Duplicate detection and append-only registry governance
- Ingestion schemas, QA, contract tests, and zero-evidence baseline

### 2.4.0 — Sprint 016: Evidence Evaluation and Review Queue Governance — Completed
- Deterministic E0–E9 post-ingestion evaluation workflow
- Append-only evaluation queue and governed state transitions
- Immutable job scope, report linkage, and reviewer-separation rules
- Evaluation schemas, QA, contract tests, and zero-job baseline

### 2.5.0 — Sprint 017: Adapter Promotion Decision Dossier Governance — Completed
- Deterministic P0–P9 promotion decision workflow
- Append-only dossier registry and decision event chain
- Independent technical, governance, and authorization roles
- Explicit authorization versus adapter-registry mutation boundary
- Promotion dossier schemas, QA, contract tests, and zero-dossier baseline

### 2.6.0 — Sprint 018: Adapter Release Execution Governance — Completed
- Deterministic R0–R9 adapter release execution workflow
- Immutable release package and pre-change/post-change snapshot contracts
- Independent approval, validation, signoff, and rollback governance
- Append-only release execution registry and stable AHIF-REL failure codes
- Release schemas, QA, contract tests, and zero-release baseline

### 2.7.0 — Sprint 019: Adapter Release Observation and Rollback Assurance Governance — Completed
- Deterministic O0–O9 post-release observation workflow
- Declared-signal inventory and signed observation baselines
- Continuous rollback reconstruction assurance
- Independent response authorization and append-only observation records
- Observation schemas, QA, contract tests, and zero-observation baseline

### 2.8.0 — Sprint 020: Adapter Incident Response and Recovery Governance — Completed
- Deterministic IR0–IR9 incident workflow
- Bounded severity, reversible containment, and recovery-path governance
- Independent response authorization and validation
- Append-only incident registry and stable AHIF-INC failure codes
- Incident schemas, contract tests, and zero-incident baseline

### 2.9.0 — Sprint 021: Continuous Compliance and Governance Audit — Completed
- Deterministic CA0–CA9 repository audit workflow
- Stable compliance rule-set and governance-drift detection
- Immutable snapshots and time-bounded exception governance
- Append-only findings and compliance-status baselines
- Audit schemas, QA, contract tests, and zero-finding baseline

### 2.10.0 — Sprint 022: Metrics, KPI, and Quality Governance — Completed
- Deterministic MQ0–MQ9 metric lifecycle
- Canonical metric catalog and versioned KPI thresholds
- Denominator, missing-data, cohort, deduplication, and freshness governance
- Immutable metric snapshots and dashboard publication contracts
- Metric schemas, QA, contract tests, and zero-metric baseline

### 2.11.0 — Sprint 023: Security and Supply Chain Governance — Completed
- Deterministic S0–S9 security and supply-chain workflow
- Asset inventory, provenance, secret-handling, vulnerability, remediation, and exception governance
- Immutable security snapshots and append-only findings/provenance registries
- Security schemas, QA, contract tests, regression tests, and `not-evaluated` baseline

### 2.12.0 — Sprint 024: Operational Resilience and Disaster Recovery Governance — Completed
- Deterministic OR0–OR9 resilience and recovery workflow
- Recovery objectives, dependency maps, backup/restore, disaster declaration, and runbook standards
- Governed exercises, failover controls, independent validation, and immutable event chains
- Recovery schemas, QA, contract tests, regression tests, and `not-evaluated` baseline

## 3.x stabilization

### 3.0.0 — Sprint 025: V3 LTS Stabilization — Repository Complete; LTS Designation HOLD
- Deterministic LTS0–LTS9 candidate, designation, maintenance, and retirement workflow
- Preservation of canonical identity rules, stable 2.x contracts, registry history, and all prior claim boundaries
- Governed support scope, change classification, backports, deprecation, supersession, and retirement
- LTS schemas, append-only empty registries, QA, contract tests, regression tests, and blocked example
- Repository validation passed; independent governance approval and operational support remain unverified, so LTS designation is `hold`

### 3.1.0 — Sprint 026: Executable Repository Automation — Completed
- Dependency-free repository-wide validation and governance regression scripts
- Pull-request, main-branch, manual, and version-tag GitHub Actions workflows
- Composed release gates with synchronized evidence requirements
- Machine-readable and checked-in repository health reporting
- Repository gates passed; production health and operational LTS designation remain explicitly out of scope and `hold`

### Future 2.x direction
- Real evidence records and evaluation jobs after user-provided model executions
- Expanded machine-readable knowledge packages
- Backward-compatible adapter capability updates
- Governance-approved adapter profile maintenance

### 3.2.1 — Sprint 027: Executable Verification Hardening — Completed
- Canonical fail-fast test harness and deterministic exit codes
- Versioned JSON reports and dual-format repository health inventory
- Six isolated failure-injection tests and end-to-end release enforcement
- Hardened artifact-producing pull-request CI and simple Make targets
- Repository conformance can pass while release eligibility and LTS designation remain `hold`

### 3.2.1 — Sprint 028: Automation Stabilization — Completed
- Shared machine-readable automation configuration and canonical execution engine
- Deterministic ignored report lifecycle, freshness enforcement, and negative self-tests
- Consolidated CI execution with timeouts, concurrency, retention, and summaries
- Repository conformance can pass while release eligibility and LTS designation remain `hold`

### 3.3.0 — Sprint 029: Framework Completion Audit — Completed
- All 22 required module roots traced to architecture, contracts, schemas, regressions, examples, pipeline stages, and outputs
- User Request through Model Adapter hand-offs verified and documented
- Executable completion audit added to the canonical full-test harness
- Internal links and manifest registration enforced with zero architectural gaps at audit completion
- Repository architecture complete within the documented boundary; Release Eligibility and LTS remain `hold`

## Sprint 030 — Runtime execution engine (3.4.0)

Completed: canonical sequential runtime, explicit stage contracts, deterministic execution traces, mandatory QA, adapter preparation, executable examples, and end-to-end tests. External model execution and empirical validation are not claimed. Release Eligibility and LTS remain HOLD.
