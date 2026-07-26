# End-to-End Validation

## Purpose

End-to-end validation verifies that compact input can travel through the entire AHIF pipeline without loss of identity, unsupported invention, contradiction, or output-contract failure.

## Validation path

```text
Compact input
→ normalized context
→ grounded decisions
→ accepted reasoning
→ compiler plan
→ compiled prompt
→ QA report
→ release decision
```

## Required invariants

- the master photo remains the sole canonical identity
- every material prompt directive traces to accepted reasoning
- explicit user constraints remain represented
- rejected alternatives never reappear
- compiler ordering is deterministic
- negative constraints correspond to observed risks
- QA findings use stable rule and failure codes
- repair actions are traceable
- release output contains final prompt, negative constraints, and QA summary

## Failure behavior

The pipeline must stop rather than produce a final prompt when identity, evidence, contradiction, or output completeness gates fail.
