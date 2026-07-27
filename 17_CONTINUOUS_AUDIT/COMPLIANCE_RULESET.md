# Compliance Rule-set

## Rule model

Every rule has a stable identifier, purpose, applicability condition, deterministic check, severity, evidence requirement, and remediation boundary.

## Baseline rules

| Rule | Requirement | Default severity |
|---|---|---|
| AHIF-COMP-001 | `VERSION.md`, README, manifest, changelog, roadmap, and latest sprint must agree. | major |
| AHIF-COMP-002 | Every path declared by `manifest.json` must resolve inside the repository. | major |
| AHIF-COMP-003 | All JSON documents must parse and preserve declared baseline counters. | major |
| AHIF-COMP-004 | Local Markdown links must resolve, excluding declared external assets. | moderate |
| AHIF-COMP-005 | Append-only registries must not lose or rewrite accepted historical records. | critical |
| AHIF-COMP-006 | No governance record may imply empirical or operational evidence that is absent. | critical |
| AHIF-COMP-007 | Role-separation requirements must be explicit for approval and validation. | major |
| AHIF-COMP-008 | Release, observation, incident, and audit states must retain provenance links. | major |
| AHIF-COMP-009 | Canonical identity authority must remain the owner-provided master photo. | critical |
| AHIF-COMP-010 | A release package must include validation results and rollback boundaries. | major |
| AHIF-COMP-011 | Exceptions must be scoped, time-bounded, approved, and reviewable. | major |
| AHIF-COMP-012 | Audit closure must preserve unresolved risks and adverse findings. | major |

Rules are repository controls. They do not prove external model behavior or production reliability.
