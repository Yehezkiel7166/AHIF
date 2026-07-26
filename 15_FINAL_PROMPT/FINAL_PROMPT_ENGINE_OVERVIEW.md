# Final Prompt Engine Overview

## Purpose

The Final Prompt Engine is the release orchestration layer of AHIF. It executes the canonical path from compact user intent to a validated, traceable, model-neutral image-generation prompt without introducing new visual decisions after reasoning or compilation.

## Architectural position

```text
Compact Input
→ Context Normalization
→ Knowledge Retrieval
→ Decision Resolution
→ Reasoning Validation
→ Prompt Compilation
→ Quality Assurance
→ Final Prompt Release
```

## Responsibilities

The engine:

- coordinates all upstream contracts in deterministic order;
- preserves canonical identity as the highest-priority invariant;
- stops execution when a mandatory contract fails;
- requests the narrowest safe recovery action;
- emits one release artifact and one explainable result summary;
- records provenance, confidence, validation status, and release eligibility;
- never invents decisions during final serialization.

## Non-responsibilities

The engine does not:

- redesign the subject;
- choose fashion, pose, lighting, or story independently;
- bypass unresolved identity risk;
- convert warnings into silent acceptance;
- apply model-specific syntax before an adapter contract exists.

## Release invariant

A final prompt may be released only when:

1. the canonical identity reference is present or explicitly bound by the execution environment;
2. all required decision and reasoning records are complete;
3. the compiler reports no blocking contradiction;
4. mandatory QA gates pass;
5. recovery history contains no unresolved critical failure;
6. the output conforms to the Final Prompt Package schema.
