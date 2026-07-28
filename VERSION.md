# Version

Current version: **3.5.0**

Release type: Backward-Compatible Minor Executable Framework Capability

## Semantic-version decision

Sprint 031 materially expands the 3.4 runtime into one public executable framework with an explicit deterministic state machine, complete stage contracts, a canonical result package, a machine-readable execution report, blocked-path propagation, deterministic recovery records, scenario execution, and failure-path tests. `Framework.execute()` is canonical; the prior `execute_framework()` API remains compatible and delegates to it. These additive capabilities justify version **3.5.0** under the existing semantic-version policy.

Canonical identity authority, compatibility guarantees, adapter contracts, governance, historical records, and claim boundaries remain unchanged. Release Eligibility and LTS remain **HOLD**. Executable repository conformance is not production readiness or empirical validation.

## Claim boundary

Repository execution does not claim production readiness, does not claim deployment success, does not claim external telemetry, does not claim operational availability, does not claim security certification, does not claim disaster-recovery execution, and does not claim empirical model certification.

LTS status: HOLD
