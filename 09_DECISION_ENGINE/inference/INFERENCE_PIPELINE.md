# Inference Pipeline

```text
Raw user input
→ normalize terms
→ identify explicit constraints
→ load identity constraints
→ infer world context
→ infer weather/time behavior
→ infer activity
→ infer body language and expression
→ infer styling
→ infer environmental interaction
→ infer camera and lighting
→ construct story beat
→ score risk
→ resolve conflicts
→ compile prompt
→ run QA
```

Each stage may pass constraints forward but may not silently override higher-priority rules.
