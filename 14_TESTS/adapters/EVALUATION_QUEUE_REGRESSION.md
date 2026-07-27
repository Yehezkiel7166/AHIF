# Evaluation Queue Regression

## Baseline assertions

- queue schema version is `1.0.0`;
- policy version is `2.4.0`;
- `append_only_events` is true;
- `job_count` equals the length of `jobs`;
- repository baseline has zero jobs;
- no event contains secrets, absolute private paths, or adapter status changes.

## Transition regression

Allowed transitions:

```text
null → queued
queued → in_review
in_review → completed
in_review → needs_revision
in_review → blocked
in_review → cancelled
```

Every other transition is rejected unless a future policy version explicitly introduces it.