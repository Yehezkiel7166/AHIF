# Knowledge Provenance Regression

## Scenarios

### Missing source

A package references a deleted or renamed canonical module.

Expected: `AHIF-KNOW-003`, status `fail`.

### Duplicate identifier

Two records publish `AHIF-KG-PHOTO-0001`.

Expected: `AHIF-KNOW-002`, status `fail`.

### Semantic expansion

A structured record claims a cultural rule absent from its cited source.

Expected: `AHIF-KNOW-004`, status `fail`.

### Identity weakening

An adapter hint allows face redesign for target compatibility.

Expected: `AHIF-KNOW-005` or `AHIF-KNOW-008`, status `fail`.

### Safe editorial update

A record label is clarified without changing conditions, effects, constraints, or provenance.

Expected: identifier retained; package patch version incremented; status `pass`.
