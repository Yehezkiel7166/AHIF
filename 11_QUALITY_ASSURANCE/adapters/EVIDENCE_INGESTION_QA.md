# Evidence Ingestion QA

## Mandatory gates

1. request schema valid;
2. declarations complete;
3. stable identifiers present;
4. artifact paths safe;
5. SHA-256 syntax valid;
6. available bytes match declared digests;
7. provenance minimum satisfied;
8. duplicate search completed;
9. evaluation references resolved or quarantined;
10. adapter status remains unchanged.

## Failure codes

| Code | Meaning | Default result |
|---|---|---|
| `AHIF-ING-001` | request schema invalid | rejected |
| `AHIF-ING-002` | unsafe or invalid artifact path | rejected |
| `AHIF-ING-003` | artifact digest mismatch | rejected |
| `AHIF-ING-004` | required artifact unavailable | quarantined |
| `AHIF-ING-005` | provenance incomplete | quarantined |
| `AHIF-ING-006` | exact duplicate found | duplicate |
| `AHIF-ING-007` | evaluation linkage invalid | quarantined |
| `AHIF-ING-008` | conflicting adapter/model metadata | rejected |
| `AHIF-ING-009` | declaration boundary violated | rejected |
| `AHIF-ING-010` | attempted automatic adapter promotion | rejected |

## Release gate

An ingestion result is valid only when the decision is deterministic, all failure codes are from this catalog, and `adapter_status_changed` is false.