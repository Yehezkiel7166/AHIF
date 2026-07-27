# Recovery Objectives Policy

Every governed service profile must declare:

- recovery time objective (RTO);
- recovery point objective (RPO);
- maximum tolerable disruption (MTD);
- measurement start and stop events;
- authoritative clock and timezone;
- data classes covered and excluded;
- dependency assumptions;
- owner and approver;
- review and expiry date.

Unknown values must remain `not-defined`; they must not be converted to zero or an implied guarantee. Conflicts are resolved conservatively in favor of the stricter objective, then escalated for governance approval.
