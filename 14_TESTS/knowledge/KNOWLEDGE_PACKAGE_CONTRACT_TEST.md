# Knowledge Package Contract Test

## Test objective

Verify every registered structured knowledge package is deterministic, traceable, identity-safe, and consumable by AHIF.

## Required assertions

1. Registry JSON parses successfully.
2. Every registered package path exists.
3. Package and record identifiers are globally unique.
4. Declared record counts match actual records.
5. Every canonical source path exists.
6. Every record contains conditions, effects, constraints, confidence, provenance, and consumer hints.
7. Confidence values are within `0.0–1.0`.
8. Priority values are integers within `0–100`.
9. No candidate record permits identity redesign or generic-person substitution.
10. Registry and package versions agree.

## Expected result

All initial fashion, travel, and photography packages pass. Any failed assertion blocks release-candidate knowledge consumption.
