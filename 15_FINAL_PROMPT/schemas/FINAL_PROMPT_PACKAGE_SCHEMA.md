# Final Prompt Package Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "AHIF Final Prompt Package",
  "type": "object",
  "required": [
    "execution_id",
    "framework_version",
    "status",
    "release_eligible",
    "final_prompt",
    "negative_constraints",
    "identity_binding",
    "execution_summary",
    "validation_summary",
    "provenance"
  ],
  "properties": {
    "execution_id": {"type": "string", "pattern": "^AHIF-EXEC-"},
    "framework_version": {"type": "string"},
    "status": {"enum": ["released", "released_with_warnings", "blocked_recoverable", "blocked_input_required", "blocked_critical"]},
    "release_eligible": {"type": "boolean"},
    "final_prompt": {"type": ["string", "null"]},
    "negative_constraints": {"type": "array", "items": {"type": "string"}},
    "identity_binding": {"type": "object"},
    "execution_summary": {"type": "object"},
    "validation_summary": {"type": "object"},
    "provenance": {"type": "object"}
  },
  "allOf": [
    {
      "if": {"properties": {"release_eligible": {"const": true}}},
      "then": {"properties": {"final_prompt": {"type": "string", "minLength": 1}}}
    },
    {
      "if": {"properties": {"release_eligible": {"const": false}}},
      "then": {"properties": {"final_prompt": {"type": "null"}}}
    }
  ],
  "additionalProperties": false
}
```
