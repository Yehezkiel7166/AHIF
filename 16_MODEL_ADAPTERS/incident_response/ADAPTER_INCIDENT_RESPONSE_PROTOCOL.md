# Adapter Incident Response Protocol

## Purpose

This protocol governs incident handling after a completed adapter release has entered observation. It converts an authorized observation response into a bounded, auditable incident process without fabricating telemetry, executing undeclared rollback, or mutating adapter support tiers.

## Entry requirements

An incident may be opened only when all of the following are pinned:

- a completed and signed release execution record;
- an active or completed observation record;
- one or more declared signals or repository-conformance findings;
- the exact adapter, source profile, target profile, release package, and snapshots;
- incident commander, technical responder, governance reviewer, validator, and authorizer roles;
- an immutable incident scope fingerprint.

Missing external telemetry is represented as `unavailable`; it must never be inferred.

## IR0–IR9 workflow

| Stage | Name | Required outcome |
|---|---|---|
| IR0 | Intake | Validate provenance and prevent duplicate incident scope. |
| IR1 | Classification | Assign bounded severity and affected contract surfaces. |
| IR2 | Containment planning | Declare reversible containment actions and forbidden mutations. |
| IR3 | Authorization | Obtain independent authorization for the exact response set. |
| IR4 | Containment verification | Verify that declared containment can be reconstructed and reverted. |
| IR5 | Recovery planning | Select restore, rollback, forward-fix, hold, or no-action path. |
| IR6 | Recovery execution record | Record externally executed actions; AHIF does not execute deployment. |
| IR7 | Validation | Compare signed snapshots, contracts, QA, and declared signals. |
| IR8 | Resolution review | Confirm residual risk, follow-up ownership, and claim boundaries. |
| IR9 | Closure | Append immutable signoff and link lessons-learned actions. |

## Severity model

- `SEV-0`: confirmed canonical identity authority corruption or unrecoverable release-chain integrity loss;
- `SEV-1`: material adapter contract break with broad release impact;
- `SEV-2`: bounded compatibility or serialization regression;
- `SEV-3`: documentation, metadata, or non-executing governance defect;
- `SEV-4`: observation requiring investigation but no confirmed defect.

Severity is not a production-health claim. It applies only to the declared AHIF scope.

## Permitted outcomes

- `restore_from_snapshot`
- `rollback_authorized_release`
- `forward_fix_candidate`
- `hold_adapter_profile`
- `no_action_required`
- `blocked_insufficient_evidence`

## Hard boundaries

Incident handling does not automatically:

- execute rollback or deployment;
- mutate adapter tiers or canonical identity authority;
- create empirical evidence records;
- certify production health or service availability;
- authorize undeclared files, parameters, or environments;
- erase adverse findings or prior append-only events.
