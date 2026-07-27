# Adapter Promotion Report Schema

```json
{
  "schema_version": "1.0",
  "report_id": "AHIF-APR-...",
  "adapter_id": "...",
  "adapter_version": "...",
  "current_tier": "contract_validated_experimental",
  "requested_tier": "empirically_validated_preview",
  "scenario_coverage": {
    "required": 0,
    "accepted": 0,
    "rejected": 0
  },
  "identity_summary": {},
  "semantic_summary": {},
  "reproducibility_summary": {},
  "blocking_findings": [],
  "decision": "hold",
  "decision_rationale": "",
  "evidence_bundle_ids": []
}
```

Permitted decisions are `promote`, `hold`, `downgrade`, and `block`.
