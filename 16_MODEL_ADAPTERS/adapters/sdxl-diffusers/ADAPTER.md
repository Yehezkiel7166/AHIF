# SDXL Diffusers Adapter

## Identifier

`ahif.sdxl-diffusers.v1` — adapter version `1.0.0`.

## Strategy

The adapter emits a deterministic Diffusers-oriented invocation object containing positive prompt, negative prompt, geometry, inference controls, generator seed metadata, and an explicitly declared conditioning pipeline when image identity conditioning is used.

## Identity Policy

Base text-to-image SDXL alone is not treated as a native identity-reference mechanism. Production identity preservation requires a declared image-conditioning implementation whose provenance and strength are recorded. Otherwise the result is experimental and degraded.

## Output Shape

- `prompt`;
- `negative_prompt`;
- `width` and `height`;
- `guidance_scale` when governed;
- `num_inference_steps` when governed;
- generator seed metadata;
- optional image-conditioning configuration;
- scheduler and model identifiers supplied by runtime configuration.
