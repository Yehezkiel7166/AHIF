# Incident Registry Governance

The incident registry is append-only and begins with zero incidents.

## Required properties

- globally unique `incident_id`;
- immutable scope fingerprint;
- links to release execution and observation records;
- ordered event sequence with previous-event hash;
- explicit actor role and timestamp;
- severity and status transitions governed by the event schema;
- closure requires independent validation and authorization.

## States

`opened`, `triaged`, `containment_authorized`, `contained`, `recovery_authorized`, `recovering`, `validation`, `resolved`, `closed`, `blocked`, `cancelled`.

Events are never rewritten or deleted. Corrections are appended as superseding events.
