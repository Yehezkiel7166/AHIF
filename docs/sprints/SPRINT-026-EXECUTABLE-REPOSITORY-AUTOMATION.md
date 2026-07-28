# Sprint 026 — Executable Repository Automation

## Release

AHIF 3.1.0

## Objective

Turn the governance contracts delivered through Sprint 025 into dependency-free, executable repository validation, regression, release-gate, and health-reporting automation.

## Delivered artifacts

- repository-wide JSON, manifest-path, local-link, metadata, and whitespace validation;
- registry and LTS claim-boundary regression checks;
- a composed release gate that requires validation, regression, synchronized release evidence, and health reporting;
- least-privilege GitHub Actions workflows for pull requests, `main`, manual regression, and version tags;
- machine-readable repository health output and a checked-in Sprint 026 health report.

## Gate semantics

A nonzero script exit blocks its corresponding CI job. The release gate composes all checks rather than bypassing them. GitHub release creation or deployment is deliberately not automated: a passing gate establishes repository eligibility only.

## Compatibility and claim boundary

The automation evaluates tracked repository artifacts. It preserves all identity, evidence, adapter, audit, metrics, security, resilience, and LTS boundaries established through Sprint 025. A pass does not prove external model behavior, empirical quality, production health, deployment success, operational readiness, maintainer availability, SLA achievement, or LTS designation. The LTS designation remains `hold`.
