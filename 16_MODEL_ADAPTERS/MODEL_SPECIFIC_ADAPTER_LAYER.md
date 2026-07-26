# Model-Specific Adapter Layer

## Purpose

The Model-Specific Adapter Layer implements versioned translations from the canonical `Final Prompt Package` into target execution requests. It operationalizes the architecture defined in Sprint 007 while keeping AHIF decisions model-neutral and identity-first.

## Initial Adapter Set

| Adapter ID | Target family | Status | Primary surface |
|---|---|---|---|
| `ahif.openai-images.v1` | OpenAI Images | `experimental` | structured API request |
| `ahif.midjourney.v1` | Midjourney | `experimental` | prompt plus parameters |
| `ahif.sdxl-diffusers.v1` | SDXL through Diffusers | `experimental` | pipeline invocation object |

Experimental status means the adapter is executable as a documented contract but is not yet approved for production release equivalence.

## Processing Stages

```text
Final Prompt Package
→ Exact Adapter Resolution
→ Capability Snapshot Validation
→ Semantic Mapping
→ Parameter Mapping
→ Request Serialization
→ Loss Disclosure
→ Adapter QA
→ Adapter Result
```

## Invariants

- Canonical identity directives are never weakened silently.
- Unsupported identity-critical requirements produce `blocked`.
- Target parameters may refine delivery but may not invent visual decisions.
- Every omitted, translated, emulated, or degraded field is recorded.
- Adapter output is reproducible from package hash, adapter version, profile version, and configuration hash.
- External target capabilities are represented as date-stamped snapshots rather than timeless assumptions.

## Release Boundary

Sprint 008 introduces experimental target adapters. Production support remains blocked until Sprint 009 defines cross-model semantic equivalence and compatibility contracts.
