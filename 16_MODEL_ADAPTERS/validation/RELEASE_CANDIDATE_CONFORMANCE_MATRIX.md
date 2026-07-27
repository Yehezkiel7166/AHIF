# Release-Candidate Conformance Matrix

## Scope

This matrix records Sprint 011 repository-level conformance. It does not claim that external image generation was executed.

| Adapter | Contract | Semantic | Deterministic request | Identity mapping | Loss disclosure | Empirical image evidence | RC2 status |
|---|---|---|---|---|---|---|---|
| OpenAI Images | Required | Required | Required | Required | Required | Pending | Contract validated, empirical pending |
| Midjourney | Required | Required | Required | Required | Required | Pending | Contract validated, empirical pending |
| SDXL/Diffusers | Required | Required | Required | Required | Required | Pending | Contract validated, empirical pending |

## Interpretation

`Contract validated` means repository contracts, fixtures, schemas, and expected blocking behavior are internally consistent. It does not mean generated images are equivalent or that adapters are production-ready.

## Promotion requirements

Before stable `2.0.0`, each declared stable adapter must have:

- current external execution evidence;
- identity preservation results meeting mandatory thresholds;
- degradation audit results without D3–D5 failures;
- reproducibility level declared;
- release regression pass;
- no unresolved critical or high-severity defect.
