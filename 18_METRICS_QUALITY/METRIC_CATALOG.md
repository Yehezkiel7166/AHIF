# Canonical Metric Catalog

Every metric uses a stable identifier, explicit decision purpose, deterministic formula, eligible source classes, exclusions, review cadence, and claim boundary.

| ID | Metric | Formula or state | Claim boundary |
|---|---|---|---|
| AHIF-MET-001 | Manifest path resolution rate | resolved declared paths / declared paths | Repository structure only. |
| AHIF-MET-002 | JSON parse success rate | valid JSON files / JSON files checked | Syntax only. |
| AHIF-MET-003 | Local Markdown link resolution rate | resolved local links / local links checked | Link integrity only. |
| AHIF-MET-004 | Registry append-only conformance | pass, fail, or not-evaluated | Requires a declared comparison baseline. |
| AHIF-MET-005 | Governance document synchronization | synchronized required release documents / required documents | Metadata consistency only. |
| AHIF-MET-006 | Evidence intake completion rate | accepted or terminal intake records / eligible intake records | No model-quality claim. |
| AHIF-MET-007 | Evaluation queue completion rate | terminal evaluation jobs / eligible jobs | No score-quality claim. |
| AHIF-MET-008 | Decision dossier closure rate | terminal dossiers / eligible dossiers | No promotion claim. |
| AHIF-MET-009 | Release validation completion rate | signed validations / eligible completed releases | No production-health claim. |
| AHIF-MET-010 | Audit remediation closure rate | independently closed findings / eligible findings | Exceptions remain separately visible. |
| AHIF-MET-011 | Metric source freshness | age relative to specification limit | Staleness indicator only. |
| AHIF-MET-012 | Metric reproducibility status | reproducible, non-reproducible, or not-evaluated | Requires exact pinned inputs. |

A value is `not-evaluated` when the required source population is empty or unavailable. Zero must never be substituted for an undefined denominator.
