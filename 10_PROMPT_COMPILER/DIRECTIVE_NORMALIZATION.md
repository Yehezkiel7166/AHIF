# Directive Normalization

## Compiler unit

Each accepted reasoning directive is normalized into:

```yaml
id: string
source_reasoning_chain: string
domain: identity|scene|activity|human|styling|environment|photography|lighting|story|realism|negative
priority: integer
statement: string
constraints: []
confidence: number
provenance: []
required: boolean
```

## Normalization rules

1. preserve the decision's factual meaning
2. remove internal reasoning language from visible prompt text
3. retain causal implications that affect visual generation
4. split compound directives only when each part remains independently traceable
5. normalize synonymous vocabulary to the repository glossary
6. reject directives that contain unsupported additions
7. mark identity, required user constraints, and safety controls as non-droppable

## Examples of valid transformation

- Internal: `Cold morning and walking activity justify a structured wool coat.`
- Compiler unit: `She wears a structured wool coat appropriate for the cold morning walk.`

The compiler expresses the accepted result. It does not expose hidden reasoning traces.
