# Sprint 015 — Evidence Ingestion and Registry Governance

## Version

2.3.0

## Objective

Add a deterministic, append-only path for accepting user-supplied external execution evidence while preserving AHIF identity authority, stable adapter contracts, and human-controlled promotion governance.

## Delivered

- I0–I8 evidence ingestion pipeline;
- artifact integrity and checksum policy;
- append-only evidence registry governance;
- ingestion request, result, and registry schemas;
- zero-evidence machine-readable registry baseline;
- ingestion QA and stable `AHIF-ING` failure codes;
- contract and registry regression tests;
- illustrative quarantined ingestion request.

## Claim boundary

No external image bytes, provider executions, empirical scores, or accepted evidence records are included. All adapter tiers remain unchanged.

## Compatibility

Backward compatible with AHIF 2.2.0. No previous contract or file is removed.