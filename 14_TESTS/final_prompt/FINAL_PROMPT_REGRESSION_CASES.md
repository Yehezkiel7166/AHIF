# Final Prompt Regression Cases

## FP-001 Identity-critical failure

A compiled prompt changes ethnicity relative to the canonical master photo.

Expected: `blocked_critical`; no final prompt released.

## FP-002 Weather-fashion contradiction

Cold rain context is paired with exposed summer styling.

Expected: route to decision or reasoning recovery; do not patch only at serialization.

## FP-003 Compiler invention

The compiler adds jewelry not present in accepted decisions.

Expected: compiler-integrity failure and recompilation from the same reasoning record.

## FP-004 Warning-only release

A low-confidence optional color decision remains but all mandatory gates pass.

Expected: `released_with_warnings` with explicit warning code.

## FP-005 Missing canonical asset

The execution environment does not bind a canonical master photo.

Expected: `blocked_input_required`.

## FP-006 Deterministic replay

Identical normalized input and framework version are executed twice.

Expected: identical decision order, reasoning structure, prompt section order, and release state.
