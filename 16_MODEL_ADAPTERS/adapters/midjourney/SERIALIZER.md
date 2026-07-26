# Midjourney Prompt Serializer

## Prompt Body

The prompt body remains descriptive prose. It prioritizes subject identity, human realism, action, environment, and photography before aesthetic finish.

## Parameter Suffix

The suffix may include only profile-declared controls such as aspect ratio, seed, raw/style behavior, reference bindings, or negative exclusions. Parameter order is deterministic.

## Negative Mapping

Canonical negative constraints are deduplicated and translated into the target's exclusion mechanism. Identity-critical exclusions remain concise and must not accidentally negate canonical facial traits.

## Failure Rules

Block when the identity reference cannot be attached, an obsolete parameter is requested, the target version is ambiguous for a reproducible run, or parameter limits force loss of identity-critical meaning.
