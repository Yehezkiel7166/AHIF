"""Model-adapter preparation stage; it performs no model or network execution."""
import json
from pathlib import Path
from typing import Any, Mapping
from .contracts import StageResult, Status, require_mapping, require_text

ROOT = Path(__file__).resolve().parents[1]


def prepare_model_adapter(payload: Mapping[str, Any]) -> StageResult:
    value = require_mapping(payload, "adapter_input")
    adapter_id = require_text(value.get("adapter_id"), "adapter_id")
    registry = json.loads((ROOT / "16_MODEL_ADAPTERS/REGISTRY/ADAPTER_REGISTRY.json").read_text())
    profile = next((x for x in registry["adapters"] if x["adapter_id"] == adapter_id), None)
    if profile is None:
        return StageResult({"adapter_id": adapter_id, "adapter_status": "blocked", "target_request": None},
                           Status.BLOCKED, errors=("AHIF-ADAPTER-UNKNOWN",))
    package = value["final_prompt"]
    if not package.get("release_eligible"):
        return StageResult({"adapter_id": adapter_id, "adapter_version": profile["adapter_version"],
                            "adapter_status": "blocked", "target_family": profile["target_family"],
                            "target_request": None}, Status.BLOCKED,
                           errors=("AHIF-ADAPTER-FINAL-PACKAGE-BLOCKED",))
    return StageResult({"adapter_id": adapter_id, "adapter_version": profile["adapter_version"],
                        "adapter_status": "prepared", "target_family": profile["target_family"],
                        "target_request": {"prompt": package["final_prompt"],
                                           "negative_constraints": package["negative_constraints"],
                                           "identity_asset": package["identity_binding"]["canonical_asset"]}})
