# Security Snapshot Specification

A security snapshot is an immutable inventory of the governed repository state.

It includes:
- repository version and archive or commit fingerprint;
- exact path inventory;
- dependency and artifact provenance references;
- applicable rule-set and schema versions;
- exclusions and their justification;
- finding identifiers and dispositions;
- validator identity and validation tool versions;
- cryptographic snapshot fingerprint.

A snapshot contains no raw secret values and no fabricated external scan result.
