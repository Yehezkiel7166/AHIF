# Reasoning Quality Assurance

## Gate criteria

A reasoning result passes only when:

- canonical identity premises are present
- every major decision has evidence and a causal reason
- alternatives are evaluated where material
- domain conflicts are resolved
- confidence thresholds are satisfied
- uncertainty is handled explicitly
- compiler directives are complete and non-contradictory

## Failure codes

| Code | Meaning |
|---|---|
| `RQA-001` | missing canonical identity premise |
| `RQA-002` | unsupported material decision |
| `RQA-003` | circular or non-causal explanation |
| `RQA-004` | unresolved cross-domain conflict |
| `RQA-005` | identity confidence below floor |
| `RQA-006` | fabricated premise or provenance |
| `RQA-007` | compiler directive introduces a new decision |
| `RQA-008` | material uncertainty concealed |
| `RQA-009` | rejected alternative lacks reason |
| `RQA-010` | reasoning result is not deterministic enough for regression |

## Outcome

- zero blocking failures: pass
- correctable non-blocking failure: revision required
- identity, provenance, or coherence failure: blocked
