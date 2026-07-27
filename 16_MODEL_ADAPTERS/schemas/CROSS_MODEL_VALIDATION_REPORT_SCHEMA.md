# Cross-Model Validation Report Schema

## Required fields

```json
{
  "schema_version": "1.0.0",
  "report_id": "AHIF-VAL-...",
  "framework_version": "2.0.0-rc2",
  "scenario_id": "...",
  "canonical_inputs": {
    "final_prompt_package_id": "...",
    "final_prompt_package_sha256": "...",
    "identity_asset_sha256": "...",
    "knowledge_registry_version": "..."
  },
  "adapters": [],
  "cross_adapter_findings": [],
  "validation_state": "contract_validated",
  "empirical_state": "pending",
  "release_eligibility": false,
  "generated_at": "UTC ISO 8601"
}
```

## Adapter result

Each adapter result contains exact adapter, serializer, and capability-profile versions; request hash; contract-gate results; semantic preservation results; degradation findings; identity evidence state; reproducibility level; failures; and release effect.

## Constraints

- `release_eligibility` is false when empirical validation required by the declared support level is missing.
- Identity-critical failure forces `validation_state: blocked`.
- Missing evidence is represented explicitly and never omitted.
- Hashes are lowercase SHA-256 hexadecimal values.
