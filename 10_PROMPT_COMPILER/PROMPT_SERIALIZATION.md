# Prompt Serialization

## Output package

```yaml
status: compiled|revision-required|blocked
schema_version: "1.0"
compiler_version: "1.4.0"
scene_id: string
final_prompt: string
negative_constraints: string
section_map: []
source_reasoning_chains: []
qa_handoff: {}
```

## Rendering requirements

- use complete, readable visual instructions
- preserve one coherent point of view
- keep identity lock explicit and early
- express physical relationships, not disconnected adjectives
- keep camera and lighting technically compatible
- avoid internal IDs, scores, or reasoning explanations in the visible prompt
- preserve metadata outside the visible prompt

## Output profiles

Version 1.4 defines one model-neutral profile:

- `neutral-still-image-v1`

Model-specific syntax, weighting, token conventions, and parameter adapters remain deferred to version 2.0.
