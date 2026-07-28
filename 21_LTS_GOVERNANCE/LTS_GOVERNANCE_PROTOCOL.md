# LTS Governance Protocol

## Purpose

Define the deterministic LTS0–LTS9 lifecycle for designating, maintaining, validating, and retiring an AHIF long-term-support line. An LTS designation is a repository governance commitment; it is not evidence of deployment, adoption, operational availability, or production support.

## Workflow

| Stage | Name | Required outcome |
|---|---|---|
| LTS0 | Candidate scope | The candidate version, supported surfaces, exclusions, and compatibility baseline are pinned. |
| LTS1 | Artifact inventory | Canonical modules, schemas, registries, tests, and documentation are enumerated. |
| LTS2 | Compatibility assessment | All prior compatibility guarantees are evaluated and any exception blocks designation. |
| LTS3 | Support policy | Maintenance window, support levels, owners, review cadence, and end conditions are declared. |
| LTS4 | Change control | Allowed fixes, prohibited changes, backport criteria, and approval roles are fixed. |
| LTS5 | Release validation | Repository contracts, JSON, paths, links, baselines, and claim boundaries pass. |
| LTS6 | Independent review | Reviewer and authorizer roles assess the immutable candidate evidence. |
| LTS7 | Designation decision | Designate, hold, reject, or supersede is recorded without inventing operational evidence. |
| LTS8 | Maintenance cycle | Accepted changes and backports are recorded as append-only events and revalidated. |
| LTS9 | Retirement | Supersession, end-of-support, migration, residual risk, and archival state are recorded. |

## Decision states

Permitted decisions are `candidate`, `hold`, `designated`, `rejected`, `superseded`, and `retired`. `designated` requires complete repository evidence for LTS0–LTS7. Missing or unverifiable evidence resolves to `hold`, never `designated`.

## Invariants

- Canonical identity authority and identity-first ordering remain unchanged.
- Every compatibility guarantee from supported earlier versions remains in force unless an explicit, approved major-version exception and migration path exist.
- A patch or backport may not introduce a breaking schema, contract, identity, or support-tier change.
- Documentation, an empty registry, or a passing repository test does not prove production operation.
- Unknown evidence remains unknown; it is never converted to pass, zero risk, or a support claim.
- Adapter promotion, deployment, rollback, empirical certification, and production support remain governed by their canonical protocols.

## Evidence boundary

Repository validation may support an AHIF framework LTS designation. It cannot establish user adoption, external maintenance capacity, service-level achievement, real-world model fidelity, deployment health, or production availability. Those claims require separately supplied and governed evidence.
