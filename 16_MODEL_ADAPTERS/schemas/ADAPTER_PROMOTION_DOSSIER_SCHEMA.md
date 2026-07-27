# Adapter Promotion Dossier Schema

```json
{
  "schema_version": "1.0.0",
  "dossier_id": "ahif:promotion-dossier:...",
  "scope_fingerprint": "sha256:<64 lowercase hex>",
  "policy_version": "2.5.0",
  "state": "draft|under_review|recommended|authorized|rejected|needs_revision|blocked|cancelled",
  "adapter": {
    "adapter_id": "string",
    "adapter_version": "string",
    "current_tier": "string",
    "requested_tier": "string"
  },
  "pinned_inputs": {
    "support_policy_version": "string",
    "promotion_gate_version": "string",
    "adapter_registry_version": "string",
    "evidence_cutoff": "string",
    "evaluation_job_ids": [],
    "aggregate_ids": []
  },
  "coverage": {
    "required_scenarios": 0,
    "accepted_scenarios": 0,
    "adverse_scenarios": 0,
    "missing_scenarios": []
  },
  "findings": {
    "identity": {},
    "semantics": {},
    "reproducibility": {},
    "drift": {},
    "blocking": []
  },
  "review": {
    "technical_reviewer_role": "string|null",
    "governance_reviewer_role": "string|null",
    "authorizing_role": "string|null",
    "separation_satisfied": false
  },
  "recommendation": "promote|hold|downgrade|block|null",
  "authorization": "accepted|rejected|null",
  "supersedes_dossier_id": "string|null",
  "events": [],
  "adapter_registry_changed": false
}
```

## Constraints

- every evaluation job must be completed and immutable;
- all adverse evidence within scope must be represented;
- exact governed versions and evidence cutoff are immutable after review begins;
- `recommended` requires completed technical and governance review;
- `authorized` requires accepted authorization and separation of duties;
- `adapter_registry_changed` must remain false inside the dossier lifecycle;
- a registry change requires a separate release action.
