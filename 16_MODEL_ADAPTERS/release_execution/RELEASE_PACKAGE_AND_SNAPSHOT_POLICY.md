# Release Package and Snapshot Policy

## Required package contents

Every adapter release package must include:

- authorized promotion dossier reference and fingerprint;
- release plan and release-scope fingerprint;
- exact adapter, capability-profile, support-policy, registry, and framework versions;
- declared file mutation list;
- pre-change registry snapshot and SHA-256 fingerprints;
- migration record describing each old and new value;
- validation commands or deterministic validation procedures;
- rollback plan and rollback owner;
- post-change snapshot;
- approval, validation, and final signoff events.

## Snapshot rules

Snapshots are immutable evidence of repository state, not editable working documents. Each snapshot must contain the exact serialized value or content fingerprint for every affected path. A post-change snapshot must be compared with the package manifest; undeclared changes block completion.

## Rollback rules

Rollback must restore the complete pre-change state for every declared mutation. A rollback plan is invalid when it depends on unavailable artifacts, unspecified manual reconstruction, or mutable external references.

## Reproducibility

Given the same authorized dossier, pinned repository state, package manifest, and release procedure, another maintainer must be able to reconstruct the same candidate diff and validation result.
