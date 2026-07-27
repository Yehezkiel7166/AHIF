# Evidence Evaluation Workflow

## Purpose

Define the deterministic post-ingestion workflow for evaluating evidence records that have already been accepted by the governed ingestion pipeline.

Evaluation does not create evidence, alter canonical identity authority, or promote an adapter. It produces reviewable identity and semantic evaluation reports that may later become inputs to aggregation and promotion governance.

## Preconditions

An evaluation job may be created only when:

1. the evidence registry record exists and has state `accepted`;
2. artifact integrity is verified;
3. adapter, model, profile, serializer, scenario, and canonical package versions are pinned;
4. the canonical master-photo reference is resolvable;
5. no active job already owns the same record and evaluation scope.

## E0–E9 workflow

| Stage | Name | Required outcome |
|---|---|---|
| E0 | Resolve record | accepted registry record and immutable identifiers resolved |
| E1 | Freeze scope | identity, semantics, reproducibility, and reviewer requirements frozen |
| E2 | Validate artifacts | required artifacts and SHA-256 fingerprints rechecked |
| E3 | Create job | deterministic job identifier and queue event created |
| E4 | Identity evaluation | identity report produced under the canonical identity protocol |
| E5 | Semantic evaluation | required meanings, constraints, and losses evaluated |
| E6 | Reproducibility review | execution metadata classified using R0–R4 |
| E7 | Independent review | required reviewer decisions recorded without overwriting prior events |
| E8 | Resolve outcome | completed, needs-revision, blocked, or cancelled |
| E9 | Publish references | immutable report references attached to the registry record |

## State model

```text
queued
→ in_review
→ completed
| needs_revision
| blocked
| cancelled
```

Only `queued → in_review` and `in_review → completed|needs_revision|blocked|cancelled` are normal transitions. A `needs_revision` job is closed; remediation requires a new job linked through `supersedes_job_id`.

## Determinism

The same record, scope, policy version, evaluator configuration, and report inputs must resolve to the same outcome and failure codes. Human scores may differ, but every decision, comment, and amendment must be preserved as an append-only event.

## Separation of duties

- ingestion decides whether evidence may enter the registry;
- evaluation measures identity, semantic, and reproducibility properties;
- aggregation summarizes multiple accepted evaluations;
- promotion governance changes adapter support status.

No evaluation operation may update the adapter registry or target profile directly.

## Claim boundary

The repository baseline contains no external evidence, no queued evaluation jobs, and no empirical evaluation results.