# Compatibility Guarantees

## Stable 2.0 guarantees

AHIF 2.0 guarantees:

- canonical identity authority remains the master photo;
- stable knowledge identifiers retain their documented meaning;
- reasoning, compiler, QA, final-prompt, and adapter schemas remain backward compatible within the 2.x line unless a critical defect requires a documented exception;
- adapter degradation and loss disclosures remain mandatory;
- deterministic ordering and release-state semantics remain stable;
- no model adapter may silently weaken identity constraints.

## Non-guarantees

AHIF does not guarantee identical pixels, composition, or facial fidelity across external image generators. Those outcomes depend on model versions, provider behavior, sampling, safety systems, and execution environments.

## Change classes

- **Patch** — corrections that preserve contracts.
- **Minor** — backward-compatible capability expansion.
- **Major** — intentional contract break with migration documentation.

## Deprecation

A stable field or identifier must be deprecated before removal. Deprecation records must include replacement guidance and the earliest removal version.
