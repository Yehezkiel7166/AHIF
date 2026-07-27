# Stable Release QA

## Mandatory gates

| Gate | Requirement |
|---|---|
| SR-01 | Version, changelog, roadmap, README, context, and manifest agree |
| SR-02 | Every manifest reference resolves |
| SR-03 | All JSON documents parse |
| SR-04 | Stable identifiers are unique and unchanged |
| SR-05 | Canonical identity authority is preserved |
| SR-06 | Compiler and QA release contracts are consistent |
| SR-07 | Adapter loss disclosure is mandatory |
| SR-08 | Compatibility claims do not exceed evidence |
| SR-09 | Migration guide is complete |
| SR-10 | No critical unresolved release failure exists |

## Release result

A stable release passes only when all mandatory gates pass. Missing empirical image evidence is allowed only when the release explicitly avoids empirical image-equivalence claims.
