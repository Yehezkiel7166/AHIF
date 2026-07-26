# Adapter Capability Model

## Capability Domains

Each target profile declares support for:

- identity reference input;
- textual identity constraints;
- negative prompting;
- weighted directives;
- regional prompting;
- seed control;
- aspect-ratio control;
- camera and lens semantics;
- lighting semantics;
- style references;
- image-to-image strength;
- character consistency features;
- structured request parameters.

## Support Levels

| Level | Meaning |
|---|---|
| `native` | Direct target-model support exists. |
| `translated` | Equivalent syntax or parameter mapping exists. |
| `emulated` | Approximation is possible through approved composition. |
| `unsupported` | No reliable representation exists. |
| `unknown` | Capability has not been verified. |

`unknown` must never be treated as supported.

## Criticality

Capabilities are classified as:

- `identity_critical`;
- `semantic_required`;
- `quality_optional`.

Unsupported identity-critical capability requirements block release. Unsupported quality-optional features may produce a degraded result if the loss is recorded.

## Versioning

Capability profiles are immutable after release. Corrections require a new profile version so prior adapter results remain reproducible.
