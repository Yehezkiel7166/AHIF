# Recovery Orchestration

## Objective

Recovery restores compliance with the smallest explainable intervention while preserving accepted user intent and canonical identity.

## Recovery levels

| Level | Scope | Example |
|---|---|---|
| R0 | no change | informational finding only |
| R1 | local text repair | remove duplicate directive |
| R2 | section repair | rebuild lighting section from accepted directives |
| R3 | compiler-plan repair | reorder or remove conflicting compiler units |
| R4 | reasoning rollback | return unsupported decision for new evidence evaluation |
| R5 | decision rollback | reselect a context decision under canonical priorities |
| R6 | hard rejection | identity or safety cannot be recovered from current input |

## Routing rules

- Missing identity lock routes directly to R3 or R6; never patch with weak generic wording.
- Unsupported material facts route to R4.
- Contradictory accepted decisions route to R4 or R5.
- Redundancy and section-order defects route to R1 or R3.
- Anatomy or physics defects caused by expression wording route to R2; defects caused by the selected activity route to R5.
- Cultural inaccuracies require new grounded evidence and route to R4 or R5.

## Repair safeguards

A repair must:

- preserve explicit user constraints unless they caused a higher-priority violation
- preserve canonical identity invariants
- record changed fields and reasons
- avoid introducing new material facts
- trigger revalidation of affected dependencies

## Termination

Stop recovery when:

- the artifact passes all mandatory gates
- the maximum safe repair level is exhausted
- identity confidence falls below the release threshold
- required evidence is unavailable
- user constraints are mutually incompatible

Hard rejection is preferable to an untraceable compromise.
