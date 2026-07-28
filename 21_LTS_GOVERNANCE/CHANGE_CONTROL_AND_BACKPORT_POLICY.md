# Change Control and Backport Policy

## Change classes

| Class | Examples | LTS treatment |
|---|---|---|
| corrective | typo, broken reference, inaccurate metadata | allowed after validation |
| security | verified vulnerability or secret-handling correction | expedited but fully evidenced |
| compatibility | non-breaking parser, schema, or documentation correction | allowed after regression review |
| additive | optional backward-compatible capability | requires explicit risk and compatibility review |
| breaking | removed field, changed invariant, incompatible semantics | prohibited on an existing LTS line |

## Backport gate

A backport requires an originating change, target line, exact patch, dependency analysis, compatibility assessment, test evidence, claim-boundary review, independent approval, rollback instructions, and append-only event. Cherry-pick success alone is not validation.

Any unresolved conflict, missing evidence, schema break, identity risk, registry rewrite, or unsupported claim produces `hold` or `rejected`. A backport event does not assert deployment or production use.
