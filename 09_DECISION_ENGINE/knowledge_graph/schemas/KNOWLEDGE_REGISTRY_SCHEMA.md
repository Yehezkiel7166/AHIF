# Knowledge Registry Schema

The knowledge registry publishes every machine-readable package available to AHIF.

Required fields:

- `registry_version`
- `generated_for_release`
- `schema_version`
- `packages`

Each package entry must contain:

- `package_id`
- `domain`
- `version`
- `status`
- `path`
- `canonical_sources`
- `record_count`
- `consumer_scopes`

Registry entries must resolve to existing files. Duplicate package identifiers or paths are blocking errors.
