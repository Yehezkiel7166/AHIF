# Supply Chain Provenance Policy

Every dependency, external artifact, generated package, and imported reference must have a provenance record containing an identifier, version, origin, acquisition method, license status, integrity fingerprint when available, and governance disposition.

## Allowed dispositions

- `approved`
- `conditionally-approved`
- `quarantined`
- `rejected`
- `unknown`

`unknown`, `quarantined`, and `rejected` items cannot enter a releasable package. Conditional approval must include scope, expiry, compensating controls, and an accountable approver role.

## Integrity requirements

- Prefer cryptographic checksums from an independent trusted source.
- Record the algorithm and exact digest.
- Never treat file name, download URL, or modification date as sufficient integrity evidence.
- Generated archives require reproducible file lists and package checksums.
- A changed artifact requires a new provenance record rather than mutation of the prior record.
