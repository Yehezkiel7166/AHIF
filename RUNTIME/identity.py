"""Canonical identity binding stage."""
from typing import Any, Mapping
from .contracts import StageResult, require_mapping, require_text


def lock_identity(identity: Mapping[str, Any]) -> StageResult:
    value = require_mapping(identity, "identity")
    asset = require_text(value.get("canonical_asset"), "identity.canonical_asset")
    return StageResult({
        "canonical_asset": asset,
        "identity_contract": "02_CORE_IDENTITY/CANONICAL_IDENTITY.md",
        "lock_status": "locked",
        "substitution_allowed": False,
    })
