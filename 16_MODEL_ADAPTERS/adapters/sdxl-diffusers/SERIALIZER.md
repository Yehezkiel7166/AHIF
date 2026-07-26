# SDXL Diffusers Request Serializer

## Positive Prompt

Canonical sections are serialized as structured natural language rather than an ungoverned keyword pile. Identity and realism clauses appear first.

## Negative Prompt

Negative constraints are emitted through the dedicated field. The serializer removes duplicates, avoids mutually exclusive negatives, and preserves anatomy and identity protection terms.

## Numeric Controls

Guidance scale and inference steps are runtime-profile values, not aesthetic guesses. Width and height must satisfy the runtime model's declared constraints. Seed metadata is deterministic when requested.

## Conditioning

Image-to-image, adapter, control, or other conditioning is accepted only when the exact pipeline is declared in runtime configuration. Undeclared conditioning fields are rejected.
