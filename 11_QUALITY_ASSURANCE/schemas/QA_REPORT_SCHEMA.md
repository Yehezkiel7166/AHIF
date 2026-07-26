# QA Report Schema

## JSON shape

```json
{
  "qa_report_id": "qa_<stable-id>",
  "framework_version": "1.5.0",
  "input_fingerprint": "sha256:<digest>",
  "status": "pass",
  "release_eligible": true,
  "mandatory_gates": {
    "identity": "pass",
    "anatomy_physics": "pass",
    "context_culture": "pass",
    "compiler_integrity": "pass",
    "output_contract": "pass"
  },
  "scores": {
    "identity_fidelity": 100,
    "anatomy_physics": 95,
    "context_environment": 92,
    "cultural_appropriateness": 95,
    "photography_lighting": 90,
    "styling_continuity": 90,
    "story_coherence": 88,
    "compiler_integrity": 96,
    "output_completeness": 100,
    "aggregate": 94
  },
  "findings": [],
  "repairs": [],
  "validation_provenance": []
}
```

## Validation rules

- unknown status values are invalid
- identity gate must pass for release eligibility
- aggregate must equal the weighted score calculation
- every finding must contain a stable code and evidence
- every applied repair must reference its originating finding
- reports with missing provenance are not release-eligible
