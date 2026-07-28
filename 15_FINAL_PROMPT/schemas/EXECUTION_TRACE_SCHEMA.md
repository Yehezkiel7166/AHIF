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
        "required": ["stage"],
        "properties": {
          "stage": {"type": "string"},
          "status": {"enum": ["pass", "warning", "fail", "blocked", "recovered"]},
          "contract": {"type": "string"},
          "input_artifact": {"type": ["string", "null"]},
          "output_artifact": {"type": ["string", "null"]},
          "confidence": {"type": ["number", "null"], "minimum": 0, "maximum": 1},
          "codes": {"type": "array", "items": {"type": "string"}},
          "execution_order": {"type": "integer", "minimum": 1},
          "input_summary": {"type": "object"},
          "output_summary": {"type": "object"},
          "execution_status": {"enum": ["pass", "warning", "blocked", "fail"]},
          "validation_status": {"enum": ["valid", "invalid"]},
          "timestamp": {"type": "string"},
          "warnings": {"type": "array", "items": {"type": "string"}},
          "errors": {"type": "array", "items": {"type": "string"}},
          "contract_version": {"type": "string"},
          "recovery_path": {"type": "string"},
          "escalation_path": {"type": "string"}
        },
        "anyOf": [
          {"required": ["status", "contract", "input_artifact", "output_artifact"]},
          {"required": ["execution_order", "input_summary", "output_summary", "execution_status", "validation_status", "timestamp", "warnings", "errors", "contract_version", "recovery_path", "escalation_path"]}
        ],
        "additionalProperties": false
      }
    }
  },
  "additionalProperties": false
}
```
