"""Shared immutable runtime contracts, states, and trace construction."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Mapping

from .errors import RuntimeContractError

RUNTIME_VERSION = "3.6.0"
CONTRACT_VERSION = "1.1"


class Status(str, Enum):
    PASS = "pass"
    WARNING = "warning"
    BLOCKED = "blocked"
    FAIL = "fail"


class ExecutionState(str, Enum):
    INITIALIZED = "INITIALIZED"
    CONTEXT_READY = "CONTEXT_READY"
    IDENTITY_LOCKED = "IDENTITY_LOCKED"
    KNOWLEDGE_READY = "KNOWLEDGE_READY"
    DECISION_COMPLETE = "DECISION_COMPLETE"
    REASONING_COMPLETE = "REASONING_COMPLETE"
    PROMPT_COMPILED = "PROMPT_COMPILED"
    QA_COMPLETE = "QA_COMPLETE"
    FINAL_PACKAGE_READY = "FINAL_PACKAGE_READY"
    ADAPTER_READY = "ADAPTER_READY"
    FINISHED = "FINISHED"
    FAILED = "FAILED"


@dataclass(frozen=True)
class StageResult:
    output: Mapping[str, Any]
    status: Status = Status.PASS
    warnings: tuple[str, ...] = ()
    errors: tuple[str, ...] = ()
    recovery_events: tuple[str, ...] = ()


def require_mapping(value: object, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise RuntimeContractError(f"{name} must be an object")
    return value


def require_text(value: object, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise RuntimeContractError(f"{name} must be a non-empty string")
    return value.strip()


def summarize(value: Mapping[str, Any]) -> dict[str, Any]:
    """Return content-free, stable metadata rather than private reasoning."""
    return {"fields": sorted(value), "field_count": len(value)}


def trace_record(stage: str, order: int, source: Mapping[str, Any], result: StageResult,
                 timestamp: str, from_state: ExecutionState,
                 to_state: ExecutionState) -> dict[str, Any]:
    """Build the complete, deterministic contract record for one stage."""
    return {
        "stage": stage,
        "execution_order": order,
        "input": summarize(source),
        "output": summarize(result.output),
        # Retained aliases preserve the 3.4 trace contract.
        "input_summary": summarize(source),
        "output_summary": summarize(result.output),
        "execution_status": result.status.value,
        "validation": {"status": "valid" if not result.errors else "invalid"},
        "validation_status": "valid" if not result.errors else "invalid",
        "error": list(result.errors),
        "errors": list(result.errors),
        "warnings": list(result.warnings),
        "recovery": list(result.recovery_events),
        "recovery_events": list(result.recovery_events),
        "execution_state": to_state.value,
        "transition_rule": f"{from_state.value} -> {to_state.value}",
        "timing": {"started_at": timestamp, "finished_at": timestamp,
                   "logical_duration_units": 1},
        "timestamp": timestamp,
        "contract_version": CONTRACT_VERSION,
        "recovery_path": "correct the earliest responsible stage and execute a new run",
        "escalation_path": "return blocked state for human review",
    }
