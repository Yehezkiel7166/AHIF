# Adapter Release Observation Protocol

## Purpose

Define the governed O0–O9 process used after a completed adapter release to verify that the released state remains consistent, reversible, evidence-bounded, and free from undocumented regression.

Observation does not create empirical evidence automatically and does not expand an adapter support claim. It records repository-level conformance, declared operational signals, rollback readiness, and any required containment action.

## Preconditions

An observation plan may be opened only when:

1. one release execution record is in `completed` state;
2. its post-change snapshot and signoff are valid;
3. the exact adapter, release, registry, policy, and package fingerprints are pinned;
4. an observation owner, independent validator, and rollback verifier are assigned;
5. no active observation owns the same observation-scope fingerprint.

## O0–O9 workflow

| Stage | Name | Required outcome |
|---|---|---|
| O0 | Resolve completed release | completed release and signoff verified |
| O1 | Freeze observation scope | adapter, release, signal sources, window, thresholds, and governed versions pinned |
| O2 | Capture observation baseline | signed post-release baseline fingerprint recorded |
| O3 | Collect declared signals | only declared repository, compatibility, QA, and owner-supplied signals accepted |
| O4 | Evaluate conformance | drift, regression, claim-boundary, and integrity checks executed |
| O5 | Verify rollback readiness | rollback package, ownership, and reconstruction path revalidated |
| O6 | Classify outcome | healthy, watch, contain, rollback_recommended, blocked, or cancelled |
| O7 | Authorize response | independent authority accepts the exact response fingerprint |
| O8 | Reconcile state | documentation, registry, incidents, and rollback references reconciled |
| O9 | Publish observation record | append-only event chain and signoff published |

## State model

```text
planned
→ observing
→ evaluated
→ healthy
| watch
| contain
| rollback_recommended
| blocked
| cancelled
```

`healthy` is valid only when every mandatory observation gate passes. `rollback_recommended` is advisory and cannot execute rollback; it must open a governed release action referencing the original release and rollback package.

## Signal boundary

- repository and contract checks may be generated locally;
- model-output evidence must be owner supplied through the existing evidence-ingestion workflow;
- no undeclared telemetry source may be treated as authoritative;
- absent signals cannot be interpreted as successful production operation;
- observation cannot promote an adapter or widen support claims.

## Baseline boundary

AHIF 2.7.0 defines observation and rollback assurance only. The baseline includes zero observation plans, zero health certifications, zero incidents, and zero rollback recommendations.
