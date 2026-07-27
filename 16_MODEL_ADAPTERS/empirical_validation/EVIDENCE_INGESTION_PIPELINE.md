# Evidence Ingestion Pipeline

## Purpose

This pipeline accepts user-supplied empirical execution evidence and converts it into a governed AHIF evidence record without changing adapter support status automatically.

## Authority boundary

- The canonical master photo remains the sole identity authority.
- External generated images are observations, never identity references.
- Ingestion validates evidence structure and integrity; it does not certify image quality.
- Promotion decisions remain separate, reviewable governance actions.

## Pipeline I0–I8

### I0 — Intake
Receive an ingestion request, evidence bundle, declared adapter profile, and artifact inventory.

### I1 — Schema validation
Validate required fields, identifiers, timestamps, adapter version, model version, and evaluation references.

### I2 — Artifact inventory
Require every declared artifact to have a relative path, media type, byte size, and SHA-256 digest.

### I3 — Integrity verification
Recompute digests when bytes are available. A mismatch blocks ingestion with `AHIF-ING-003`.

### I4 — Provenance verification
Confirm execution source, operator declaration, prompt-package reference, target request reference, and collection timestamp.

### I5 — Duplicate detection
Compare bundle ID, execution ID, target-request digest, generated-artifact digest, and registry fingerprints. Exact duplicates are rejected; related reruns are linked.

### I6 — Evaluation linkage
Validate identity and semantic report references. Missing empirical evaluations result in `quarantined`, not `accepted`.

### I7 — Registry decision
Emit one status:

- `accepted` — integrity and minimum evidence requirements pass;
- `quarantined` — structurally valid but incomplete, unverifiable, or awaiting review;
- `rejected` — invalid, conflicting, unsafe, or corrupted;
- `duplicate` — an equivalent evidence record already exists.

### I8 — Append-only registration
Write a new registry event. Existing historical events are never rewritten. Corrections create superseding events.

## Determinism

Given the same request, artifact digests, registry snapshot, and policy version, the pipeline must produce the same decision and failure-code set.

## Non-goals

This pipeline does not execute image models, calculate facial similarity, approve target profiles, or promote adapters.