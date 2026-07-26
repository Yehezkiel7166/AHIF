# Execution Trace

## Trace purpose

The execution trace provides a maintainable audit path across AHIF modules. It records state transitions and contract outcomes, not private chain-of-thought.

## Trace record

Each stage appends:

- stage identifier;
- input artifact identifier;
- output artifact identifier;
- contract version;
- status;
- confidence band;
- warnings or failure codes;
- recovery route, when used;
- timestamp supplied by the execution host.

## Trace identifiers

Recommended identifiers:

- `AHIF-EXEC-*` for executions;
- `AHIF-CTX-*` for normalized contexts;
- `AHIF-DEC-*` for decision sets;
- `AHIF-RSN-*` for reasoning records;
- `AHIF-CMP-*` for compiled packages;
- `AHIF-QA-*` for QA reports;
- `AHIF-FP-*` for final prompt packages.
