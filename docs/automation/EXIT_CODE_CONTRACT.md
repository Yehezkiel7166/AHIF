# Exit-Code Contract

| Status | Exit | Meaning |
|---|---:|---|
| PASS | 0 | All applicable repository checks passed. |
| HOLD | 0 | Checks passed, but governance evidence forbids a positive release or LTS designation. |
| FAIL | 1 | Configuration, evidence, or repository state is malformed or nonconformant. |
| INTERNAL_ERROR | 2 | The verifier itself could not execute correctly. |

Missing operational/LTS evidence is `HOLD`; missing required repository evidence, including stale generated reports, is `FAIL`. Runtime defects are never downgraded to warnings. The exact mapping is validated from shared configuration.
