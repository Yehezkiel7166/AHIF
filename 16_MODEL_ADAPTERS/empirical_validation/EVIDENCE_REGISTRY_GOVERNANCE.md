# Evidence Registry Governance

## Registry model

The registry is an append-only index of evidence decisions. It stores metadata and references, not canonical identity authority.

## Required record fields

- stable `record_id`;
- immutable `bundle_id` and `execution_id`;
- adapter and model versions;
- ingestion status and reason codes;
- artifact fingerprints;
- provenance summary;
- linked evaluation reports;
- policy version and decision timestamp;
- optional supersedes/superseded-by relationship.

## Stable identifiers

`record_id` format:

```text
ahif-evidence-record:<adapter-id>:<execution-id>:<digest-prefix>
```

Identifiers are never recycled.

## Mutation policy

Registry history is append-only. A factual correction must:

1. create a new record;
2. reference the prior record using `supersedes`;
3. preserve the original record;
4. state the correction reason.

## Status transitions

Allowed transitions are represented as new events:

```text
quarantined → accepted
quarantined → rejected
accepted → revoked
accepted → superseded
```

No transition changes an adapter support tier automatically.

## Human review

Human review is mandatory when:

- provenance cannot be independently verified;
- identity evaluation is near a policy threshold;
- model or adapter version drift is detected;
- artifacts contain inconsistent metadata;
- a record would materially affect a target-profile recommendation.

## Privacy and minimization

Store only evidence needed for reproducibility and governance. Do not embed secrets, account credentials, private API tokens, or unnecessary personal metadata.