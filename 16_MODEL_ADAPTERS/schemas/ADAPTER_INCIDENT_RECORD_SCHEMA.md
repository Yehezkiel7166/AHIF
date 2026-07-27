# Adapter Incident Record Schema

```json
{
  "schema_version": "1.0.0",
  "incident_id": "AHIF-INC-YYYY-NNNN",
  "status": "opened",
  "severity": "SEV-4",
  "scope_fingerprint": "sha256:<hex>",
  "adapter_id": "string",
  "release_execution_id": "string",
  "observation_id": "string",
  "declared_findings": [],
  "affected_contracts": [],
  "containment_plan": [],
  "recovery_path": "blocked_insufficient_evidence",
  "roles": {
    "incident_commander": "unassigned",
    "technical_responder": "unassigned",
    "governance_reviewer": "unassigned",
    "validator": "unassigned",
    "authorizer": "unassigned"
  },
  "events": [],
  "residual_risk": "unassessed",
  "created_at": "RFC3339",
  "closed_at": null
}
```

All real identifiers, actors, timestamps, signals, and actions must come from user-provided or externally executed records.
