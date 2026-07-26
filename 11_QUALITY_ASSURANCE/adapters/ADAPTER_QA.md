# Adapter Quality Assurance

## Purpose

Adapter QA validates that model-specific translation preserves the canonical Final Prompt Package and declares every compatibility loss.

## Gates

### AQ-01 Source Eligibility

The source package must have a release-eligible QA state.

### AQ-02 Profile Integrity

The exact adapter profile and version must resolve from the registry.

### AQ-03 Directive Coverage

Every canonical directive must appear in the transformation plan.

### AQ-04 Identity Preservation

Identity-critical directives must remain semantically intact.

### AQ-05 Capability Honesty

The adapter must not use or claim undeclared capabilities.

### AQ-06 Loss Disclosure

Every omission, approximation, or degradation must be explicit.

### AQ-07 Serialization Conformance

The target request must conform to the adapter request contract.

### AQ-08 Trace Completeness

The result must link source directives, transformation operations, and target fields.

## Blocking Conditions

Identity loss, undeclared semantic loss, unsupported mandatory capability, source ineligibility, or incomplete trace blocks release.
