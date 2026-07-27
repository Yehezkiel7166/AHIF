# Release Governance

## Purpose

This policy defines the release authority, evidence requirements, compatibility obligations, and rollback rules for stable AHIF releases.

## Release authority

A stable release is eligible only when all mandatory repository contracts pass:

1. canonical identity authority remains unchanged;
2. knowledge, decision, reasoning, compiler, QA, final-prompt, and adapter contracts are internally consistent;
3. all machine-readable schemas and registries validate;
4. no stable identifier is silently repurposed;
5. migration and compatibility documentation is complete;
6. unresolved critical failures are absent.

## Evidence classes

AHIF distinguishes three evidence classes:

- **Contract evidence** — schemas, registries, deterministic transformations, and regression fixtures.
- **Semantic evidence** — preservation of canonical intent across compiler and adapter outputs.
- **Empirical image evidence** — externally generated images evaluated against identity and visual-consistency criteria.

Stable AHIF core contracts require contract and semantic evidence. Empirical image evidence is required only for claims of image-output equivalence or production-certified model support.

## Release decision

The release decision must be machine-auditable and recorded in the release evidence register. Missing empirical evidence may not be converted into a positive image-parity claim.

## Rollback

A stable contract may be rolled back only when a critical identity, safety, or compatibility defect is confirmed. Rollback documentation must identify the affected contract, versions, migration impact, and replacement path.
