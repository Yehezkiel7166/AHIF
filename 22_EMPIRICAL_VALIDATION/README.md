# AHIF empirical validation framework

## Boundary

Empirical validation is the controlled collection, integrity verification, human review, and reporting of evidence from real image-generation runs performed outside this repository workflow. This directory makes AHIF **empirically validatable**. It does not execute image generation, call external APIs, contain completed empirical results, establish benchmark performance, certify an adapter, imply production readiness, or change Release Eligibility or LTS. LTS remains **HOLD**.

## Architecture

- `scenarios/`: versioned executable input definitions, initially grounded in the Kyoto and Tokyo repository examples.
- `executions/`: append-only metadata for externally performed runs.
- `evidence/`: evidence manifests linking artifacts to SHA-256 digests. Binary artifacts are not supplied by this sprint.
- `evaluations/`: categorical human reviews across every repository dimension.
- `metrics/`: the fixed dimension and status vocabulary; numeric and automatic scores are prohibited.
- `baseline/`: baseline/candidate comparison records. An image is identified by its digest, not implied to exist.
- `reports/`: machine-readable, metadata-only report records with an explicit no-production-claim boundary.
- `schemas/`: JSON Schema 2020-12 contracts for Scenario, Execution, Evaluation, Evidence, Comparison, and Report.
- `framework.py`: dependency-free record validation, SHA-256 verification, and deterministic report assembly. It has no model or network integration.

All registries begin empty. Empty means no evidence has been collected and no evaluation has occurred.

## Evidence workflow

1. Select a committed scenario and compile a prompt package through the existing runtime without invoking a model.
2. An authorized operator separately performs a real run and stores the raw output in an approved evidence location.
3. Record the execution ID, framework version, scenario, UTC timestamp, exact adapter, prompt-package SHA-256, optional image SHA-256, statuses, reviewer, and comments.
4. Create an Evidence record. Set `AVAILABLE` only when at least one artifact and its actual SHA-256 are present.
5. Run `verify_evidence()` against the repository/evidence root. Missing files, unsafe paths, and digest mismatches fail closed.
6. Preserve records rather than rewriting adverse or missing evidence.

The framework never discovers artifacts, calls providers, or marks evidence available automatically.

## Evaluation workflow

A human reviewer creates an Evaluation record. Every dimension—identity, anatomy, pose, hair, face, lighting, camera, composition, story, environment, cultural accuracy, prompt consistency, and overall—uses only `NOT_EVALUATED`, `PENDING`, `APPROVED`, or `REJECTED`. Numeric scores and automatic assignments are outside this contract. An overall approved/rejected evaluation requires an identified reviewer and a disposition for every dimension. Evidence can remain missing or rejected independently of evaluation state.

A baseline comparison records baseline and candidate image digests, categorical decision, optional evidence link, reviewer, and comments. No empty baseline represents a result.

## Reports and use

`build_report()` copies execution, scenario, prompt-package metadata, and statuses into a deterministic machine-readable document. Every report carries `NO_PRODUCTION_CLAIM`. Approval is a reviewer disposition about the scoped artifact; it is not a benchmark, production-readiness decision, release authorization, adapter promotion, or LTS evidence by itself. Existing governed ingestion, evaluation, promotion, and release processes remain authoritative.

## Run tests

```bash
python3 -m unittest discover -s 14_TESTS/empirical_validation -p 'test_*.py' -v
```

## Runtime integration (Sprint 033)

`Framework.execute()` delegates its final local stage to `prepare_runtime_validation()` after QA, final-prompt release control, and adapter preparation. The function validates and returns cross-referenced execution, missing-evidence, and report records. Its `registry_update` is an in-memory proposal, not a persisted empirical claim. `validate_registries()` checks canonical envelopes, record schemas, duplicate identifiers, and execution references across all five registries. External execution, artifact ingestion, and human review remain separate governed actions.
