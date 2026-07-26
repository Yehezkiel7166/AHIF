# Release Eligibility

## Eligibility states

- `released` — all mandatory contracts pass.
- `released_with_warnings` — mandatory gates pass and only non-blocking warnings remain.
- `blocked_recoverable` — execution can continue after a defined upstream correction.
- `blocked_input_required` — required user or asset input is missing.
- `blocked_critical` — identity or safety failure prohibits release.

## Mandatory release checks

| Check | Minimum |
|---|---|
| Identity QA | Pass, no critical identity code |
| Reasoning QA | Meets identity floor and causal completeness |
| Compiler QA | No blocking contradiction or invented directive |
| Context QA | Required context resolved or explicitly assumed |
| Human realism QA | No severe anatomy or physics risk |
| Output contract | Schema-valid and section-complete |

Aggregate scoring cannot override a mandatory failure.
