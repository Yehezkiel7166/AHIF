# Sprint 011 — Cross-Model Validation

## Release

Version: `2.0.0-rc2`

## Objective

Establish the end-to-end validation architecture, evidence contracts, identity comparison protocol, degradation auditing, and release-candidate regression baseline required before stable multi-model support can be declared.

## Delivered

- cross-model validation architecture;
- deterministic V0–V7 execution protocol;
- identity preservation comparison protocol and schema;
- degradation audit protocol;
- evidence and reproducibility policy;
- release-candidate conformance matrix;
- validation report schema;
- QA gates and stable `AHIF-VAL` failure codes;
- validation contract test and RC regression suite;
- Kyoto and Tokyo contract fixtures;
- machine-readable RC2 validation baseline.

## Evidence boundary

No external image-generation run is included in the repository. Therefore Sprint 011 validates repository contracts, deterministic request transformation, semantic preservation expectations, blocking behavior, and evidence handling. Empirical image equivalence remains explicitly pending and is mandatory for stable support in Sprint 012.

## Compatibility

Backward compatible with `2.0.0-rc1`. No canonical module, knowledge package, adapter, or prior test is removed.

## Acceptance criteria

- every registered adapter is bound to exact versions and profiles;
- fixtures preserve mandatory canonical semantics;
- identity mapping loss and undisclosed degradation block;
- missing empirical evidence is explicit;
- no production support claim is permitted;
- all JSON, manifest references, and local documentation links validate.
