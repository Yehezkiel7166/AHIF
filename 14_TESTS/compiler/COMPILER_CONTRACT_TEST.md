# Prompt Compiler Contract Test

## Contract assertions

1. compiler rejects `blocked` and `revision-required` reasoning status
2. every compiler unit references an accepted reasoning chain
3. canonical identity section is first
4. section ordering is deterministic
5. one material statement cannot originate from an unsupported source
6. contradictions are reported rather than hidden
7. visible prompt excludes internal reasoning IDs and explanations
8. negative constraints are relevant and non-conflicting
9. metadata identifies compiler version and source chains
10. output conforms to `COMPILED_PROMPT_SCHEMA.md`

A release cannot pass when any assertion fails.
