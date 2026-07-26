# QA Report Contract

## Required fields

```yaml
qa_report_id: string
framework_version: 1.5.0
input_fingerprint: string
status: pass|revise|fail
release_eligible: boolean
mandatory_gates:
  identity: pass|fail
  anatomy_physics: pass|fail
  context_culture: pass|fail
  compiler_integrity: pass|fail
  output_contract: pass|fail
scores:
  identity_fidelity: 0-100
  anatomy_physics: 0-100
  context_environment: 0-100
  cultural_appropriateness: 0-100
  photography_lighting: 0-100
  styling_continuity: 0-100
  story_coherence: 0-100
  compiler_integrity: 0-100
  output_completeness: 0-100
  aggregate: 0-100
findings:
  - code: string
    lint_rule: string|null
    severity: critical|error|warning|info
    component: string
    evidence: string
    repairable: boolean
    recovery_level: R0|R1|R2|R3|R4|R5|R6
    action: string
repairs: []
validation_provenance: []
```

## Privacy boundary

The report may expose concise validation evidence and decision summaries. It must not expose private chain-of-thought.

## Release rule

`release_eligible` is true only when status is `pass`, all mandatory gates pass, and no critical, error, or warning marked as blocking remains.
