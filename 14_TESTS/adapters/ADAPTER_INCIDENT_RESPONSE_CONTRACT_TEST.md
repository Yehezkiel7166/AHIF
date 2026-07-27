# Adapter Incident Response Contract Test

## Positive contract checks

- accepts an incident with valid release and observation references;
- preserves immutable scope and append-only event ordering;
- requires independent authorization before containment or recovery;
- supports restore, rollback, forward-fix, hold, no-action, and blocked paths;
- requires snapshot, fingerprint, QA, and residual-risk reconciliation before closure.

## Negative contract checks

- reject fabricated telemetry or actor identities;
- reject incident creation without release provenance;
- reject undeclared mutations and direct adapter-tier changes;
- reject rewritten event history;
- reject closure without validation and authorization;
- reject claims of production health based only on AHIF governance records.
