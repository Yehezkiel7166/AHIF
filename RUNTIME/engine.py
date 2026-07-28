"""Single canonical sequential AHIF execution engine."""
from __future__ import annotations

import hashlib
import json
from typing import Any, Callable, Mapping

from .adapter import prepare_model_adapter
from .compiler import compile_prompt
from .context import load_context
from .contracts import (RUNTIME_VERSION, ExecutionState, StageResult,
                        require_mapping, trace_record)
from .decision import run_decision
from .final_prompt import generate_final_prompt
from .identity import lock_identity
from .knowledge import load_knowledge
from .qa import run_quality_assurance
from .reasoning import run_reasoning

DEFAULT_TIMESTAMP = "1970-01-01T00:00:00Z"

TRANSITIONS = (
    ("context", ExecutionState.INITIALIZED, ExecutionState.CONTEXT_READY),
    ("identity", ExecutionState.CONTEXT_READY, ExecutionState.IDENTITY_LOCKED),
    ("knowledge", ExecutionState.IDENTITY_LOCKED, ExecutionState.KNOWLEDGE_READY),
    ("decision", ExecutionState.KNOWLEDGE_READY, ExecutionState.DECISION_COMPLETE),
    ("reasoning", ExecutionState.DECISION_COMPLETE, ExecutionState.REASONING_COMPLETE),
    ("compiler", ExecutionState.REASONING_COMPLETE, ExecutionState.PROMPT_COMPILED),
    ("qa", ExecutionState.PROMPT_COMPILED, ExecutionState.QA_COMPLETE),
    ("final_prompt", ExecutionState.QA_COMPLETE, ExecutionState.FINAL_PACKAGE_READY),
    ("adapter", ExecutionState.FINAL_PACKAGE_READY, ExecutionState.ADAPTER_READY),
)


class Framework:
    """Public AHIF framework facade with the sole canonical execution method."""

    @staticmethod
    def execute(request: Mapping[str, Any]) -> dict[str, Any]:
        """Execute every AHIF stage without invoking an external model."""
        source = require_mapping(request, "request")
        for field in ("user_request", "identity", "adapter_id"):
            if field not in source:
                from .errors import RuntimeContractError
                raise RuntimeContractError(f"request.{field} is required")
        timestamp = source.get("execution_timestamp", DEFAULT_TIMESTAMP)
        if not isinstance(timestamp, str) or not timestamp.endswith("Z"):
            from .errors import RuntimeContractError
            raise RuntimeContractError("execution_timestamp must be an RFC 3339 UTC string ending in Z")
        canonical = json.dumps(source, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
        execution_id = "AHIF-EXEC-" + hashlib.sha256(canonical.encode()).hexdigest()[:16].upper()
        trace: list[dict[str, Any]] = []
        pipeline: dict[str, Any] = {}
        current = ExecutionState.INITIALIZED

        transition_by_name = {name: (before, after) for name, before, after in TRANSITIONS}

        def run(name: str, value: Mapping[str, Any],
                function: Callable[[Mapping[str, Any]], StageResult]) -> StageResult:
            nonlocal current
            before, after = transition_by_name[name]
            if current is not before:
                raise RuntimeError(f"illegal framework transition: {current.value} -> {after.value}")
            result = function(value)
            if not isinstance(result, StageResult):
                raise TypeError(f"{name} did not return StageResult")
            current = after
            trace.append(trace_record(name, len(trace) + 1, value, result, timestamp, before, after))
            pipeline[name] = dict(result.output)
            return result

        context = run("context", require_mapping(source["user_request"], "user_request"), load_context)
        identity = run("identity", require_mapping(source["identity"], "identity"), lock_identity)
        knowledge = run("knowledge", context.output, load_knowledge)
        decision = run("decision", {"context": context.output, "knowledge": knowledge.output}, run_decision)
        reasoning = run("reasoning", {"decision": decision.output, "identity": identity.output}, run_reasoning)
        compiled = run("compiler", reasoning.output, compile_prompt)
        qa = run("qa", compiled.output, run_quality_assurance)
        final = run("final_prompt", {"compiled": compiled.output, "qa": qa.output}, generate_final_prompt)
        adapter = run("adapter", {"final_prompt": final.output,
                                   "adapter_id": source["adapter_id"]}, prepare_model_adapter)
        current = ExecutionState.FINISHED

        statuses = [item["execution_status"] for item in trace]
        overall = ("fail" if "fail" in statuses else "blocked" if "blocked" in statuses
                   else "warning" if "warning" in statuses else "pass")
        warnings = [warning for item in trace for warning in item["warnings"]]
        errors = [error for item in trace for error in item["errors"]]
        recoveries = [event for item in trace for event in item["recovery_events"]]
        report = {
            "framework_version": RUNTIME_VERSION,
            "execution_id": execution_id,
            "pipeline_stages": [name for name, _, _ in TRANSITIONS],
            "stage_status": {item["stage"]: item["execution_status"] for item in trace},
            "warnings": warnings,
            "errors": errors,
            "timing": {"started_at": timestamp, "finished_at": timestamp,
                       "logical_duration_units": len(trace)},
            "validation": {"status": overall, "qa_gate": qa.output["gate"]},
            "recovery_events": recoveries,
            "output_summary": {"final_prompt_available": bool(final.output.get("final_prompt")),
                               "adapter_request_available": bool(adapter.output.get("target_request"))},
            "final_state": current.value,
        }
        return {
            "execution_id": execution_id,
            "framework_version": RUNTIME_VERSION,
            "execution_trace": {"execution_id": execution_id, "framework_version": RUNTIME_VERSION,
                                "initial_state": ExecutionState.INITIALIZED.value,
                                "final_state": current.value, "stages": trace},
            "pipeline_state": pipeline,
            "decision_output": decision.output,
            "reasoning_output": reasoning.output,
            "compiled_prompt": compiled.output,
            "qa_report": qa.output,
            "final_prompt": final.output.get("final_prompt"),
            "adapter_request": adapter.output.get("target_request"),
            "metadata": {"framework_version": RUNTIME_VERSION, "execution_id": execution_id,
                         "deterministic": True, "external_model_invoked": False},
            "execution_report": report,
            # Backward-compatible 3.4 result fields.
            "validation_state": {"status": overall, "qa": qa.output},
            "final_prompt_package": final.output,
            "adapter_package": adapter.output,
        }


def execute_framework(request: Mapping[str, Any]) -> dict[str, Any]:
    """Backward-compatible alias delegating to the canonical public method."""
    return Framework.execute(request)
