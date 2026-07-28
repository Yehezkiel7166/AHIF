# AHIF — Artificial Human Identity Framework

**Version:** 3.2.0
**Status:** Stable Framework + Executable Repository Automation; LTS Designation HOLD
**Primary use case:** Consistent AI travel influencer generation from one canonical master photo.

AHIF is a modular software-engineering framework for generating a persistent digital human whose identity remains stable while clothing, hairstyle, pose, expression, activity, camera, weather response, and storytelling adapt to the requested context.

## Core operating principle

> Identity First. Human Second. Reality Third. Beauty Fourth.

## Framework pipeline

```text
Knowledge Graph
→ Decision Engine
→ Reasoning Engine
→ Prompt Compiler
→ Quality Assurance
→ Final Prompt
→ Model Adapter
```

Version 3.2.0 preserves the stable framework, canonical identity authority, prior governance modules, and claim boundaries while making repository validation, regression, release gates, and health reporting executable. Repository validation does not establish production health or operational LTS support; the LTS designation remains `hold`.

## Daily use

1. Upload the canonical master photo to the image generator.
2. Upload `00_CONTEXT/AHIF_AI_CONTEXT.md` to ChatGPT.
3. Ask ChatGPT to load the framework.
4. Provide a compact request:

```text
Location: Kyoto, Japan
Place: Gion district
Atmosphere: calm autumn morning
Output: final image-generation prompt
```

5. AHIF normalizes context, resolves decisions, validates reasoning, compiles one coherent prompt, runs mandatory QA gates, and releases only a validated artifact.

## Architectural responsibilities

- **Knowledge Graph** represents reusable facts and relationships.
- **Decision Engine** selects context-appropriate visual decisions.
- **Reasoning Engine** validates causality, evidence, alternatives, confidence, identity safety, and cross-domain coherence.
- **Prompt Compiler** expresses accepted decisions in deterministic model-neutral prompt form without inventing new decisions.
- **Quality Assurance** applies mandatory gates, deterministic linting, failure classification, scoring, and recovery routing.
- **Final Prompt Engine** orchestrates the complete execution, enforces release eligibility, and emits the validated prompt package and explainable result summary.
- **Model Adapter Layer** translates a released package into an exact target request while preserving identity, semantics, provenance, and loss disclosure.

## Repository map

- `00_CONTEXT/` — condensed operational context for AI loading
- `01_FOUNDATION/` — philosophy, constitution, architecture, vocabulary
- `02_CORE_IDENTITY/` — canonical identity and anti-drift rules
- `03_HUMAN_SIMULATION/` — anatomy, behavior, body language, realism
- `04_CHARACTER/` — personality, emotion, habits, continuity
- `05_FASHION/` — context-aware wardrobe, hair, makeup, accessories
- `06_TRAVEL_WORLD/` — geography, culture, weather, transport, safety
- `07_PHOTOGRAPHY/` — camera, lens, lighting, composition
- `08_STORY/` — narrative and environmental interaction
- `09_DECISION_ENGINE/` — context, knowledge graph, structured knowledge packages, inference, resolution, and reasoning
- `10_PROMPT_COMPILER/` — compiler pipeline, schemas, ordering, contradiction control, and serialization
- `11_QUALITY_ASSURANCE/` — QA orchestration, linting, failure taxonomy, recovery, schemas, domain gates, and final validation
- `12_TEMPLATES/` — reusable input and output templates
- `13_EXAMPLES/` — worked examples
- `14_TESTS/` — identity, decision, reasoning, compiler, QA, and final-prompt regression tests
- `15_FINAL_PROMPT/` — execution orchestration, release contracts, schemas, and final prompt packaging
- `16_MODEL_ADAPTERS/` — adapter architecture, registry, profiles, serializers, compatibility, empirical evidence, release, observation, and incident governance
- `17_CONTINUOUS_AUDIT/` — continuous compliance rules, drift detection, exceptions, snapshots, and append-only audit status
- `18_METRICS_QUALITY/` — canonical metrics, KPI thresholds, denominator controls, snapshots, and dashboard governance
- `19_SECURITY_SUPPLY_CHAIN/` — security scope, provenance, secret handling, vulnerability risk, exceptions, snapshots, and append-only registries
- `20_OPERATIONAL_RESILIENCE/` — recovery objectives, backup/restore governance, disaster declaration, runbooks, exercises, and resilience registries
- `21_LTS_GOVERNANCE/` — LTS designation, compatibility, maintenance, backport, deprecation, retirement, evidence, and registries
- `scripts/` — dependency-free validation, regression, failure-injection, release-gate, health, and canonical full-test entry points
- `.github/workflows/` — least-privilege validation, regression, and release-gate automation
- `docs/sprints/` — versioned sprint documentation
- `assets/identity-reference/` — canonical master-photo location

