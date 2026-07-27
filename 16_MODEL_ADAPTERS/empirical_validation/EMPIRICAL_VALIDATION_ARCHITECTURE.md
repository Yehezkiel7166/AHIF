# Empirical Validation Architecture

## Purpose

The empirical validation subsystem records and evaluates externally generated image evidence without allowing unverified observations to modify canonical AHIF identity facts.

It extends the stable 2.0 contract-validation layer with an auditable evidence path:

```text
Released Final Prompt Package
→ Target Adapter Request
→ External Model Execution
→ Evidence Capture
→ Identity and Semantic Evaluation
→ Reproducibility Review
→ Adapter Promotion Decision
```

## Architectural boundary

The subsystem consumes generated-image evidence. It does not generate images, infer missing execution metadata, or claim target capability from documentation alone.

Canonical identity authority remains the master photo. Generated outputs are observations, never identity sources.

## Components

1. **Execution Record** — exact adapter, target, parameters, seed policy, timestamps, and prompt package identifiers.
2. **Evidence Bundle** — generated outputs, canonical-reference linkage, checksums, evaluator records, and environment metadata.
3. **Identity Evaluation** — structured comparison against canonical identity invariants.
4. **Semantic Evaluation** — comparison against the released prompt package and accepted variance policy.
5. **Reproducibility Review** — evidence that another qualified evaluator can repeat the execution.
6. **Promotion Gate** — determines whether an adapter remains experimental, becomes empirically validated, or is blocked.

## Authority order

1. Project Constitution
2. Canonical identity asset
3. Stable framework contracts
4. Released Final Prompt Package
5. Adapter capability profile
6. External execution record
7. Generated-image observations
8. Evaluator interpretation

Lower-authority evidence cannot override higher-authority constraints.

## Non-claims

The presence of an evidence bundle does not by itself prove:

- identity fidelity;
- semantic equivalence;
- deterministic image reproduction;
- production readiness;
- cross-model visual parity.

Those claims require the explicit promotion gates defined by this subsystem.
