# Provenance Record Schema

Required fields:

- stable record and asset identifiers;
- asset type, version, origin, and acquisition method;
- supplier or maintainer identity as declared;
- license disposition;
- checksum algorithm and digest when available;
- approval disposition and constraints;
- supersession link;
- reviewer and record fingerprint.

A missing checksum must be represented as `unavailable` with a reason, never as a fabricated digest.
