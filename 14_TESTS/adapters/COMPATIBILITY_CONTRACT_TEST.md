# Compatibility Contract Test

## Contract Assertions

- compatibility is measured against the canonical package;
- exact adapter versions and immutable profiles are required;
- mandatory semantic domains cannot be skipped;
- identity has the highest comparison priority;
- pairwise comparison cannot override canonical findings;
- every variance has a type, evidence, confidence, and release effect;
- empirical image equivalence is not claimed by request-level tests;
- production promotion remains blocked before Sprint 011 validation.

## Negative Tests

The contract must reject:

- comparing requests from different source packages;
- missing identity evidence;
- silent negative-prompt loss;
- unknown capability assumptions;
- adapter result without exact profile version;
- promotion recommendation based only on aggregate score.
