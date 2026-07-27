# Release Execution Registry Governance

## Purpose

Maintain an append-only index of adapter release plans and execution outcomes.

## Registry properties

- zero or more release records;
- unique `release_id` and `release_scope_fingerprint`;
- immutable authorization and pre-change snapshot references;
- append-only events ordered by sequence;
- explicit approval, execution, validation, rollback, and signoff status;
- no deletion or rewriting of failed, blocked, cancelled, or rolled-back history.

## Duplicate control

Only one active release may own the same adapter version, target tier, authorized dossier, and pre-change registry fingerprint. A duplicate must be cancelled with `AHIF-REL-012`.

## Mutation recording

A completed record must list every changed path, previous fingerprint, resulting fingerprint, validation result, and final registry tier. The record must never imply production support beyond the evidence and tier authorized by the source dossier.

## Baseline

`registry/RELEASE_EXECUTION_REGISTRY.json` intentionally contains zero records in AHIF 2.6.0.
