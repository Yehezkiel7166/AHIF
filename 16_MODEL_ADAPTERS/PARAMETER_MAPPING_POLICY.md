# Parameter Mapping Policy

## Mapping Classes

| Class | Meaning |
|---|---|
| `direct` | Canonical value maps to a native target parameter. |
| `derived` | Target value is deterministically derived from canonical context. |
| `serialized` | Canonical meaning is expressed in prompt syntax. |
| `omitted_optional` | Optional feature is unavailable and disclosed. |
| `blocked` | Required meaning cannot be preserved. |

## Governed Parameters

Adapters may map aspect ratio, output dimensions, quality mode, seed, variation, negative guidance, reference strength, style strength, guidance scale, inference steps, and target model version only when the capability profile declares them.

## No Hidden Tuning

An adapter must not choose aesthetic tuning values merely to improve beauty. Defaults must be either target-native documented defaults or AHIF-governed deterministic values justified by identity preservation, realism, or context fidelity.

## Version Sensitivity

A parameter mapping belongs to one adapter version and one target capability snapshot. Changed target behavior requires a new profile and, when behavior is breaking, a new adapter major version.
