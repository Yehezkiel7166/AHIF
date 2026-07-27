# Validation Evidence and Reproducibility

## Evidence bundle

A validation bundle binds:

- canonical input hashes;
- master-photo hash;
- knowledge registry and package versions;
- Final Prompt Package hash;
- adapter registry, adapter, serializer, and capability-profile versions;
- normalized target request hash;
- generation receipt or explicit `not_executed` state;
- output artifact hashes when available;
- evaluator and QA report identifiers.

## Reproducibility levels

- `R0 undocumented` — insufficient evidence;
- `R1 request_reproducible` — exact normalized request can be reproduced;
- `R2 execution_traceable` — external job and environment metadata are bound;
- `R3 output_reproducible` — target supports materially repeatable output under documented controls.

AHIF does not require all targets to reach R3. It requires the achieved level to be explicit.

## Evidence integrity

Hashes use SHA-256. Timestamps use UTC ISO 8601. Mutable URLs alone are not evidence. Secrets, private tokens, and biometric embeddings must not be committed.

## Expiration

Evidence expires when an adapter, serializer, capability profile, canonical package, evaluator protocol, or target behavior materially changes.

## Release rule

Stable model support requires current empirical evidence for the declared target version or capability snapshot. Contract-only evidence supports experimental or release-candidate status only.
