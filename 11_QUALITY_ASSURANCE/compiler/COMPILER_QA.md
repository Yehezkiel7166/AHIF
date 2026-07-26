# Prompt Compiler QA

## Scope

This gate validates compiler behavior before full Quality Assurance Engine hardening in version 1.5.

## Required checks

- accepted reasoning input only
- canonical identity lock present and first
- deterministic section order
- no unsupported material facts
- no unresolved contradictions
- one dominant activity
- one dominant story beat
- coherent camera, composition, and lighting
- context-aware styling
- relevant negative constraints
- complete metadata and provenance references

## Result

```yaml
status: pass|revise|fail
failures: []
warnings: []
```

`fail` is mandatory for missing identity lock, blocked reasoning input, invented material facts, or concealed contradictions.
