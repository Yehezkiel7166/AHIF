# QA Pipeline

## Execution sequence

```text
Ingest QA package
→ Validate package completeness
→ Run deterministic prompt lint
→ Run identity gate
→ Run anatomy and physics gate
→ Run context and cultural gate
→ Run camera, lighting, and environment coherence gate
→ Run compiler integrity gate
→ Classify findings
→ Calculate category and aggregate scores
→ Select recovery route
→ Revalidate repaired artifact
→ Emit QA report and release decision
```

## Stage 1 — Package validation

Reject incomplete packages that omit the canonical identity lock, reasoning status, compiler metadata, compiled prompt, or negative constraints.

## Stage 2 — Prompt lint

Apply stable lint rules to detect omissions, contradictions, duplication, unsafe beautification, weak identity language, impossible physical instructions, and unsupported model-specific syntax.

## Stage 3 — Domain gates

Run domain-specific validators independently. A passing aggregate score cannot override a mandatory gate failure.

## Stage 4 — Finding classification

Each finding requires:

- stable code
- severity
- affected component
- evidence
- violated rule
- repairability
- recommended action

## Stage 5 — Scoring

Calculate category scores only after mandatory gates. Use scores to prioritize refinement, not to waive identity or anatomy requirements.

## Stage 6 — Recovery

Route repairable findings to the smallest safe repair action. Do not regenerate the entire prompt when a local deterministic correction is sufficient.

## Stage 7 — Revalidation

Every repaired artifact must rerun all affected gates and all upstream invariants that the repair could influence.

## Stage 8 — Release decision

A final prompt is release-eligible only when all blocking findings are closed and the QA report is complete.
