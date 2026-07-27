# Identity Comparison Report Schema

## Required fields

```json
{
  "schema_version": "1.0.0",
  "comparison_id": "AHIF-IDCMP-...",
  "identity_asset_sha256": "...",
  "output_asset_sha256": "...",
  "adapter_binding": {
    "adapter_id": "...",
    "adapter_version": "...",
    "capability_profile_version": "..."
  },
  "risk_annotations": {},
  "dimension_scores": {
    "face_silhouette": 0.0,
    "eye_system": 0.0,
    "central_proportions": 0.0,
    "lower_face": 0.0,
    "age_presentation": 0.0,
    "ethnicity_presentation": 0.0,
    "recognizability": 0.0
  },
  "identity_score": 0.0,
  "evidence_mode": "human_review",
  "evidence_quality": "sufficient",
  "findings": [],
  "status": "pass"
}
```

## Validation rules

- `identity_score` equals the minimum mandatory dimension score.
- `pass` requires all identity thresholds and no critical drift finding.
- Output evidence must resolve and match its declared hash.
- `not_evaluated` is mandatory when no generated output exists.
