# Reasoning Pipeline

## Input

The pipeline receives:

- normalized context
- canonical identity invariants
- knowledge graph evidence
- candidate and resolved decisions
- confidence data

## Execution sequence

1. **Premise registration** — record explicit and derived facts.
2. **Identity grounding** — attach non-negotiable identity constraints.
3. **Evidence binding** — connect decisions to source evidence.
4. **Causal evaluation** — verify why each decision follows.
5. **Alternative evaluation** — compare plausible options.
6. **Cross-domain validation** — detect incoherence between domains.
7. **Confidence propagation** — calculate domain and aggregate confidence.
8. **Uncertainty handling** — omit, neutralize, request, or block.
9. **Trace generation** — produce the explainable reasoning record.
10. **Compiler handoff** — emit ordered compiler directives.

## Blocking conditions

- canonical identity is unavailable
- identity confidence is below the identity floor
- a major decision lacks evidence
- unresolved decisions contradict each other
- a scene requires fabricated cultural or environmental facts
- compiler directives cannot form one coherent scene
