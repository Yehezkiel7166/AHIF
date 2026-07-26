# Architecture

AHIF has nine logical layers:

1. **Canonical Identity** — immutable identity rules
2. **Character Brain** — personality, habits, preferences
3. **Knowledge Layer** — location, climate, culture, activities
4. **Decision Engine** — proposes decisions and resolves conflicts
5. **Reasoning Engine** — binds evidence, verifies causal coherence, evaluates alternatives, and propagates confidence
6. **Reality Simulation** — anatomy, physics, behavior
7. **Visual Direction** — fashion, camera, lighting, composition
8. **Prompt Compiler** — converts compiler-ready reasoning into a final prompt
9. **Quality Assurance** — applies deterministic linting, mandatory gates, failure classification, recovery orchestration, and release control

## Processing sequence

```text
User input
→ Context parser
→ Canonical identity constraints
→ Knowledge graph grounding
→ Decision inference and conflict resolution
→ Reasoning and evidence validation
→ Human, styling, camera, lighting, and story coherence
→ Prompt compilation
→ QA validation
→ Final prompt
```

## Architectural rule

The Prompt Compiler must not invent material decisions. It consumes only decisions accepted by the Reasoning Engine.
