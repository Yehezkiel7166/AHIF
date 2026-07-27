# Cross-Model Validation QA

## Mandatory gates

| Gate | Failure code | Blocking condition |
|---|---|---|
| Frozen input integrity | AHIF-VAL-001 | Missing or mismatched canonical hash |
| Exact adapter binding | AHIF-VAL-002 | Floating, unknown, or mismatched version |
| Deterministic serialization | AHIF-VAL-003 | Same input produces different normalized request |
| Semantic preservation | AHIF-VAL-004 | Required canonical semantic is lost |
| Identity reference integrity | AHIF-VAL-005 | Identity binding is absent or weakened |
| Loss disclosure | AHIF-VAL-006 | Material transformation loss is undisclosed |
| Evidence integrity | AHIF-VAL-007 | Evidence is unresolved, mutable, or hash-invalid |
| Identity comparison | AHIF-VAL-008 | Mandatory identity threshold fails |
| Reproducibility declaration | AHIF-VAL-009 | Achieved level is absent or overstated |
| Release claim integrity | AHIF-VAL-010 | Support claim exceeds evidence |

## Severity

AHIF-VAL-001, 002, 004, 005, 006, 008, and 010 are critical. AHIF-VAL-003, 007, and 009 are high unless they prevent evaluation, in which case they are critical.

## RC2 acceptance

The repository-level Sprint 011 suite passes when contract and semantic fixtures pass, blocking behavior is correct, all missing empirical evidence is explicit, and no adapter is promoted beyond `experimental`.

## Stable-release handoff

Sprint 012 must consume current external evidence, rerun all gates, resolve or scope every blocking finding, and publish exact compatibility guarantees.
