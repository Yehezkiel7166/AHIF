# OpenAI Images Adapter

## Identifier

`ahif.openai-images.v1` — adapter version `1.0.0`.

## Strategy

The adapter preserves AHIF's natural-language prompt as a coherent instruction block, binds the canonical identity image through the target's supported image input workflow, maps requested output geometry through declared size controls, and serializes negative constraints as explicit avoidance instructions because a dedicated negative-prompt field is not assumed.

## Identity Policy

Production-equivalent output requires an attached canonical identity image. Text-only identity reconstruction is marked `degraded` and cannot pass production release gating.

## Output Shape

The target request contains model selection supplied by runtime configuration, prompt, image reference metadata when present, output size or aspect representation, quality controls when declared, and provenance metadata retained outside the vendor request.

## External Capability Snapshot

This adapter uses the date-stamped capability profile. Runtime implementations must revalidate the target documentation before changing supported fields.
