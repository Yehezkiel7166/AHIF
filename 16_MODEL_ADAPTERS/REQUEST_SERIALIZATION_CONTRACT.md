# Target Request Serialization Contract

## Required Inputs

A serializer accepts:

- release-eligible Final Prompt Package;
- exact adapter identifier and version;
- exact capability profile version;
- approved adapter configuration;
- canonical identity asset reference metadata;
- deterministic run identifier.

## Required Output

The serializer emits:

- `target_family`;
- `target_request`;
- `semantic_map`;
- `parameter_map`;
- `loss_report`;
- `identity_preservation_status`;
- `source_package_hash`;
- `adapter_configuration_hash`;
- `adapter_status`.

## Serialization Rules

1. Preserve the canonical positive prompt meaning before optimization.
2. Keep identity reference binding explicit when the target accepts image input.
3. Translate negative constraints only through declared target mechanisms.
4. Separate textual prompt content from execution parameters.
5. Never inject undocumented target defaults into the canonical record.
6. Record target defaults that may affect reproducibility.
7. Reject unknown parameters instead of forwarding them.
8. Use stable field ordering in machine-readable output.

## Blocking Conditions

Serialization fails closed when the source package is not release eligible, the selected profile is missing, the identity asset is required but unavailable, or a target limitation would remove an identity-critical constraint.
