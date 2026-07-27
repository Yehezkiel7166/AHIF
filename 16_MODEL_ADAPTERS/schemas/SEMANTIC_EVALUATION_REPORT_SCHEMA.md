# Semantic Evaluation Report Schema

```json
{
  "schema_version": "1.0",
  "report_id": "AHIF-SER-...",
  "bundle_id": "AHIF-EVB-...",
  "domains": {
    "location_place": {"status": "pass", "variance": [], "findings": []},
    "atmosphere_weather": {"status": "pass", "variance": [], "findings": []},
    "fashion_styling": {"status": "pass", "variance": [], "findings": []},
    "pose_expression_activity": {"status": "pass", "variance": [], "findings": []},
    "photography": {"status": "pass", "variance": [], "findings": []},
    "story": {"status": "pass", "variance": [], "findings": []},
    "negative_constraints": {"status": "pass", "variance": [], "findings": []}
  },
  "undisclosed_losses": [],
  "blocking_findings": [],
  "overall_status": "pass",
  "confidence": 0.0,
  "recommendation": "accept"
}
```

The report must reference the compatibility tolerance applicable to each accepted variance.
