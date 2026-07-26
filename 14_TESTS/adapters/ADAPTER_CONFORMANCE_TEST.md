# Adapter Conformance Test

## Objective

Verify that any future model-specific adapter conforms to the AHIF adapter architecture before it is marked supported.

## Required Cases

### AC-001 Identity-Critical Native Mapping

A native identity reference capability preserves the source identity directive and trace.

### AC-002 Unsupported Identity Capability

An unsupported identity-critical requirement produces a blocked result.

### AC-003 Declared Non-Critical Degradation

A quality-optional unsupported feature produces `released_with_degradation` with complete disclosure.

### AC-004 Silent Omission Detection

A missing directive not represented in the plan fails conformance.

### AC-005 Capability Overclaim

Use of an undeclared capability fails conformance.

### AC-006 Deterministic Planning

Identical source package, profile version, and configuration produce the same transformation semantics.

### AC-007 Source QA Rejection

A non-release-eligible source package is blocked before serialization.

### AC-008 Traceability

Every target field maps to one or more source directives or approved adapter metadata.

## Acceptance

An adapter may be marked `supported` only when all blocking cases pass and no identity-critical degradation exists.
