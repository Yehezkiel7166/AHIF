# Cross-Model Validation Contract Test

## Cases

### VAL-C01 — Frozen input binding

Changing any canonical package or identity hash after V0 must fail with `AHIF-VAL-001`.

### VAL-C02 — Exact adapter resolution

A floating adapter version must fail with `AHIF-VAL-002`.

### VAL-C03 — Deterministic serialization

Two executions using identical frozen inputs must produce the same normalized request hash.

### VAL-C04 — Canonical semantic loss

Removing a required scene, activity, or realism directive must fail with `AHIF-VAL-004`.

### VAL-C05 — Identity mapping loss

Dropping the identity reference or weakening its authority must fail with `AHIF-VAL-005`.

### VAL-C06 — Undisclosed degradation

Any D2–D4 transformation absent from the audit record must fail with `AHIF-VAL-006`.

### VAL-C07 — Missing image evidence

A contract-only run must report `empirical_pending`; it must not report generated-image equivalence.

### VAL-C08 — Failed identity comparison

Any mandatory identity score below threshold must fail with `AHIF-VAL-008`.

### VAL-C09 — Overstated support

Declaring production support while empirical evidence is pending must fail with `AHIF-VAL-010`.
