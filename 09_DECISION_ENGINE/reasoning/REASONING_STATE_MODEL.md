# Reasoning State Model

## State definition

A reasoning state is the complete, versioned record used to evaluate one requested scene.

## Required fields

| Field | Purpose |
|---|---|
| `request_context` | Normalized location, place, atmosphere, time, weather, and activity inputs |
| `identity_invariants` | Canonical constraints that cannot be traded away |
| `knowledge_evidence` | Graph nodes and relationships supporting the scene |
| `candidate_decisions` | Decisions emitted by the inference pipeline |
| `resolved_decisions` | Decisions retained after conflict resolution |
| `reasoning_chains` | Causal explanations for retained decisions |
| `rejected_alternatives` | Plausible options not selected and the rejection reason |
| `confidence` | Domain and aggregate confidence |
| `uncertainties` | Missing or ambiguous facts that remain material |
| `compiler_directives` | Ordered instructions for prompt compilation |
| `qa_flags` | Conditions requiring validation or blocking output |

## State transitions

```text
INITIALIZED
→ GROUNDED
→ EVALUATED
→ RESOLVED
→ EXPLAINED
→ COMPILER_READY
```

A state becomes `BLOCKED` when identity safety, causal coherence, or minimum confidence fails.

## Transition rules

### INITIALIZED → GROUNDED

Requires normalized context and canonical identity availability.

### GROUNDED → EVALUATED

Requires evidence for every material candidate decision. Unsupported candidates are removed or marked uncertain.

### EVALUATED → RESOLVED

Requires conflict resolution and rule-priority compliance.

### RESOLVED → EXPLAINED

Requires a causal chain for every major visual decision.

### EXPLAINED → COMPILER_READY

Requires no blocking QA flag and a complete compiler directive set.

## Determinism

Given the same canonical identity, normalized context, knowledge version, and rule version, the engine should produce materially equivalent reasoning. Controlled variation may occur only in non-identity details explicitly classified as interchangeable.
