# Disaster Declaration Policy

A disaster declaration requires a scoped trigger, affected capability, severity, decision authority, timestamp, communications owner, and explicit exit criteria.

Permitted states are `suspected`, `declared`, `contained`, `recovering`, `restored`, `closed`, and `blocked`. State transitions are append-only. Incident severity alone does not authorize destructive recovery actions.

A declaration must not be inferred from missing telemetry. Unknown state remains unknown and is escalated.
