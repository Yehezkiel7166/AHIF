# Rule Resolver

The rule resolver collects candidate decisions, detects contradictions, and selects the safest coherent set.

## Resolution sequence

1. remove prohibited choices
2. enforce identity constraints
3. enforce anatomy and physics
4. enforce culture and environment
5. honor explicit user choices
6. remove conflicting secondary choices
7. select the highest-confidence coherent option
8. simplify when uncertainty remains
