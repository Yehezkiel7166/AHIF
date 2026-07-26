# Negative Constraint Synthesis

## Principle

Negative constraints are risk controls, not a generic keyword dump.

## Sources

Select constraints from:

- canonical identity risks
- reasoning QA flags
- scene-specific anatomy and physics risks
- environmental and cultural risks
- camera and rendering risks
- model-neutral baseline failures

## Ordering

1. identity failures
2. anatomy and hand failures
3. physical interaction failures
4. environment and lighting failures
5. styling and cultural failures
6. rendering artifacts

## Rules

- include only relevant failure modes
- use concise, non-contradictory terms
- do not negate a required positive instruction
- avoid excessive negatives that compete with the scene description
- retain identity drift, generic-face substitution, facial redesign, ethnicity drift, and age drift in every identity-critical generation
- adapters may translate syntax in version 2.0, but cannot remove canonical protections
