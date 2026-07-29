# AHIF — Artificial Human Identity Framework

**Version:** 3.7.0
**Status:** Integrated AHIF Framework; Release Eligibility and LTS Designation HOLD
**Primary use case:** Consistent AI travel influencer generation from one canonical master photo.

AHIF is a modular software-engineering framework for generating a persistent digital human whose identity remains stable while clothing, hairstyle, pose, expression, activity, camera, weather response, and storytelling adapt to the requested context.

## Core operating principle

> Identity First. Human Second. Reality Third. Beauty Fourth.

## Framework pipeline

```text
User Request
→ Context
→ Core Identity
→ Knowledge Graph
→ Decision Engine
→ Reasoning Engine
→ Prompt Compiler
→ Quality Assurance
→ Final Prompt
→ Runtime
→ Model Adapter
→ Empirical Validation
→ Evidence Registry Proposal
→ Framework Result
```

Version 3.7.0 preserves the stable framework, canonical identity authority, prior governance modules, and claim boundaries while making repository validation, regression, release gates, and health reporting executable. Repository validation does not establish production health or operational LTS support; the LTS designation remains `hold`.

The runtime now applies the canonical [Photographic Realism Contract](07_PHOTOGRAPHY/PHOTOGRAPHIC_REALISM_CONTRACT.md): context-derived positive realism semantics, bounded artifact constraints, compiler readiness and contradiction controls, mandatory QA checks, and explicit adapter mapping disclosure. This additive integration does not copy mutable appearance from the master photo and does not alter version, empirical status, adapter tier, Release Eligibility, or LTS `hold`.

## Daily use

1. Upload the canonical master photo to the image generator.
2. Upload `00_CONTEXT/AHIF_AI_CONTEXT.md` to ChatGPT.
3. Ask ChatGPT to load the framework.
4. Provide a compact request:

```text
Location: Kyoto, Japan
Place: Gion district
Atmosphere: calm autumn morning
Output: final image-generation prompt
```

5. AHIF normalizes context, resolves decisions, validates reasoning, compiles one coherent prompt, runs mandatory QA gates, and releases only a validated artifact.

## Architectural responsibilities

- **Knowledge Graph** represents reusable facts and relationships.
- **Decision Engine** selects context-appropriate visual decisions.
- **Reasoning Engine** validates causality, evidence, alternatives, confidence, identity safety, and cross-domain coherence.
- **Prompt Compiler** expresses accepted decisions in deterministic model-neutral prompt form without inventing new decisions.
- **Quality Assurance** applies mandatory gates, deterministic linting, failure classification, scoring, and recovery routing.
- **Final Prompt Engine** orchestrates the complete execution, enforces release eligibility, and emits the validated prompt package and explainable result summary.
- **Model Adapter Layer** translates a released package into an exact target request while preserving identity, semantics, provenance, and loss disclosure.

## Repository map

- `00_CONTEXT/` — condensed operational context for AI loading
- `01_FOUNDATION/` — philosophy, constitution, architecture, vocabulary
- `02_CORE_IDENTITY/` — canonical identity and anti-drift rules
- `03_HUMAN_SIMULATION/` — anatomy, behavior, body language, realism
- `04_CHARACTER/` — personality, emotion, habits, continuity
- `05_FASHION/` — context-aware wardrobe, hair, makeup, accessories
- `06_TRAVEL_WORLD/` — geography, culture, weather, transport, safety
- `07_PHOTOGRAPHY/` — camera, lens, lighting, composition
- `08_STORY/` — narrative and environmental interaction
- `09_DECISION_ENGINE/` — context, knowledge graph, structured knowledge packages, inference, resolution, and reasoning
- `10_PROMPT_COMPILER/` — compiler pipeline, schemas, ordering, contradiction control, and serialization
- `11_QUALITY_ASSURANCE/` — QA orchestration, linting, failure taxonomy, recovery, schemas, domain gates, and final validation
- `12_TEMPLATES/` — reusable input and output templates
- `13_EXAMPLES/` — worked examples
- `14_TESTS/` — identity, decision, reasoning, compiler, QA, and final-prompt regression tests
- `15_FINAL_PROMPT/` — execution orchestration, release contracts, schemas, and final prompt packaging
- `16_MODEL_ADAPTERS/` — adapter architecture, registry, profiles, serializers, compatibility, empirical evidence, release, observation, and incident governance
- `17_CONTINUOUS_AUDIT/` — continuous compliance rules, drift detection, exceptions, snapshots, and append-only audit status
- `18_METRICS_QUALITY/` — canonical metrics, KPI thresholds, denominator controls, snapshots, and dashboard governance
- `19_SECURITY_SUPPLY_CHAIN/` — security scope, provenance, secret handling, vulnerability risk, exceptions, snapshots, and append-only registries
- `20_OPERATIONAL_RESILIENCE/` — recovery objectives, backup/restore governance, disaster declaration, runbooks, exercises, and resilience registries
- `21_LTS_GOVERNANCE/` — LTS designation, compatibility, maintenance, backport, deprecation, retirement, evidence, and registries
- `scripts/` — dependency-free validation, regression, failure-injection, release-gate, health, and canonical full-test entry points
- `.github/workflows/` — least-privilege validation, regression, and release-gate automation
- `docs/sprints/` — versioned sprint documentation
- `assets/identity-reference/` — canonical master-photo location

