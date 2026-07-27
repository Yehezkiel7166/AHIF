# Continuous Compliance and Governance Audit Protocol

## Purpose

This protocol governs recurring repository-level compliance assessment after incident-response governance. It detects policy drift, stale references, incomplete release reconciliation, and broken governance contracts without inventing operational telemetry or changing adapter state.

## Entry requirements

An audit run must pin:

- repository version and commit or archive fingerprint;
- manifest, roadmap, changelog, version, constitution, and AI-context versions;
- enabled compliance rule-set version;
- audit scope and exclusions;
- auditor, reviewer, exception approver, and closure authority roles;
- immutable audit-scope fingerprint.

## CA0–CA9 workflow

| Stage | Name | Required outcome |
|---|---|---|
| CA0 | Scope intake | Validate repository identity, scope, and duplicate-run status. |
| CA1 | Rule resolution | Resolve active rules and applicability. |
| CA2 | Snapshot | Capture immutable hashes for governed inputs. |
| CA3 | Conformance checks | Evaluate deterministic repository and documentation controls. |
| CA4 | Drift analysis | Compare current state with the last accepted baseline. |
| CA5 | Finding classification | Assign severity, evidence links, and affected contracts. |
| CA6 | Exception review | Validate time-bounded exceptions and compensating controls. |
| CA7 | Remediation plan | Assign owner, due condition, validation method, and rollback boundary. |
| CA8 | Independent validation | Re-run resolved checks and verify closure evidence. |
| CA9 | Closure | Append signoff and publish the immutable audit report. |

## Finding severity

- `critical`: canonical authority, provenance, or release-chain integrity is invalid;
- `major`: a required governance contract or release gate is broken;
- `moderate`: drift can mislead future execution but does not invalidate current artifacts;
- `minor`: bounded documentation or metadata inconsistency;
- `informational`: observation requiring no remediation.

## Hard boundaries

Continuous audit does not automatically:

- execute deployments, rollback, containment, or recovery;
- mutate adapter tiers, profiles, or canonical identity authority;
- create empirical evidence or production telemetry;
- approve its own exceptions or findings;
- certify production health, availability, or model output quality.
