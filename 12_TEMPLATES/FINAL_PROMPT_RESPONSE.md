# Final Prompt Response

A successful response contains:

```text
Status: released | released_with_warnings
Framework version: <version>

Final prompt:
<validated model-neutral prompt>

Negative constraints:
<risk-derived constraints>

Explainable summary:
<identity status, normalized context, selected decisions, concise rationale, confidence, QA result>

Validation:
<mandatory gates, warnings, recovery history, release eligibility>
```

A blocked response must omit a production-ready final prompt and state the failure codes, earliest failing stage, and required recovery action.
