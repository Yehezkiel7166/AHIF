# Execution Request Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "AHIF Execution Request",
  "type": "object",
  "required": ["location", "place", "atmosphere", "output_type"],
  "properties": {
    "location": {"type": "string", "minLength": 1},
    "place": {"type": "string", "minLength": 1},
    "atmosphere": {"type": "string", "minLength": 1},
    "output_type": {"const": "final_image_generation_prompt"},
    "time": {"type": ["string", "null"]},
    "season": {"type": ["string", "null"]},
    "weather": {"type": ["string", "null"]},
    "activity": {"type": ["string", "null"]},
    "constraints": {"type": "array", "items": {"type": "string"}},
    "canonical_identity_asset": {"type": ["string", "null"]}
  },
  "additionalProperties": false
}
```
