# Execution Trace Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "AHIF Execution Trace",
  "type": "object",
  "required": ["execution_id", "framework_version", "stages"],
  "properties": {
    "execution_id": {"type": "string"},
    "framework_version": {"type": "string"},
    "stages": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["stage", "status", "contract", "input_artifact", "output_artifact"],
        "properties": {
          "stage": {"pattern": "^F[0-7]$"},
          "status": {"enum": ["pass", "warning", "fail", "blocked", "recovered"]},
          "contract": {"type": "string"},
          "input_artifact": {"type": ["string", "null"]},
          "output_artifact": {"type": ["string", "null"]},
          "confidence": {"type": ["number", "null"], "minimum": 0, "maximum": 1},
          "codes": {"type": "array", "items": {"type": "string"}}
        },
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```
