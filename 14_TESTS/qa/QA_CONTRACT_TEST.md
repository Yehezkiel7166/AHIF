# QA Contract Test

## Contract assertions

A conforming QA Engine must:

1. reject a package without canonical identity lock
2. reject unsupported material facts
3. detect unresolved contradictions
4. produce stable lint and failure codes
5. separate mandatory gates from aggregate scoring
6. preserve the identity override
7. assign a recovery level to every blocking finding
8. rerun affected gates after repair
9. emit a complete machine-readable QA report
10. release only a `pass` artifact

## Determinism assertion

Repeated validation of an unchanged normalized package must produce the same status, mandatory-gate results, triggered deterministic lint rules, and aggregate score.
