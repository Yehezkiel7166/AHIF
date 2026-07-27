# Identity Evaluation Report Schema

```json
{
  "schema_version": "1.0",
  "report_id": "AHIF-IDR-...",
  "bundle_id": "AHIF-EVB-...",
  "evaluator": {
    "type": "human",
    "id": "..."
  },
  "dimensions": {
    "facial_geometry": {"status": "pass", "confidence": 0.0, "notes": ""},
    "eye_structure": {"status": "pass", "confidence": 0.0, "notes": ""},
    "nose_mouth_structure": {"status": "pass", "confidence": 0.0, "notes": ""},
    "age_continuity": {"status": "pass", "confidence": 0.0, "notes": ""},
    "ethnicity_continuity": {"status": "pass", "confidence": 0.0, "notes": ""},
    "skin_tone_continuity": {"status": "pass", "confidence": 0.0, "notes": ""},
    "characteristic_features": {"status": "pass", "confidence": 0.0, "notes": ""},
    "generic_model_substitution": {"status": "pass", "confidence": 0.0, "notes": ""}
  },
  "blocking_findings": [],
  "overall_status": "pass",
  "recommendation": "accept"
}
```

`confidence` ranges from `0.0` to `1.0`. A report cannot recommend acceptance when a blocking finding exists.
