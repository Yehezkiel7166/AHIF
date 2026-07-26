# Reasoning Trace Template

## Scene identifier

Use a stable identifier for the compilation request.

## Premises

List normalized user inputs, canonical identity constraints, and applicable knowledge evidence.

## Accepted decisions

For each major decision record:

```text
Decision ID:
Domain:
Decision:
Premises:
Constraints:
Reason:
Cross-domain effects:
Confidence:
Compiler directive:
```

## Rejected alternatives

```text
Alternative:
Rejection code:
Reason:
```

## Uncertainties

List unresolved facts, their materiality, and the chosen handling policy.

## Final status

One of:

- `compiler-ready`
- `revision-required`
- `blocked`
