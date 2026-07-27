# Security Exception Schema

Required fields:
- exception ID and affected rule/finding IDs;
- exact assets and versions;
- justification and compensating controls;
- owner role, approver role, start, expiry, review interval;
- revocation conditions;
- immutable fingerprint.

An expired exception is invalid without a new independently approved record.
