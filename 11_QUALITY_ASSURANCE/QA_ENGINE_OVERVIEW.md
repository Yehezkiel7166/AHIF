# Quality Assurance Engine

## Purpose

The Quality Assurance Engine is the final policy and validation boundary before AHIF emits a usable prompt. It evaluates the compiled artifact against identity, human realism, environmental truth, cultural respect, compiler integrity, and output-contract requirements.

QA does not redesign the scene. It detects failures, classifies severity, determines whether repair is safe, and either accepts, revises, or rejects the artifact.

## Inputs

The engine consumes:

- normalized user constraints
- canonical identity invariants
- accepted decision record
- reasoning result and confidence summary
- compiler plan
- compiled prompt
- negative constraints
- compiler metadata and provenance

## Outputs

The engine emits:

- overall status: `pass`, `revise`, or `fail`
- category scores
- findings with stable failure codes
- blocking and non-blocking findings
- repair actions
- recovery route
- validation evidence
- release eligibility

## Governing hierarchy

1. safety and policy
2. canonical identity
3. anatomy and physics
4. cultural respect
5. explicit user constraints
6. environmental truth
7. character continuity
8. story coherence
9. visual refinement

A lower-priority preference cannot compensate for a higher-priority failure.

## Status semantics

| Status | Meaning |
|---|---|
| `pass` | All mandatory gates pass; only informational findings may remain. |
| `revise` | No unrecoverable failure exists, but one or more repairable blocking findings remain. |
| `fail` | Identity, safety, evidence, contradiction, or output-contract failure prevents safe release. |

## Architectural boundary

The Decision Engine selects. The Reasoning Engine validates and explains. The Prompt Compiler expresses accepted decisions. The Quality Assurance Engine evaluates the compiled artifact and controls release. It must not silently invent replacement decisions.
