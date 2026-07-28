# AHIF LTS Maintenance Policy

## Support model

AHIF 3.0.0 LTS establishes a stable governance baseline for the framework. Maintenance changes must be classified as corrective, security-related, documentation-only, compatibility-preserving enhancement, deprecation, or breaking change.

## Rules

1. Stable schemas and identifiers must not be changed incompatibly in a patch release.
2. Deprecations require a replacement path, migration guidance, and a declared removal window.
3. Breaking changes require a new major version.
4. Security and integrity corrections may override ordinary cadence but still require documented scope and validation.
5. Adapter capability claims remain evidence-bound and may not be promoted by documentation changes.
6. Empty registries retain `not-evaluated`; they do not imply success, safety, or absence of findings.
7. Every maintenance release must synchronize README, VERSION, CHANGELOG, ROADMAP, manifest, AI context, tests, and release validation.

## LTS claim boundary

LTS describes contract and maintenance stability. It does not certify production deployment, external model behavior, operational availability, security penetration testing, or disaster-recovery execution.
