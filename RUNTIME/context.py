"""Context normalization stage."""
from typing import Any, Mapping
from .contracts import StageResult, require_mapping, require_text


def load_context(user_request: Mapping[str, Any]) -> StageResult:
    request = require_mapping(user_request, "user_request")
    allowed = ("location", "place", "atmosphere", "activity", "weather", "time", "season", "constraints")
    output = {key: request[key] for key in allowed if key in request}
    for key in ("location", "place", "atmosphere"):
        output[key] = require_text(request.get(key), f"user_request.{key}")
    constraints = output.get("constraints", [])
    if not isinstance(constraints, list) or any(not isinstance(x, str) or not x.strip() for x in constraints):
        from .errors import RuntimeContractError
        raise RuntimeContractError("user_request.constraints must be an array of non-empty strings")
    output["constraints"] = sorted(set(x.strip() for x in constraints))
    return StageResult(output)
