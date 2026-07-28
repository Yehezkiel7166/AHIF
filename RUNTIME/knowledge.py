"""Deterministic machine-readable knowledge loader."""
import json
from pathlib import Path
from typing import Any, Mapping
from .contracts import StageResult

ROOT = Path(__file__).resolve().parents[1]


def load_knowledge(context: Mapping[str, Any]) -> StageResult:
    del context
    records = []
    packages = []
    for path in sorted((ROOT / "09_DECISION_ENGINE/knowledge_graph/packages").glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        if not data.get("validation", {}).get("schema_validated"):
            continue
        packages.append(data["package_id"])
        records.extend(data["records"])
    records.sort(key=lambda item: (-item["priority"], item["id"]))
    return StageResult({"package_ids": packages, "records": records})
