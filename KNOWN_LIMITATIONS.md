# AHIF Known Limitations

This is the canonical limitation register for Framework V1 acceptance. Each
entry distinguishes what the repository currently does from work that can occur
only when real inputs, execution, evidence, or authorization are supplied. A
future-work statement is not a promise or a new AHIF module.

## 1. Canonical identity asset is user-supplied

**Repository capability:** `manifest.json` names
`assets/identity-reference/MASTER_PHOTO.jpg`, but the repository intentionally
contains `PLACE_MASTER_PHOTO_HERE.txt` rather than a person's master photo. The
runtime accepts a canonical asset reference and locks it as identity metadata;
it does not inspect image pixels or prove that the referenced file is a valid
photo.

**Future work:** A user must supply the master photo to the applicable local or
provider workflow and comply with the Master Photo Protocol. Repository
acceptance cannot supply, infer, or certify a person's identity asset.

## 2. Adapter execution is not included

**Repository capability:** `RUNTIME/engine.py` prepares
`adapter_request`, records `external_model_invoked: false`, and performs no
network call. `RUNTIME/README.md` explicitly limits execution to deterministic
local preparation.

**Future work:** An authorized operator may submit the prepared request to a
supported external tool under that tool's requirements. Provider credentials,
availability, billing, safety behavior, model behavior, and returned artifacts
are outside repository execution and are not asserted.

## 3. Empirical evidence is absent

**Repository capability:** `22_EMPIRICAL_VALIDATION/README.md` defines schemas,
categorical review, SHA-256 integrity checks, deterministic reports, and empty
registries. Runtime preparation emits a non-persisted proposal with evidence
`MISSING` and evaluation `NOT_EVALUATED`.

**Future work:** Real output must be produced separately, supplied through the
governed evidence workflow, integrity-checked, and reviewed by identified human
reviewers before any scoped empirical conclusion is possible. No current image
quality, identity preservation, semantic equivalence, benchmark, or adapter
certification claim is supported.

## 4. Governance specifications are not operational telemetry

**Repository capability:** Continuous Audit, Metrics and Quality, Security and
Supply Chain, and Operational Resilience define policies, schemas, blocked
examples, and registries. Their current empty or `not-evaluated` records do not
represent successful external operations. `FRAMEWORK_INTEGRATION_REPORT.md`
also records that older narrative governance contract tests remain Markdown
specifications rather than executable unit tests.

**Future work:** Evidence from actual audit operation, metric populations,
security assessment, provenance collection, backup/restore, disaster recovery,
failover, and rollback exercises must be supplied and evaluated under the
existing governance before any corresponding operational claim can be made.

## 5. Release Eligibility and LTS remain HOLD

**Repository capability:** the repository release gate distinguishes passing
repository conformance from release authorization. `15_FINAL_PROMPT/RELEASE_ELIGIBILITY.md`
retains its existing eligibility states, and
`21_LTS_GOVERNANCE/registry/LTS_STATUS.json` records `status: hold`, zero
registered releases, zero maintenance events, and `not-evaluated` validation.

**Future work:** Only the existing governance processes and their required real
evidence and authorization can change Release Eligibility or LTS. Framework V1
acceptance does not do so.

## 6. Repository checks have a bounded meaning

**Repository capability:** `scripts/test_all.sh` validates repository structure,
JSON and links, runtime behavior, empirical validators, negative fixtures,
configured registries, release evidence, and source syntax. Reports are
generated locally under ignored `.artifacts/reports/` and identify the tested
commit.

**Future work:** Passing these checks does not test an external provider,
generated pixels, deployment environment, production load, availability,
security posture, or recovery execution. Those claims require their own scoped
evidence; repository success must not be reused as that evidence.

## 7. Determinism is local and input-scoped

**Repository capability:** identical request objects, including an explicit UTC
execution timestamp, produce deterministic local packages and trace metadata.
The runtime uses a stable default timestamp when none is provided.

**Future work:** Pixel-level reproducibility and provider-side determinism are
not guaranteed or tested. Any comparison of external outputs must use the
existing empirical evidence and comparison contracts rather than extrapolating
from local package determinism.

