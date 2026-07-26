# Adapter Registry Contract

## Registry Entry

Each adapter entry contains:

- `adapter_id`;
- `adapter_version`;
- `target_family`;
- `target_version_range`;
- `capability_profile`;
- `request_schema`;
- `result_schema`;
- `conformance_suite`;
- `status`.

## Stable Identity

Adapter identifiers are lowercase, namespaced, and stable. A breaking behavior change requires a major adapter version.

## Status Values

- `experimental`;
- `supported`;
- `deprecated`;
- `retired`.

Only `supported` adapters may be used for production release packages. Experimental adapters must label their result as non-production.

## Resolution

Registry resolution must select an exact adapter version. Floating or ambiguous resolution is prohibited in reproducible runs.
