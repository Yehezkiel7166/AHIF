"""Validate persisted empirical records and generate claim-bounded reports.

This module performs no network access and no image generation.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

ROOT = Path(__file__).resolve().parent
SCHEMAS = ROOT / "schemas"
RECORD_SCHEMAS = {name: SCHEMAS / f"{name}.schema.json" for name in ("scenario", "execution", "evaluation", "evidence", "report", "comparison")}
REGISTRIES = {
    "execution": ("executions/EXECUTION_REGISTRY.json", "executions", "execution_id"),
    "evaluation": ("evaluations/EVALUATION_REGISTRY.json", "evaluations", "evaluation_id"),
    "evidence": ("evidence/EVIDENCE_REGISTRY.json", "evidence", "evidence_id"),
    "report": ("reports/REPORT_REGISTRY.json", "reports", "report_id"),
    "comparison": ("baseline/COMPARISON_REGISTRY.json", "comparisons", "comparison_id"),
}

class ValidationError(ValueError):
    """A record violates its repository schema."""

class IntegrityError(ValidationError):
    """An evidence artifact does not match its declared digest."""

def _check(value: Any, schema: Mapping[str, Any], path: str = "$") -> None:
    if "const" in schema and value != schema["const"]: raise ValidationError(f"{path}: expected {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]: raise ValidationError(f"{path}: invalid value {value!r}")
    types = schema.get("type")
    if types:
        types = [types] if isinstance(types, str) else types
        checks = {"object": lambda x:isinstance(x,dict), "array":lambda x:isinstance(x,list), "string":lambda x:isinstance(x,str), "null":lambda x:x is None, "boolean":lambda x:isinstance(x,bool)}
        if not any(checks[t](value) for t in types): raise ValidationError(f"{path}: expected {' or '.join(types)}")
    if isinstance(value, dict):
        missing = set(schema.get("required", ())) - set(value)
        if missing: raise ValidationError(f"{path}: missing required fields: {', '.join(sorted(missing))}")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            extra = set(value)-set(props)
            if extra: raise ValidationError(f"{path}: unknown fields: {', '.join(sorted(extra))}")
        for key, child in props.items():
            if key in value: _check(value[key], child, f"{path}.{key}")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0): raise ValidationError(f"{path}: too few items")
        if schema.get("uniqueItems") and len({json.dumps(x,sort_keys=True) for x in value}) != len(value): raise ValidationError(f"{path}: duplicate items")
        for index, item in enumerate(value): _check(item, schema.get("items", {}), f"{path}[{index}]")
    if isinstance(value, str):
        if len(value) < schema.get("minLength", 0): raise ValidationError(f"{path}: empty string")
        import re
        if schema.get("pattern") and not re.fullmatch(schema["pattern"], value): raise ValidationError(f"{path}: invalid format")

def validate_record(kind: str, record: Mapping[str, Any]) -> None:
    """Validate a record against the canonical schema and cross-field rules."""
    try: schema_path = RECORD_SCHEMAS[kind]
    except KeyError as exc: raise ValidationError(f"unknown record kind: {kind}") from exc
    _check(record, json.loads(schema_path.read_text()))
    if kind == "execution":
        if record["evidence_status"] == "AVAILABLE" and not record.get("image_hash"):
            raise ValidationError("$.image_hash: required when evidence is AVAILABLE")
    if kind == "evaluation":
        if record["status"] in {"APPROVED", "REJECTED"}:
            if not record.get("reviewer") or any(v == "NOT_EVALUATED" for v in record["dimensions"].values()):
                raise ValidationError("completed evaluation requires reviewer and every dimension reviewed")
    if kind == "evidence" and record["status"] == "AVAILABLE" and not record["artifacts"]:
        raise ValidationError("available evidence requires at least one artifact")

def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""): digest.update(block)
    return f"sha256:{digest.hexdigest()}"

def verify_evidence(record: Mapping[str, Any], repository_root: str | Path) -> None:
    validate_record("evidence", record)
    root = Path(repository_root).resolve()
    for artifact in record["artifacts"]:
        path = (root / artifact["path"]).resolve()
        if root not in path.parents or not path.is_file(): raise IntegrityError(f"missing or unsafe evidence artifact: {artifact['path']}")
        actual = sha256_file(path)
        if actual != artifact["sha256"]: raise IntegrityError(f"hash mismatch for {artifact['path']}")

def validate_registries(root: str | Path = ROOT) -> dict[str, int]:
    """Validate registry envelopes, identifiers, and execution references."""
    base = Path(root)
    loaded: dict[str, list[dict[str, Any]]] = {}
    for kind, (relative, collection, identifier) in REGISTRIES.items():
        payload = json.loads((base / relative).read_text(encoding="utf-8"))
        if set(payload) != {"schema_version", collection} or payload["schema_version"] != "1.0":
            raise ValidationError(f"{relative}: incompatible registry envelope")
        records = payload[collection]
        if not isinstance(records, list): raise ValidationError(f"{relative}: {collection} must be an array")
        identifiers = []
        for record in records:
            validate_record(kind, record); identifiers.append(record[identifier])
        if len(identifiers) != len(set(identifiers)):
            raise ValidationError(f"{relative}: duplicate identifiers")
        loaded[kind] = records
    execution_ids = {item["execution_id"] for item in loaded["execution"]}
    for kind in ("evaluation", "evidence"):
        orphaned = sorted(item["execution_id"] for item in loaded[kind]
                          if item["execution_id"] not in execution_ids)
        if orphaned: raise ValidationError(f"{kind} registry has orphan executions: {', '.join(orphaned)}")
    for report in loaded["report"]:
        if report["execution_metadata"].get("execution_id") not in execution_ids:
            raise ValidationError(f"report registry has orphan report: {report['report_id']}")
    return {kind: len(records) for kind, records in loaded.items()}

def build_report(execution: Mapping[str, Any], scenario: Mapping[str, Any], prompt_package: Mapping[str, Any]) -> dict[str, Any]:
    """Create metadata-only output; it asserts neither success nor readiness."""
    validate_record("execution", execution); validate_record("scenario", scenario)
    if execution["scenario_id"] != scenario["scenario_id"]: raise ValidationError("scenario ID mismatch")
    report = {"schema_version":"1.0", "report_id":f"report:{execution['execution_id']}", "execution_metadata":dict(execution), "scenario_metadata":dict(scenario), "prompt_package":dict(prompt_package), "evaluation_status":execution["evaluation_status"], "evidence_status":execution["evidence_status"], "claim_boundary":"NO_PRODUCTION_CLAIM"}
    validate_record("report", report)
    return report

def _canonical_hash(value: Mapping[str, Any]) -> str:
    encoded = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
    return "sha256:" + hashlib.sha256(encoded.encode()).hexdigest()

def prepare_runtime_validation(source: Mapping[str, Any]):
    """Prepare claim-bounded empirical records for the canonical runtime path.

    The returned registry update is an in-memory append proposal. It deliberately
    records missing evidence because the runtime neither calls a model nor writes
    governance registries as a side effect.
    """
    from RUNTIME.contracts import StageResult
    execution_id = source["execution_id"]
    scenario = {
        "schema_version": "1.0", "scenario_id": f"runtime:{execution_id}",
        "title": "Canonical runtime execution", "source": "RUNTIME.Framework.execute",
        "input": dict(source["user_request"]),
        "dimensions": ["identity", "environment", "prompt_consistency"],
        "comments": "Runtime metadata only; no image generation was performed.",
    }
    execution = {
        "schema_version": "1.0", "execution_id": execution_id,
        "framework_version": "3.7.0", "scenario_id": scenario["scenario_id"],
        "timestamp": source["timestamp"], "model_adapter": source["adapter_id"],
        "prompt_package_hash": _canonical_hash(source["prompt_package"]),
        "image_hash": None, "evaluation_status": "NOT_EVALUATED",
        "evidence_status": "MISSING", "reviewer": None,
        "comments": "Adapter request prepared only; no external execution occurred.",
    }
    evidence = {
        "schema_version": "1.0", "evidence_id": f"evidence:{execution_id}",
        "execution_id": execution_id, "status": "MISSING", "artifacts": [],
        "collected_at": None, "collector": None,
        "comments": "No externally produced artifact was supplied.",
    }
    validate_record("scenario", scenario)
    validate_record("execution", execution)
    validate_record("evidence", evidence)
    report = build_report(execution, scenario, source["prompt_package"])
    return StageResult({
        "status": "NOT_EVALUATED", "evidence_status": "MISSING",
        "execution_record": execution, "evidence_record": evidence,
        "report": report,
        "registry_update": {
            "execution_id": execution_id,
            "execution_registry": execution,
            "evidence_registry": evidence,
            "report_registry": report,
        },
        "persisted": False, "claim_boundary": "NO_PRODUCTION_CLAIM",
    })
