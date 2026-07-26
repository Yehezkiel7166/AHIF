# Prompt Compiler Regression Cases

## C-001 — Kyoto cold morning

Expected: identity lock, calm walking activity, cold-weather styling, coherent autumn environment, moderate environmental portrait perspective, soft morning light, and relevant negatives.

## C-002 — Tokyo rain at night

Expected: physically plausible rain interaction, controlled practical lighting, wet-surface reflections, stable identity visibility, and no sunlight contradiction.

## C-003 — Conflicting lighting directives

Input contains direct noon sun and diffuse overcast lighting.

Expected: `revision-required`; no final prompt.

## C-004 — Unsupported accessory

Reasoning input does not authorize an umbrella, but a compiler directive introduces one.

Expected: `blocked` or `revision-required` with unsupported-fact diagnostic.

## C-005 — Duplicate identity language

Equivalent identity statements appear in multiple accepted directives.

Expected: consolidated identity lock with no loss of canonical protections.

## C-006 — Multiple dominant activities

Input contains cycling and seated café dining as simultaneous primary actions.

Expected: contradiction diagnostic; no hidden merge.

## C-007 — High-risk facial obstruction

Reasoning permits a scarf but requires face visibility.

Expected: compiler states the scarf remains below the lower face and preserves recognizability.

## C-008 — Deterministic recompilation

The same normalized reasoning record is compiled twice.

Expected: identical section plan and semantically equivalent prompt package.
