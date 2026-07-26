# Reasoning Handoff

## Contract

The Prompt Compiler consumes only decisions marked accepted by the Reasoning Engine.

## Handoff rules

1. preserve the order of compiler directives
2. place identity-lock directives before adaptive details
3. compile causal decisions into natural visual instructions, not internal explanations
4. do not include rejected alternatives in the final prompt
5. preserve uncertainty only when it materially affects generation
6. reject a `blocked` reasoning result
7. return a `revision-required` result to the decision layer

## Separation of concerns

The Reasoning Engine explains and validates decisions. The Prompt Compiler expresses those decisions as a coherent image-generation prompt. The compiler must not silently make new material decisions.
