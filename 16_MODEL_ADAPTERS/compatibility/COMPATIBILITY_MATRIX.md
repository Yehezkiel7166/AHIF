# Adapter Compatibility Matrix

## Scope

This matrix evaluates the experimental adapters introduced in version 1.8.0 against the canonical AHIF Final Prompt Package contract.

| Capability | OpenAI Images v1 | Midjourney v1 | SDXL Diffusers v1 | Canonical requirement |
|---|---|---|---|---|
| Positive prompt semantics | Native structured prompt | Prompt text | Positive prompt | Required |
| Negative constraints | Embedded instruction contract | `--no` mapping where supported plus disclosure | Negative prompt | Critical |
| Canonical image reference | Request image/reference surface | Character/image-reference surface | Image-conditioning surface | Critical |
| Aspect ratio | Request size/aspect mapping | Native aspect parameter | Width/height mapping | Required |
| Seed control | Profile-dependent | Profile-dependent | Native pipeline parameter | Optional and disclosed |
| Guidance control | Profile-dependent | Not equivalent; declared loss | Native guidance parameter | Quality |
| Sampler control | Not exposed in canonical adapter | Not exposed | Native scheduler mapping | Optional |
| Deterministic request serialization | Required | Required | Required | Critical |
| Loss disclosure | Required | Required | Required | Critical |
| Identity-critical block behavior | Required | Required | Required | Critical |

## Interpretation

The matrix records representational capability, not guaranteed pixel-level output equivalence. Rendering results remain model-dependent. AHIF compatibility requires preserved canonical meaning, traceability, and identity-safe failure behavior.

## Promotion Status

All three adapters remain `experimental` in version 1.9.0. Sprint 009 establishes the contracts and comparison evidence required for later cross-model validation; it does not claim empirical image-output parity.
