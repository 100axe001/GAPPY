from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import typer


def read_json(
    value: str | None, file: Path | None, *, required: bool = False
) -> dict[str, Any]:
    if value and file:
        raise typer.BadParameter("Use only one of --data or --file.")
    if file is not None:
        raw = file.read_text(encoding="utf-8")
    elif value is not None:
        raw = value
    elif required:
        raise typer.BadParameter("Provide --data or --file.")
    else:
        return {}

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise typer.BadParameter(f"Invalid JSON: {exc}") from exc
    if not isinstance(parsed, dict):
        raise typer.BadParameter("JSON payload must be an object.")
    return parsed


# Resource types that expose a `lemma <type> schema` command (see _authoring);
# a validation error for one points the user at it for the full shape + enums.
_SCHEMA_RESOURCES = frozenset(
    {"agent", "function", "table", "workflow", "schedule", "surface"}
)


def build_request(model_cls: Any, data: dict[str, Any], *, context: str | None = None) -> Any:
    """Construct an SDK request model from a dict, turning a missing/mistyped
    field into an actionable `ValueError` instead of a raw `KeyError`/`TypeError`.

    Keeping this at the construction site lets `run_with_client` stay narrow:
    genuine bugs elsewhere still surface as tracebacks, while a hand-written
    payload missing a required field reports exactly which one. `context` (e.g.
    "agent triage") is appended so bundle imports name the offending resource,
    and — when it names a resource with a schema command — points at it.
    """
    where = f" ({context})" if context else ""
    hint = ""
    if context:
        resource = context.split()[0]
        if resource in _SCHEMA_RESOURCES:
            hint = (
                f" Run `lemma {resource} schema` for the required fields "
                "and valid enums."
            )
    try:
        return model_cls.from_dict(data)
    except KeyError as exc:
        key = exc.args[0] if exc.args else ""
        field = f": {key}" if key else ""
        raise ValueError(f"Missing required field{field}.{where}{hint}") from exc
    except TypeError as exc:
        raise ValueError(f"Invalid field value{where}: {exc}{hint}") from exc
