# Midjourney Adapter

## Identifier

`ahif.midjourney.v1` — adapter version `1.0.0`.

## Strategy

The adapter serializes the canonical prompt as one ordered natural-language prompt followed by a governed parameter suffix. Parameters are isolated from semantic content. Identity reference syntax is attached only through a capability declared by the active Midjourney snapshot.

## Identity Policy

The canonical master photo must be bound through an approved reference mechanism. Style reference and identity reference are treated as separate semantic channels and must never share a role.

## Output Shape

- ordered prompt text;
- optional identity reference binding;
- optional style reference binding;
- aspect-ratio parameter;
- controlled variation and seed parameters when requested;
- negative constraint translation;
- exact target-version selection when reproducibility requires it.
