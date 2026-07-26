# AHIF — Artificial Human Identity Framework

**Version:** 1.3.0  
**Status:** Reasoning Engine Release  
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
```

The Reasoning Engine introduced in version 1.3.0 verifies why each decision is valid, records evidence and alternatives, propagates confidence, and blocks identity-unsafe or incoherent scenes before compilation.

## Daily use

1. Upload the canonical master photo to the image generator.
2. Upload `00_CONTEXT/AHIF_AI_CONTEXT.md` to ChatGPT.
3. Ask ChatGPT to load the framework.
4. Provide a compact request such as:

```text
Location: Kyoto, Japan
Place: Gion district
Atmosphere: calm autumn morning
Output: final image-generation prompt
```

5. AHIF normalizes context, resolves decisions, produces an explainable reasoning result, compiles one coherent prompt, and validates the result.

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
- `09_DECISION_ENGINE/` — context, knowledge graph, inference, resolution, and reasoning
- `10_PROMPT_COMPILER/` — prompt assembly and machine-readable handoff schemas
- `11_QUALITY_ASSURANCE/` — identity, decision, reasoning, and final validation
- `12_TEMPLATES/` — reusable input and output templates
- `13_EXAMPLES/` — worked examples
- `14_TESTS/` — identity, decision, reasoning, and prompt regression tests
- `docs/sprints/` — versioned sprint documentation
- `assets/identity-reference/` — canonical master-photo location

## Source of truth

The repository is the source of truth. AI context files are condensed operational views derived from the canonical modules.

## Canonical identity rule

The uploaded master photo is the only canonical identity reference. Text may clarify the image but must never replace, reinterpret, or override it.
