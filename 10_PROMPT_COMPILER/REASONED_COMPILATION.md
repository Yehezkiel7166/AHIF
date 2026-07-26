# Reasoned Compilation

The compiler must not concatenate keywords or resolve major visual choices independently.

## Required input

A `compiler-ready` result conforming to `schemas/REASONING_OUTPUT_SCHEMA.md`.

## Required behavior

1. use only accepted decisions and compiler directives
2. preserve canonical identity instructions at the beginning
3. group related human, environment, fashion, behavior, and photography instructions
4. remove duplicates without removing meaning
5. reject contradictions rather than hiding them
6. describe one coherent scene
7. retain realism and environment interaction
8. place negative constraints after the positive scene definition
9. keep the prompt readable and model-adaptable

## Prohibited behavior

- introducing unsupported clothing, location, weather, activity, or identity details
- selecting a rejected alternative
- compiling a blocked reasoning result
- converting uncertainty into a false fact

The final prompt is an expression of resolved reasoning, not a new decision surface.
