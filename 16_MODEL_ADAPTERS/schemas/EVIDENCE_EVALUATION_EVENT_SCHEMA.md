# Evidence Evaluation Event Schema

```json
{
  "schema_version": "1.0.0",
  "event_id": "string",
  "job_id": "string",
  "sequence": 1,
  "event_type": "job_created|review_started|report_attached|finding_recorded|review_approved|revision_required|job_blocked|job_cancelled|job_completed|amendment",
  "prior_state": "null|queued|in_review|completed|needs_revision|blocked|cancelled",
  "next_state": "queued|in_review|completed|needs_revision|blocked|cancelled",
  "actor_role": "string",
  "policy_version": "2.4.0",
  "content_fingerprint": "sha256:<64 lowercase hex>",
  "references": ["repository-relative path or stable record id"],
  "amends_event_id": "string|null",
  "notes": "string|null"
}
```

Events are ordered by `sequence`. An amendment may clarify a prior event but must not erase it.