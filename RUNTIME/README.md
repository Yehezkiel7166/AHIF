# AHIF Executable Framework

`Framework.execute()` is the one canonical public execution interface for AHIF
3.5.0. The compatibility function `execute_framework()` and the command-line
interface delegate directly to it; they do not implement alternate pipelines.

The framework performs no network calls and does not execute an image model. It
deterministically normalizes context, locks the supplied canonical identity,
loads registered knowledge, makes priority-ordered decisions, creates the
explainable (non-chain-of-thought) reasoning handoff, compiles, performs
mandatory QA, packages the final prompt, and prepares an adapter request.

## Quick start

```python
from RUNTIME import Framework

request = {
    "user_request": {
        "location": "Kyoto, Japan",
        "place": "Gion district",
        "atmosphere": "calm autumn morning",
    },
    "identity": {
        "canonical_asset": "assets/identity-reference/MASTER_PHOTO.jpg",
    },
    "adapter_id": "ahif.openai-images.v1",
}
result = Framework.execute(request)
print(result["final_prompt"])
print(result["execution_report"])
```

Execute a repository scenario with one command:

```sh
python3 -m RUNTIME 13_EXAMPLES/runtime/KYOTO_AUTUMN.json
```

## Input object

The object requires `user_request`, `identity`, and `adapter_id`.
`user_request` requires non-empty `location`, `place`, and `atmosphere`; it may
also carry activity, weather, time, season, and string constraints. `identity`
requires `canonical_asset`. `execution_timestamp` is optional and defaults to a
stable epoch value to preserve reproducibility.

## Output object and execution report

The result contains the execution trace and pipeline state, decision and
reasoning outputs, compiled prompt, QA report, final prompt, adapter request,
metadata, and the backward-compatible 3.4 package fields. The machine-readable
`execution_report` includes version and execution ID, ordered stages and their
statuses, warnings, errors, deterministic logical timing, validation, recovery
events, output availability, and final state. Trace summaries disclose field
metadata rather than private reasoning content.

## State machine and error handling

The only legal sequence is:

`INITIALIZED -> CONTEXT_READY -> IDENTITY_LOCKED -> KNOWLEDGE_READY ->
DECISION_COMPLETE -> REASONING_COMPLETE -> PROMPT_COMPILED -> QA_COMPLETE ->
FINAL_PACKAGE_READY -> ADAPTER_READY -> FINISHED`.

Every trace stage records input, output, validation, errors, recovery events,
execution state, and its transition rule. Invalid boundary input raises
`RuntimeContractError`. QA or adapter policy blocks are returned as structured
blocked results; a blocked QA package cannot reach a prepared adapter request.
Recovery is deterministic normalization or correction of the earliest
responsible input followed by a new run.

Runtime conformance is not empirical model validation, production readiness,
release eligibility, or an LTS designation. Existing Release Eligibility and
LTS HOLD decisions are unchanged.
