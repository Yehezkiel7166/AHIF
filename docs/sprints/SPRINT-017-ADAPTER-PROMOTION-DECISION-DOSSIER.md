# Sprint 017 — Adapter Promotion Decision Dossier Governance

## Version

2.5.0

## Objective

Add a deterministic, auditable governance layer that converts completed evaluations and eligible aggregates into adapter promotion, hold, downgrade, or block recommendations while keeping authorization separate from adapter-registry mutation.

## Delivered

- P0–P9 adapter promotion decision dossier workflow;
- append-only promotion decision registry governance;
- dossier and decision-event schemas;
- zero-dossier machine-readable registry baseline;
- promotion dossier QA and stable `AHIF-PROMO` failure codes;
- contract and registry regression tests;
- illustrative blocked dossier example.

## Source-of-truth decision

Sprint 016 completed post-ingestion evaluation queue governance. The next unresolved governance boundary is how completed evaluations become support-tier decisions. Because the repository contains no owner-supplied model outputs, completed evaluation jobs, or eligible aggregates, Sprint 017 implements the decision mechanism and preserves a zero-decision baseline rather than fabricating promotion evidence.

## Claim boundary

No external generated-image evidence, completed evaluation jobs, promotion authorizations, reviewer identities, or adapter-tier changes are included.

## Compatibility

Backward compatible with AHIF 2.4.0. No previous contract or file is removed.
