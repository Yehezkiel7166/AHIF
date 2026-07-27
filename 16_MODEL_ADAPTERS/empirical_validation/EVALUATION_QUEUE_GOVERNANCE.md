# Evaluation Queue Governance

## Queue authority

`16_MODEL_ADAPTERS/empirical_validation/queue/EVALUATION_QUEUE.json` is the machine-readable baseline for post-ingestion evaluation jobs. It is append-only at the event level and contains zero jobs in the repository release.

## Job identity

A job identifier must be stable and unique. Recommended form:

```text
ahif:eval:<record-id>:<scope-hash-prefix>
```

The scope hash is calculated from the canonical serialization of the record identifier, requested evaluation dimensions, policy version, evaluator configuration, and report schema versions.

## Duplicate control

A new job is rejected as a duplicate when an active or completed job has the same scope fingerprint. A replacement job is allowed only when it declares `supersedes_job_id` and changes at least one governed input.

## Append-only events

Each job stores ordered events. Existing events must never be edited or deleted. Corrections are represented by later amendment events that identify the corrected event.

Required event fields:

- event identifier;
- job identifier;
- event type;
- prior and next state;
- actor role;
- timestamp or declared offline sequence;
- policy version;
- content fingerprint.

## Reviewer independence

Where independent review is required, the same actor may not submit both the primary evaluation and the independent approval. Repository documentation may define roles, but it must not invent reviewer identities.

## Privacy and minimization

Store stable actor roles or pseudonymous identifiers rather than unnecessary personal information. Do not place secrets, provider credentials, or private filesystem paths in queue events.

## Adapter boundary

Queue completion does not promote, downgrade, or certify an adapter. Promotion remains governed by `ADAPTER_PROMOTION_GATE.md`.