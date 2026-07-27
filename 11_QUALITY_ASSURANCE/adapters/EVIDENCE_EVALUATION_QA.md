# Evidence Evaluation QA

## Mandatory gates

1. referenced registry record exists and is accepted;
2. artifact integrity remains verified;
3. evaluation scope and required dimensions are explicit;
4. all adapter, profile, scenario, protocol, and package versions are pinned;
5. scope fingerprint is valid and duplicate search completed;
6. state transition is permitted;
7. report references match requested dimensions;
8. independent reviewer separation is satisfied when required;
9. all event fingerprints and sequence values are valid;
10. adapter status remains unchanged.

## Failure codes

| Code | Meaning | Default outcome |
|---|---|---|
| `AHIF-EVAL-001` | job schema invalid | blocked |
| `AHIF-EVAL-002` | evidence record missing or not accepted | blocked |
| `AHIF-EVAL-003` | integrity verification failed | blocked |
| `AHIF-EVAL-004` | governed version not pinned | blocked |
| `AHIF-EVAL-005` | duplicate scope fingerprint | cancelled |
| `AHIF-EVAL-006` | invalid state transition | blocked |
| `AHIF-EVAL-007` | required evaluation report missing | needs_revision |
| `AHIF-EVAL-008` | independent review conflict | needs_revision |
| `AHIF-EVAL-009` | event sequence or fingerprint invalid | blocked |
| `AHIF-EVAL-010` | attempted automatic adapter status change | blocked |

## Completion gate

A job may be `completed` only when all requested reports are resolved, blocking findings are absent, independent review requirements pass, and `adapter_status_changed` is false.