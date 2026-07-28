# LTS Support and Maintenance Policy

## Required declaration

Each LTS candidate must declare:

- exact release and source commit;
- supported framework surfaces and explicit exclusions;
- compatibility baseline and supported predecessor lines;
- maintenance start, review cadence, and planned end conditions;
- responsible maintainer and independent reviewer roles;
- accepted change classes and security or resilience escalation paths;
- response targets, clearly labeled as targets rather than measured service levels;
- migration and supersession policy;
- evidence references and claim boundary.

## Support levels

Permitted repository support levels are `candidate`, `lts`, `maintenance`, `security-only`, `superseded`, and `retired`. A level describes governed repository treatment, not a commercial SLA or a continuously staffed service.

## Maintenance rules

Maintenance must preserve stable identifiers, canonical identity rules, schemas, registries, and public contracts. Corrections, security remediations, compatibility fixes, documentation clarifications, and validated non-breaking enhancements may be accepted. Breaking changes require a new major line and migration contract.

Unverified maintainer availability, response performance, or external deployment state must be recorded as `not-evaluated` and cannot be used to justify designation.
