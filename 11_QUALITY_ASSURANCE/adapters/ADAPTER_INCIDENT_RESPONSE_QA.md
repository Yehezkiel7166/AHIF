# Adapter Incident Response QA

## Failure catalog

| Code | Failure |
|---|---|
| AHIF-INC-001 | Missing completed release reference |
| AHIF-INC-002 | Missing observation provenance |
| AHIF-INC-003 | Duplicate incident scope |
| AHIF-INC-004 | Invalid severity assignment |
| AHIF-INC-005 | Undeclared containment mutation |
| AHIF-INC-006 | Missing independent authorization |
| AHIF-INC-007 | Non-reconstructable rollback or restore path |
| AHIF-INC-008 | Role conflict between responder, validator, and authorizer |
| AHIF-INC-009 | Snapshot or package fingerprint mismatch |
| AHIF-INC-010 | Invalid status transition or event sequence |
| AHIF-INC-011 | Empirical or production-health claim inflation |
| AHIF-INC-012 | Unrecorded residual risk |
| AHIF-INC-013 | Incident closed without validation |
| AHIF-INC-014 | Canonical identity authority mutation |
| AHIF-INC-015 | Registry event rewritten or deleted |
| AHIF-INC-016 | Recovery action executed outside declared scope |

A release passes only when every applicable failure is absent or explicitly blocks the incident from completion.
