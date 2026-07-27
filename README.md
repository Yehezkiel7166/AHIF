# AHIF — Artificial Human Identity Framework

**Version:** 2.4.0
**Status:** Stable Framework + Governed Evidence Evaluation Infrastructure
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

Version 2.4.0 preserves the stable 2.x framework and adds deterministic post-ingestion evaluation jobs, append-only review events, reviewer-separation controls, and a zero-job evaluation queue baseline. It preserves strict boundaries between ingestion, evaluation, aggregation, and human adapter-promotion governance.

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
- `16_MODEL_ADAPTERS/` — adapter architecture, registry, profiles, serializers, compatibility, empirical evidence, aggregation, and target-profile governance
- `docs/sprints/` — versioned sprint documentation
- `assets/identity-reference/` — canonical master-photo location

## Source of truth

The repository is the source of truth. AI context files are condensed operational views derived from canonical modules.

## Canonical identity rule

The uploaded master photo is the only canonical identity reference. Text may clarify the image but must never replace, reinterpret, or override it.

## Current release — 2.5.0

Sprint 017 adds Adapter Promotion Decision Dossier Governance. Completed evaluations and eligible aggregates can be assembled into deterministic P0–P9 dossiers that recommend promote, hold, downgrade, or block outcomes. Dossiers preserve adverse evidence, append-only events, exact policy versions, reviewer separation, and an explicit authorization boundary.

The repository baseline contains no external execution evidence, accepted registry records, completed evaluation jobs, promotion dossiers, authorizations, or empirical scores. OpenAI Images, Midjourney, and SDXL/Diffusers remain at their existing support tiers. Authorization never changes the adapter registry automatically.

The permanent architectural rules are defined in [`PROJECT_CONSTITUTION.md`](PROJECT_CONSTITUTION.md).

## Version 2.2 evidence aggregation

Accepted evidence bundles may now be grouped into explicit cohorts, aggregated conservatively, audited for outliers and drift, and converted into advisory target-profile recommendations. The framework does not include real external evidence in this release and never promotes adapters automatically.


## Version 2.3 evidence ingestion

Owner-supplied evidence can now be checked against explicit request and result schemas, verified using SHA-256 artifact fingerprints, classified as accepted, quarantined, rejected, or duplicate, and indexed in an append-only registry. Empirical evaluation and adapter promotion remain separate governed processes.


## Version 2.4 evidence evaluation

Only accepted evidence records may enter the evaluation queue. Evaluation jobs pin all governed versions, preserve append-only reviewer events, and resolve to completed, needs-revision, blocked, or cancelled without changing adapter status.


## Version 2.5 promotion decisions

Only completed evaluation jobs and eligible aggregates may enter a promotion dossier. Recommendations and authorizations are append-only governance records. Adapter registry mutation requires a separate release action with before/after snapshots, rollback instructions, stable-release QA, and documentation updates.
