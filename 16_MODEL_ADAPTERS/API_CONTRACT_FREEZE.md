# Adapter Contract Freeze

## Frozen contracts for 2.0

The following contract families are frozen for the 2.0 stable line:

- adapter registry entries;
- capability profiles;
- target request schema;
- transformation plan schema;
- adapter result schema;
- compatibility report schema;
- interoperability result schema;
- cross-model validation report schema;
- identity comparison report schema.

## Allowed changes

Backward-compatible additions are allowed when defaults preserve existing behavior. Existing stable fields may not change meaning.

## Prohibited changes

- removing required identity controls;
- changing a stable identifier's semantics;
- omitting loss disclosure;
- converting unsupported capabilities into silent approximations;
- promoting empirical support without evidence.

## Versioning

Contract changes must follow semantic versioning and include migration notes.
