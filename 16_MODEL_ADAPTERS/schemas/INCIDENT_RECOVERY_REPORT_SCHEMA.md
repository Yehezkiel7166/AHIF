# Incident Recovery Report Schema

```json
{
  "schema_version": "1.0.0",
  "incident_id": "string",
  "recovery_path": "string",
  "declared_actions": [],
  "executed_actions": [],
  "pre_recovery_snapshot": "string",
  "post_recovery_snapshot": "string",
  "package_fingerprints": [],
  "contract_validation": [],
  "qa_result": "blocked",
  "rollback_reconstructable": false,
  "residual_risk": [],
  "validator_signoff": null,
  "authorizer_signoff": null,
  "claim_boundary": "No production-health certification is implied."
}
```
