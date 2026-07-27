# Evidence Bundle Contract

## Required bundle contents

Every empirical validation bundle must include:

- unique evidence bundle identifier;
- AHIF framework version;
- Final Prompt Package identifier and checksum;
- adapter identifier and version;
- target capability-profile identifier;
- exact serialized request;
- execution timestamp in UTC;
- target service or runtime version when observable;
- parameter set and seed policy;
- canonical identity asset checksum;
- generated-output checksums;
- evaluator identity or evaluator-system identifier;
- identity evaluation report;
- semantic evaluation report;
- reproducibility status;
- disclosure of missing or unverifiable metadata.

## Immutability

An accepted bundle is immutable. Corrections create a new bundle linked through `supersedes`.

## Evidence states

- `draft` — incomplete and not eligible for scoring.
- `complete` — required fields present.
- `reviewed` — independent review completed.
- `accepted` — passes evidence-integrity gates.
- `rejected` — invalid, contradictory, or unverifiable.
- `superseded` — replaced by a newer bundle.

## Missing metadata

Unknown values must be recorded as `unknown` with an explanation. They must never be inferred silently.

## Storage

Binary image files may be stored outside the repository. The repository stores stable references, checksums, and evaluation records. Private URLs, credentials, and expiring access tokens are prohibited.
