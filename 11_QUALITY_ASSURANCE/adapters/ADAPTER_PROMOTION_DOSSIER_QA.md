# Adapter Promotion Dossier QA

## Mandatory gates

1. dossier schema and decision-scope fingerprint are valid;
2. exact adapter version, current tier, and requested tier are pinned;
3. all referenced evaluation jobs exist and are completed;
4. evidence and aggregate eligibility remain valid at the declared cutoff;
5. scenario coverage and missing coverage are explicit;
6. adverse evidence, outliers, and drift findings are retained;
7. technical, governance, and authorization roles satisfy separation rules;
8. state transition and append-only event chain are valid;
9. recommendation is supported by the promotion gate and support policy;
10. adapter registry remains unchanged inside the dossier lifecycle.

## Failure codes

| Code | Meaning | Default outcome |
|---|---|---|
| `AHIF-PROMO-001` | dossier schema invalid | blocked |
| `AHIF-PROMO-002` | adapter or requested tier not pinned | blocked |
| `AHIF-PROMO-003` | evaluation job missing or incomplete | needs_revision |
| `AHIF-PROMO-004` | evidence or aggregate ineligible | blocked |
| `AHIF-PROMO-005` | scenario coverage incomplete or undisclosed | needs_revision |
| `AHIF-PROMO-006` | adverse evidence, outlier, or drift omitted | blocked |
| `AHIF-PROMO-007` | reviewer or authorizer conflict | needs_revision |
| `AHIF-PROMO-008` | invalid transition or event chain | blocked |
| `AHIF-PROMO-009` | recommendation exceeds evidence | blocked |
| `AHIF-PROMO-010` | attempted automatic adapter registry mutation | blocked |
| `AHIF-PROMO-011` | duplicate active decision scope | cancelled |
| `AHIF-PROMO-012` | stale policy or evidence cutoff | needs_revision |

## Authorization gate

A dossier may become `authorized` only when all mandatory gates pass, the recommendation is explicit, technical and governance review are complete, the authorizing role is independent, and `adapter_registry_changed` is false.

Authorization is evidence for a later release action; it is not itself a registry mutation.
