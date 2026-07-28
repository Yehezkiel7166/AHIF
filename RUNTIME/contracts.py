"""Shared immutable runtime contracts and trace construction."""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, Mapping

from .errors import RuntimeContractError

RUNTIME_VERSION = "3.4.0"
CONTRACT_VERSION = "1.0"


class Status(str, Enum):
    PASS = "pass"
    WARNING = "warning"
    BLOCKED = "blocked"
    FAIL = "fail"


@dataclass(frozen=True)
class StageResult:
    output: Mapping[str, Any]
    status: Status = Status.PASS
    warnings: tuple[str, ...] = ()
    errors: tuple[str, ...] = ()


def require_mapping(value: object, name: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise RuntimeContractError(f"{name} must be an object")
    return value


def require_text(value: object, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise RuntimeContractError(f"{name} must be a non-empty string")
    return value.strip()


def summarize(value: Mapping[str, Any]) -> dict[str, Any]:
    """Return content-free, stable trace metadata rather than private reasoning."""
    return {"fields": sorted(value), "field_count": len(value)}


def trace_record(stage: str, order: int, source: Mapping[str, Any], result: StageResult,
                 timestamp: str) -> dict[str, Any]:
    return {
        "stage": stage,
        "execution_order": order,
        "input_summary": summarize(source),
        "output_summary": summarize(result.output),
        "execution_status": result.status.value,
        "validation_status": "valid" if not result.errors else "invalid",
        "timestamp": timestamp,
        "warnings": list(result.warnings),
        "errors": list(result.errors),
        "contract_version": CONTRACT_VERSION,
        "recovery_path": "correct the earliest responsible stage and execute a new run",
        "escalation_path": "return blocked state for human review",
    }
