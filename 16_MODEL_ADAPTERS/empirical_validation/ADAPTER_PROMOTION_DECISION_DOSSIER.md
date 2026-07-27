# Adapter Promotion Decision Dossier

## Purpose

Define the governed P0–P9 process that converts completed evidence evaluations and eligible aggregates into an auditable adapter-tier decision proposal.

A dossier is a decision record, not an automatic status mutation. It may recommend promotion, hold, downgrade, or block, but the adapter registry changes only through a separately authorized release-governance action.

## Preconditions

A dossier may be opened only when:

1. every referenced evaluation job exists and is `completed`;
2. every referenced evidence record remains `accepted`;
3. required aggregate and drift reports are present for the requested decision scope;
4. adapter, model, capability-profile, policy, registry, and support-policy versions are pinned;
5. adverse evidence is included rather than filtered out;
6. no active dossier already owns the same decision-scope fingerprint.

## P0–P9 workflow

| Stage | Name | Required outcome |
|---|---|---|
| P0 | Resolve candidate | exact adapter version and current support tier resolved |
| P1 | Freeze decision scope | requested tier, scenario coverage, policies, and evidence cutoff frozen |
| P2 | Verify evaluation set | completed jobs and immutable report links verified |
| P3 | Verify aggregation | eligibility, cohort integrity, confidence, outlier, and drift checks passed |
| P4 | Build dossier | deterministic dossier ID and scope fingerprint created |
| P5 | Risk review | blocking findings, adverse evidence, and unsupported claims recorded |
| P6 | Governance review | technical and governance reviewers record independent decisions |
| P7 | Resolve recommendation | promote, hold, downgrade, or block recommendation produced |
| P8 | Authorize decision | designated authority accepts or rejects the recommendation |
| P9 | Publish decision record | immutable decision record and release-action boundary published |

## State model

```text
draft
→ under_review
→ recommended
→ authorized
| rejected
| needs_revision
| blocked
| cancelled
```

Normal transitions are `draft → under_review`, `under_review → recommended|needs_revision|blocked|cancelled`, and `recommended → authorized|rejected|needs_revision`.

An `authorized` dossier still does not edit the adapter registry. Registry mutation requires an explicit release record that references the authorized dossier, updates support policy evidence, passes stable-release QA, and preserves rollback information.

## Decision rules

- `promote` requires all mandatory dimensions to meet the requested tier threshold, adequate scenario coverage, no identity-critical failure, no unresolved drift, and independent authorization.
- `hold` preserves the current tier when evidence is insufficient, mixed, stale, or below threshold without requiring downgrade.
- `downgrade` is appropriate when accepted adverse evidence invalidates the current support claim.
- `block` applies when integrity, provenance, reviewer independence, or claim-boundary requirements fail.

## Separation of duties

- evaluators may not be the sole authorizing authority;
- dossier authors may assemble evidence but may not overwrite evaluation reports;
- governance reviewers must disclose role conflicts;
- release maintainers may apply an authorized decision but may not invent missing evidence;
- no stage may alter canonical identity authority.

## Determinism and immutability

The same pinned inputs, evidence cutoff, policy versions, and reviewer decisions must resolve to the same recommendation and failure codes. Events and amendments are append-only. A material scope change requires a new dossier linked with `supersedes_dossier_id`.

## Claim boundary

This repository defines the governance mechanism only. The baseline contains no real completed evaluation jobs, promotion dossiers, authorizations, or adapter-tier changes.
