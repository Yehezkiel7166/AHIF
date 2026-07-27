# Aggregation Governance Report Schema

```json
{
  "review_id": "agr.<date>.<revision>",
  "aggregate_id": "string",
  "recommendation_id": "string",
  "reviewers": ["string"],
  "checks": [{"check_id": "string", "result": "pass|fail|hold", "evidence": ["string"]}],
  "risk_summary": ["string"],
  "decision": "accepted|rejected|held",
  "adapter_status_change": "none|promotion_review|downgrade_review",
  "signed_at": "ISO-8601"
}
```

An accepted report authorizes use of the recommendation, not automatic adapter promotion.
