# Sprint 027 — Executable Verification Hardening

## Release and semantic version

AHIF **3.2.0** is a backward-compatible minor release. The canonical test entry point, stable machine-readable report interface, failure-injection suite, Make targets, and end-to-end gate are new capabilities rather than a narrowly scoped defect correction; therefore 3.2.0 is appropriate instead of 3.1.1. No compatibility-breaking 4.0.0 change is made.

## Delivered verification system

- `scripts/test_all.sh` fail-fast orchestration with deterministic exit semantics and summary;
- JSON reports for validation, regression, health, release gate, and complete run;
- isolated malformed-JSON, missing-target, broken-link, inconsistent-version, invalid-LTS, and claim-boundary negative cases;
- JSON and Markdown repository health inventories;
- Make targets and least-privilege PR CI with report artifacts.

## RED → GREEN → REGRESSION → AUDIT evidence

The six controlled fixtures form the RED suite and must each be rejected. The unchanged repository forms GREEN. Governance regression preserves registry structure and `hold`; the full harness then audits syntax, report creation, composition, and claim boundaries end to end.

## Claim boundary and decision

Repository automation does not claim production readiness, deployment success, operational availability, external telemetry, security certification, disaster-recovery execution, empirical model certification, or adapter-tier change. Canonical identity authority is unchanged. **LTS status: HOLD** because no separate verifiable maintainer, authorization, maintenance, SLA, deployment, or operational evidence is present.