## Source of truth

The repository is the source of truth. AI context files are condensed operational views derived from canonical modules.

## Canonical identity rule

The uploaded master photo is the only canonical identity reference. Text may clarify the image but must never replace, reinterpret, or override it.

## Current release — 3.2.0

Sprint 027 hardens Sprint 026 automation with a canonical `make test` harness, versioned JSON reports, isolated failure injection, deterministic exit codes, CI artifacts, and composed release enforcement. Run `scripts/validate_repository.sh`, `scripts/run_regression.sh`, and `scripts/release_gate.sh` locally; pull requests and release tags run equivalent GitHub Actions gates. `python3 scripts/repository_health.py` emits a machine-readable repository-only assessment.

Passing automation establishes repository conformance only. The baseline still contains zero registered LTS releases and zero maintenance events. The LTS designation is `hold`; no maintainer commitment, support adoption, backport execution, SLA achievement, deployment, empirical certification, production health, or production availability is asserted.

## Version 2.2 evidence aggregation

Accepted evidence bundles may now be grouped into explicit cohorts, aggregated conservatively, audited for outliers and drift, and converted into advisory target-profile recommendations. The framework does not include real external evidence in this release and never promotes adapters automatically.


## Version 2.3 evidence ingestion

Owner-supplied evidence can now be checked against explicit request and result schemas, verified using SHA-256 artifact fingerprints, classified as accepted, quarantined, rejected, or duplicate, and indexed in an append-only registry. Empirical evaluation and adapter promotion remain separate governed processes.


## Version 2.4 evidence evaluation

Only accepted evidence records may enter the evaluation queue. Evaluation jobs pin all governed versions, preserve append-only reviewer events, and resolve to completed, needs-revision, blocked, or cancelled without changing adapter status.


## Version 2.5 promotion decisions

Only completed evaluation jobs and eligible aggregates may enter a promotion dossier. Recommendations and authorizations are append-only governance records. Adapter registry mutation requires a separate release action with before/after snapshots, rollback instructions, stable-release QA, and documentation updates.


## Version 2.6 release execution

Only an authorized promote or downgrade dossier may open an adapter release plan. Every mutation must be declared, fingerprinted, validated, independently approved, reversible, and reconciled with repository documentation. AHIF 2.6.0 defines this mechanism without executing a real release.


## Version 2.7 release observation

Only a completed and signed release may open an observation plan. Observation may classify repository-level conformance and rollback readiness, but it cannot prove production health, create empirical evidence, mutate the adapter registry, or execute rollback.


## Sprint 022 Metrics and Quality Rule

Treat every metric as a versioned governance contract. Pin the exact population, numerator, denominator, exclusions, missing-data treatment, threshold version, and source fingerprints. Empty populations must produce `not-evaluated`, not zero or success. Dashboards are projections of immutable snapshots and may not fabricate telemetry, KPI achievement, empirical certification, production health, or adapter-tier changes. The AHIF 2.10.0 baseline contains zero registered metric specifications, zero metric snapshots, and zero dashboards.

## Sprint 023 Security and Supply Chain Rule

Treat repository security as a scoped, evidence-bound governance process. Never store raw secrets, fabricate advisory data, infer vulnerability absence from an empty finding registry, or treat repository review as infrastructure penetration testing. Unknown executable provenance and unresolved critical exposure block release eligibility. The AHIF 2.11.0 baseline contains zero security findings, zero provenance records, and status `not-evaluated`.
