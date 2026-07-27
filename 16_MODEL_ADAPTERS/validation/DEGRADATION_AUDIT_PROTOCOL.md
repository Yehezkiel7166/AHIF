# Degradation Audit Protocol

## Purpose

Detect and classify semantic or control loss introduced between the canonical Final Prompt Package and a target-model request or output.

## Degradation classes

- `D0 none` — no material loss;
- `D1 representational` — syntax changes while meaning is preserved;
- `D2 controllability` — a non-critical control becomes approximate;
- `D3 semantic` — a required non-identity semantic is weakened;
- `D4 identity_critical` — identity binding or preservation is weakened;
- `D5 undisclosed` — any loss absent from the transformation record.

## Audit domains

Identity reference, scene anchor, activity, pose and gesture, styling, environment interaction, camera and composition, lighting and color, realism controls, negative constraints, reproducibility controls, and output metadata.

## Rules

- D1 is acceptable when disclosed.
- D2 requires a mitigation and confidence adjustment.
- D3 blocks the affected adapter unless the canonical package marks the semantic optional.
- D4 always blocks.
- D5 always blocks and is a conformance defect.

## Audit record

Every finding includes source directive, target representation, degradation class, evidence, mitigation, residual risk, release effect, and responsible adapter stage.

## Cross-adapter interpretation

Different targets may use different mechanisms. Mechanism variance is not degradation when canonical meaning and identity safety are preserved.
