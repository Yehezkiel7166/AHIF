# Sprint 028 — Automation Stabilization

AHIF **3.2.1** is a patch release because this sprint consolidates and corrects the existing Sprint 025–027 automation without adding a new public framework capability. Shared configuration, a canonical engine, report hygiene, deterministic self-tests, and CI reliability reduce duplication while preserving compatible Make and script entry points.

The mandatory flow was INSPECT → RED (audit findings and new negative requirements) → GREEN (canonical implementation) → REGRESSION → AUDIT → COMMIT → DRAFT PR. Architecture findings are preserved in `docs/automation/AUTOMATION_ARCHITECTURE.md`. The LTS designation remains **HOLD**. Canonical identity authority, adapter tiers, append-only histories, compatibility guarantees, and all production/operational claim boundaries are unchanged.
