# Continuous Audit Contract Test

## Assertions

1. CA0 rejects an unknown repository version or duplicate scope fingerprint.
2. CA1 resolves only declared rules and applicability.
3. CA2 snapshots every governed input with SHA-256.
4. CA3 detects release-file, manifest, JSON, link, and registry violations.
5. CA4 distinguishes a changed file from a violated contract.
6. CA5 preserves adverse findings and evidence references.
7. CA6 blocks expired or self-approved exceptions.
8. CA7 requires owner, validation, and rollback boundaries.
9. CA8 is performed by an independent role.
10. CA9 cannot close critical unresolved risk.
11. No stage mutates adapter tier, canonical identity, or operational environment.
12. Missing external telemetry remains unavailable rather than inferred.