## Source of truth

The repository is the source of truth. AI context files are condensed operational views derived from canonical modules.

## Developer quick start

AHIF's local runtime and verification tools use the Python standard library; no
package installation or provider credential is required for repository-only
execution.

```sh
git clone <repository-url>
cd AHIF
python3 -m RUNTIME 13_EXAMPLES/runtime/KYOTO_AUTUMN.json > /tmp/ahif-result.json
make test
```

For a custom request, copy an example JSON and set `user_request.location`,
`user_request.place`, `user_request.atmosphere`, `identity.canonical_asset`, and
`adapter_id`. The committed repository contains a placement instruction at
`assets/identity-reference/PLACE_MASTER_PHOTO_HERE.txt`, not a real identity
photo. Supply a master photo through the applicable image workflow; local AHIF
records the asset reference but does not inspect pixels or invoke the provider.
See [`RUNTIME/README.md`](RUNTIME/README.md) for the complete input contract.

### Canonical minimal workflow

```text
User-supplied Master Photo reference
→ request Context (`user_request`)
→ Framework.execute(request)
→ `final_prompt_package`
→ `adapter_request`
→ `execution_report`
→ `empirical_validation.registry_update` proposal
→ governed Evidence Registration only if a real external artifact exists
```

The quickest API invocation is:

```python
import json
from pathlib import Path
from RUNTIME import Framework

request = json.loads(Path("13_EXAMPLES/runtime/KYOTO_AUTUMN.json").read_text())
result = Framework.execute(request)
print(result["final_prompt_package"])
print(result["adapter_request"])
print(result["execution_report"])
```

Interpret `execution_report.validation.status`, `stage_status`, `warnings`, and
`errors` before using an output. `metadata.external_model_invoked` remains
`false`: the adapter request is prepared, not submitted. Evidence registration
is conditional and governed; a missing external artifact must remain `MISSING`
and `NOT_EVALUATED`.

### Validation and troubleshooting

- Run `make test` for the canonical all-in-one check. A successful repository
  run ends with `SUMMARY: PASS`; `HOLD` from health and release-gate steps is an
  intentional governance outcome, not a fabricated release approval.
- Run `make runtime-test`, `make empirical-test`, `make audit`, or
  `make release-check` to isolate a subsystem.
- A CLI usage error means exactly one request JSON path is required. Invalid
  JSON must be corrected in the request file. `RuntimeContractError` identifies
  missing or invalid request fields; compare the request with
  `13_EXAMPLES/runtime/KYOTO_AUTUMN.json` and the input contract in
  `RUNTIME/README.md`.
- An unknown adapter or a QA failure returns a structured blocked result; inspect
  the execution report instead of bypassing the failed stage.
- Generated verification reports are in `.artifacts/reports/` and are ignored by
  Git. They prove only the checked-out repository state.

The final acceptance decision, certification criteria, and canonical boundaries
are in the [Framework V1 Acceptance Report](FRAMEWORK_ACCEPTANCE_REPORT.md),
[Certification Checklist](FRAMEWORK_CERTIFICATION_CHECKLIST.md), and
[Known Limitations](KNOWN_LIMITATIONS.md).

## Canonical identity rule

The uploaded master photo is the only canonical identity reference. Text may clarify the image but must never replace, reinterpret, or override it.

## Framework completion audit

Sprint 029 connects every required module, contract boundary, schema boundary, regression, example, pipeline stage, and output in the [Framework Traceability Matrix](FRAMEWORK_TRACEABILITY_MATRIX.md). The [Completeness Report](FRAMEWORK_COMPLETENESS_REPORT.md) states the audited denominator and result; the [Gap Analysis](FRAMEWORK_GAP_ANALYSIS.md) contains only repository-evidenced gaps; and the [Acceptance Checklist](FRAMEWORK_ACCEPTANCE_CHECKLIST.md) separates architectural acceptance from prohibited production, empirical, release, and LTS claims. Run `make audit` for the executable module, pipeline, manifest, and link gate.

