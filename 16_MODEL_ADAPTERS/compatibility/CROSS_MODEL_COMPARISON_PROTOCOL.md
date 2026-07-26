# Cross-Model Comparison Protocol

## Procedure

1. Validate one canonical Final Prompt Package and source hash.
2. Resolve exact adapters and immutable profiles.
3. Serialize every target request independently.
4. Validate each result against its adapter contract.
5. Extract normalized semantic evidence.
6. Compare each adapter result to the canonical package.
7. Produce pairwise variance records.
8. Apply compatibility class and confidence floors.
9. Emit a compatibility report and release recommendation.

## Evidence

Evidence must reference machine-readable fields, directive identifiers, serialized request paths, parameter mappings, and loss records. Human-readable explanation may summarize evidence but cannot replace it.

## Comparison Boundaries

This protocol validates request-level semantic compatibility. Empirical image-output validation is deferred to Sprint 011 and requires generated samples, identity metrics, and human review under a separate release-candidate protocol.

## Determinism

Repeated comparison of identical package hashes, adapter versions, profiles, and configurations must produce the same compatibility report.
