# Dashboard Publication Contract

A dashboard is a projection of signed metric snapshots, not a source of truth.

Every published panel must expose:

- metric identifier and specification version;
- snapshot identifier and calculation fingerprint;
- numerator, denominator, unit, and status;
- source window and freshness;
- exclusions and data-quality warnings;
- threshold version;
- reviewer and publication state;
- link to the immutable source snapshot.

Draft, blocked, invalid, and not-evaluated states must remain visible. Dashboard exports may not imply production health, model superiority, or empirical certification unless separately supported by governed external evidence.
