# Adapter Release Execution Protocol

## Purpose

Define the governed R0–R9 process that converts one authorized adapter promotion dossier into a reproducible adapter-registry release action.

A release action is the only Sprint 018 artifact permitted to propose a support-tier mutation. Authorization alone is insufficient. Execution requires immutable inputs, an approved plan, pre-change and post-change snapshots, stable-release QA, rollback readiness, and a signed result record.

## Preconditions

A release plan may be opened only when:

1. one promotion dossier exists in `authorized` state;
2. its recommendation is `promote` or `downgrade`;
3. the exact adapter and registry versions match the dossier scope;
4. no unresolved blocking finding, stale evidence cutoff, or superseding dossier exists;
5. release owner, independent approver, validator, and rollback owner roles are assigned;
6. no active release plan owns the same release-scope fingerprint.

## R0–R9 workflow

| Stage | Name | Required outcome |
|---|---|---|
| R0 | Resolve authorization | authorized dossier and recommendation verified |
| R1 | Freeze release scope | adapter, from-tier, to-tier, registry version, policies, and artifacts pinned |
| R2 | Capture pre-change snapshot | immutable registry and affected-file fingerprints recorded |
| R3 | Build release package | deterministic package manifest and migration record created |
| R4 | Validate candidate | contract, regression, compatibility, and claim-boundary checks pass |
| R5 | Approve execution | independent approver accepts the exact release fingerprint |
| R6 | Apply mutation | only declared files and fields are changed |
| R7 | Validate post-change state | snapshot, manifest, documentation, and support claims agree |
| R8 | Resolve outcome | completed, rolled_back, blocked, failed, or cancelled recorded |
| R9 | Publish release record | append-only event chain and signoff published |

## State model

```text
planned
→ candidate_ready
→ approved
→ executing
→ completed
| rolled_back
| blocked
| failed
| cancelled
```

`completed` is valid only after post-change validation and signoff. A failed validation after mutation must transition to `rolled_back` or remain `failed` with an explicit containment record.

## Mutation boundary

- only the paths declared in the package manifest may change;
- the adapter registry tier may change only from the pinned `from_tier` to `to_tier`;
- canonical identity authority, stable framework contracts, and unrelated adapters are immutable;
- an authorization cannot be reused for another adapter version, model snapshot, or target tier;
- all release events and amendments are append-only.

## Baseline boundary

AHIF 2.6.0 defines the execution mechanism only. The baseline includes zero release plans, approvals, executions, rollbacks, and adapter-tier changes.
