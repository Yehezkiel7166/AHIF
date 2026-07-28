"""Single canonical sequential AHIF execution engine."""
from __future__ import annotations
import hashlib
import json
from typing import Any, Callable, Mapping
from .adapter import prepare_model_adapter
from .compiler import compile_prompt
from .context import load_context
from .contracts import RUNTIME_VERSION, StageResult, Status, require_mapping, trace_record
from .decision import run_decision
from .final_prompt import generate_final_prompt
from .identity import lock_identity
from .knowledge import load_knowledge
from .qa import run_quality_assurance
from .reasoning import run_reasoning

DEFAULT_TIMESTAMP = "1970-01-01T00:00:00Z"


def execute_framework(request: Mapping[str, Any]) -> dict[str, Any]:
    """Execute all architecture stages without invoking an external model."""
    source = require_mapping(request, "request")
    timestamp = source.get("execution_timestamp", DEFAULT_TIMESTAMP)
    if not isinstance(timestamp, str) or not timestamp.endswith("Z"):
        from .errors import RuntimeContractError
        raise RuntimeContractError("execution_timestamp must be an RFC 3339 UTC string ending in Z")
    canonical = json.dumps(source, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    execution_id = "AHIF-EXEC-" + hashlib.sha256(canonical.encode()).hexdigest()[:16].upper()
    trace, state = [], {}

    def run(name: str, input_value: Mapping[str, Any], function: Callable[[Mapping[str, Any]], StageResult]) -> StageResult:
        result = function(input_value)
        trace.append(trace_record(name, len(trace) + 1, input_value, result, timestamp))
        state[name] = result.output
        return result

    context = run("context", source["user_request"], load_context)
    identity = run("identity", source["identity"], lock_identity)
    knowledge = run("knowledge", context.output, load_knowledge)
    decision = run("decision", {"context": context.output, "knowledge": knowledge.output}, run_decision)
    reasoning = run("reasoning", {"decision": decision.output, "identity": identity.output}, run_reasoning)
    compiled = run("compiler", reasoning.output, compile_prompt)
    qa = run("qa", compiled.output, run_quality_assurance)
    final = run("final_prompt", {"compiled": compiled.output, "qa": qa.output}, generate_final_prompt)
    adapter = run("adapter", {"final_prompt": final.output, "adapter_id": source["adapter_id"]}, prepare_model_adapter)
    statuses = [item["execution_status"] for item in trace]
    overall = "fail" if "fail" in statuses else "blocked" if "blocked" in statuses else "warning" if "warning" in statuses else "pass"
    return {"execution_id": execution_id, "framework_version": RUNTIME_VERSION,
            "execution_trace": {"execution_id": execution_id, "framework_version": RUNTIME_VERSION, "stages": trace},
            "pipeline_state": state, "validation_state": {"status": overall, "qa": qa.output},
            "final_prompt_package": final.output, "adapter_package": adapter.output}
