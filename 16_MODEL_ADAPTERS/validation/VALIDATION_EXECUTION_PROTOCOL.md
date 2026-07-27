# Cross-Model Validation Execution Protocol

## Preconditions

- Final Prompt Package status is `release_eligible`.
- Canonical identity asset reference resolves.
- Adapter registry and selected capability profiles validate.
- Knowledge registry and consumed packages validate.
- Scenario fixture declares mandatory semantics and tolerances.

## Execution sequence

### V0 — Freeze inputs

Record immutable hashes for the Final Prompt Package, identity reference, adapter registry, capability profiles, knowledge registry, and scenario fixture.

### V1 — Resolve adapters

Resolve exact adapter and serializer versions. Unknown or floating versions are prohibited.

### V2 — Serialize requests

Generate target requests without adding new visual decisions. Record all transformations, defaults, losses, and unsupported controls.

### V3 — Run contract gates

Validate schema conformance, package binding, parameter legality, identity-reference mapping, negative constraints, and loss disclosure.

### V4 — Compare semantics

Compare each request with the same canonical package. Evaluate mandatory semantic preservation and permitted target-native variance.

### V5 — Attach empirical evidence

When outputs exist, bind each image, generation receipt, seed or job identifier, timestamp, and evaluator record. Missing empirical evidence must be explicit.

### V6 — Evaluate identity and degradation

Apply the identity comparison and degradation audit protocols. Identity failures block the adapter result.

### V7 — Aggregate release-candidate status

Emit per-adapter and cross-adapter results. `2.0.0-rc2` may pass contract validation while retaining `empirical_pending`; stable support requires empirical validation in the Sprint 012 release gate.

## Determinism

Re-executing V0–V4 with identical frozen inputs must produce byte-equivalent normalized requests and equivalent report findings.

## Prohibited behavior

- using one target model as the canonical reference;
- silently replacing unsupported identity controls;
- inferring image parity from request similarity;
- claiming production support from contract-only evidence;
- accepting undocumented loss.