## Current release — 3.7.0

Sprint 033 integrates the canonical runtime with the existing empirical-validation contracts after mandatory QA and adapter preparation. It emits deterministic, cross-referenced execution/evidence/report records as a non-persisted registry proposal; it does not invoke a model or fabricate evidence. The [Framework Integration Report](FRAMEWORK_INTEGRATION_REPORT.md) records the audited interfaces and remaining work. Run `make test`, `make audit`, and `make release-check` for repository-only verification.

Passing automation establishes repository conformance only. The baseline still contains zero registered LTS releases and zero maintenance events. The LTS designation is `hold`; no maintainer commitment, support adoption, backport execution, SLA achievement, deployment, empirical certification, production health, or production availability is asserted.

## Version 2.2 evidence aggregation

Accepted evidence bundles may now be grouped into explicit cohorts, aggregated conservatively, audited for outliers and drift, and converted into advisory target-profile recommendations. The framework does not include real external evidence in this release and never promotes adapters automatically.


## Version 2.3 evidence ingestion

Owner-supplied evidence can now be checked against explicit request and result schemas, verified using SHA-256 artifact fingerprints, classified as accepted, quarantined, rejected, or duplicate, and indexed in an append-only registry. Empirical evaluation and adapter promotion remain separate governed processes.


## Version 2.4 evidence evaluation

Only accepted evidence records may enter the evaluation queue. Evaluation jobs pin all governed versions, preserve append-only reviewer events, and resolve to completed, needs-revision, blocked, or cancelled without changing adapter status.


## Version 2.5 promotion decisions

Only completed evaluation jobs and eligible aggregates may enter a promotion dossier. Recommendations and authorizations are append-only governance records. Adapter registry mutation requires a separate release action with before/after snapshots, rollback instructions, stable-release QA, and documentation updates.


## Version 2.6 release execution

Only an authorized promote or downgrade dossier may open an adapter release plan. Every mutation must be declared, fingerprinted, validated, independently approved, reversible, and reconciled with repository documentation. AHIF 2.6.0 defines this mechanism without executing a real release.


## Version 2.7 release observation

Only a completed and signed release may open an observation plan. Observation may classify repository-level conformance and rollback readiness, but it cannot prove production health, create empirical evidence, mutate the adapter registry, or execute rollback.


## Sprint 022 Metrics and Quality Rule

Treat every metric as a versioned governance contract. Pin the exact population, numerator, denominator, exclusions, missing-data treatment, threshold version, and source fingerprints. Empty populations must produce `not-evaluated`, not zero or success. Dashboards are projections of immutable snapshots and may not fabricate telemetry, KPI achievement, empirical certification, production health, or adapter-tier changes. The AHIF 2.10.0 baseline contains zero registered metric specifications, zero metric snapshots, and zero dashboards.

## Sprint 023 Security and Supply Chain Rule

Treat repository security as a scoped, evidence-bound governance process. Never store raw secrets, fabricate advisory data, infer vulnerability absence from an empty finding registry, or treat repository review as infrastructure penetration testing. Unknown executable provenance and unresolved critical exposure block release eligibility. The AHIF 2.11.0 baseline contains zero security findings, zero provenance records, and status `not-evaluated`.

## Empirical validation infrastructure (Sprint 032)

[`22_EMPIRICAL_VALIDATION/`](22_EMPIRICAL_VALIDATION/README.md) provides executable scenario records, empty evidence registries, categorical human-evaluation contracts, baseline comparison records, SHA-256 integrity verification, and claim-bounded machine-readable reports. It accepts only artifacts supplied from real runs performed separately; it does not invoke image generation or external APIs. No empirical result, numeric score, benchmark, model certification, production readiness, Release Eligibility change, or LTS change is asserted.

## Executable Runtime (Sprint 030)

AHIF 3.7.0 provides a canonical deterministic executable framework in [`RUNTIME/`](RUNTIME/README.md). It executes the architectural pipeline through mandatory QA and prepares, but does not invoke, a registered model adapter. Use `Framework.execute()` or run `python3 -m RUNTIME 13_EXAMPLES/runtime/KYOTO_AUTUMN.json`; run `make runtime-test` for executable end-to-end examples. This capability does not change Release Eligibility or LTS HOLD status.
