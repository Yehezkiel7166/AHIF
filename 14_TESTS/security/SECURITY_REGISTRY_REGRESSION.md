# Security Registry Regression

Validate that:
- prior finding and provenance records are immutable;
- record counts match array lengths;
- event sequence and previous fingerprints are continuous;
- expired exceptions are noncompliant;
- `not-evaluated` cannot be rendered as pass;
- no raw secret-like value appears in registries;
- release eligibility is blocked for unresolved critical/high reachable findings or unknown executable provenance.
