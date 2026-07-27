# Artifact Integrity Policy

## Digest standard

AHIF uses SHA-256 for artifact fingerprints. Each artifact declaration includes:

- relative path or external object reference;
- media type;
- byte size;
- SHA-256 digest;
- capture role;
- availability state.

## Artifact roles

- `canonical_input_reference` — reference to the owner-supplied master photo; bytes need not be committed;
- `prompt_package` — released AHIF prompt package;
- `target_request` — exact serialized model request;
- `generated_output` — externally generated image;
- `execution_log` — provider or local execution metadata;
- `evaluation_report` — identity or semantic evaluation record.

## Verification states

- `verified_bytes` — digest recomputed from available bytes;
- `declared_only` — digest declared but bytes unavailable;
- `mismatch` — recomputed digest differs;
- `unavailable` — required artifact reference cannot be resolved.

Only `verified_bytes` artifacts can satisfy strict reproducibility gates. `declared_only` evidence may be quarantined for later completion.

## Safety

Artifact paths must be relative, normalized, and traversal-free. Executable attachments are not required by AHIF evidence contracts and should be rejected unless explicitly governed by a future policy.