# Prompt Lint Rule Catalog

## Rule contract

Every lint rule has a stable identifier, severity, deterministic trigger, remediation guidance, and release effect.

| Rule | Severity | Trigger | Release effect |
|---|---|---|---|
| `AHIF-L001` | critical | Canonical identity lock is missing or weakened. | fail |
| `AHIF-L002` | critical | Prompt permits a different person, redesigned face, ethnicity drift, or age drift. | fail |
| `AHIF-L003` | error | Material directive lacks accepted decision or reasoning provenance. | fail |
| `AHIF-L004` | error | Unresolved contradiction remains in scene, weather, time, activity, camera, or lighting. | fail |
| `AHIF-L005` | error | Anatomy, balance, grip, contact, or object physics are impossible. | revise or fail |
| `AHIF-L006` | error | Explicit user constraint is omitted or contradicted. | revise |
| `AHIF-L007` | error | Cultural element is inaccurate, stereotyped, or decorative without context. | revise or fail |
| `AHIF-L008` | warning | More than one dominant activity or story beat is present. | revise |
| `AHIF-L009` | warning | Equivalent instructions are repeated without adding precision. | revise |
| `AHIF-L010` | warning | Styling conflicts with climate, activity, place, or character continuity. | revise |
| `AHIF-L011` | warning | Camera or lens language creates facial distortion risk. | revise |
| `AHIF-L012` | warning | Lighting, shadow, reflection, or color-temperature logic is inconsistent. | revise |
| `AHIF-L013` | warning | Negative constraints are generic, duplicated, or unrelated to identified risks. | revise |
| `AHIF-L014` | warning | Prompt over-specifies beauty traits that could overwrite identity. | revise |
| `AHIF-L015` | info | Optional refinement can improve clarity without changing decisions. | pass |
| `AHIF-L016` | error | Model-specific syntax appears before an approved adapter stage. | revise |

## Determinism

The same normalized QA package must produce the same triggered rule set. Rules must not depend on subjective aesthetic preference.

## Extension policy

New rules append new identifiers. Existing identifiers must not be repurposed because test history and release records depend on stable semantics.

## Photographic realism runtime rules

| ID | Trigger | Effect |
|---|---|---|
| `AHIF-QA-REALISM-SKIN-SYNTHETIC` | Positive prompt requests waxy, plastic, or porcelain skin | block |
| `AHIF-QA-REALISM-EXCESSIVE-SYMMETRY` | Positive prompt requests perfect or hyper-symmetry | block |
| `AHIF-QA-REALISM-EMPIRICAL-CLAIM` | Prompt asserts empirical generated-image success | block |
| `AHIF-QA-REALISM-LIGHTING-INCOHERENT` | Positive semantics request contradictory physical lighting | block |
| `AHIF-QA-REALISM-ENVIRONMENT-INTEGRATION` | Positive semantics request a pasted or cutout subject | block |
| `AHIF-QA-REALISM-COMPILER-INTEGRITY` | Declared realism contract lacks its semantic section | block |

Compiler failures `AHIF-COMPILER-REALISM-NOT-READY` and
`AHIF-COMPILER-REALISM-OPTICS-CONTRADICTION` block before QA. These checks do not score-compensate
identity failure.
