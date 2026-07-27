# AHIF — Artificial Human Identity Framework

**Version:** 2.0.0-rc2
**Status:** Cross-Model Validation — Release Candidate 2
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

Version 2.0.0-rc2 adds formal cross-model validation to the identity-first pipeline. It freezes canonical inputs, validates deterministic adapter requests, audits semantic degradation, defines identity-preservation evidence, and prevents support claims from exceeding available evidence.

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
- `16_MODEL_ADAPTERS/` — adapter architecture, registry, profiles, serializers, mappings, compatibility contracts, and cross-model validation
- `docs/sprints/` — versioned sprint documentation
- `assets/identity-reference/` — canonical master-photo location

## Source of truth

The repository is the source of truth. AI context files are condensed operational views derived from canonical modules.

## Canonical identity rule

The uploaded master photo is the only canonical identity reference. Text may clarify the image but must never replace, reinterpret, or override it.

## Current release — 2.0.0-rc2

Sprint 011 establishes the Cross-Model Validation layer. It adds deterministic V0–V7 execution, exact evidence binding, identity-preservation comparison, degradation auditing, reproducibility levels, validation schemas, QA gates, and release-candidate regression fixtures. Repository-level contract and semantic validation are complete, while empirical generated-image evidence remains explicitly pending. All adapters remain experimental until the stable 2.0 release gate is satisfied.

The permanent architectural rules are defined in [`PROJECT_CONSTITUTION.md`](PROJECT_CONSTITUTION.md).
