"""Pod-scoped resource views for the TUI main screen."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from ..cli_core.io import list_items, to_plain
from ..cli_core.state import CliState, client_session
from .state import resolve_pod_id


@dataclass(frozen=True)
class ResourceView:
    name: str
    title: str
    columns: tuple[str, ...]
    load: Callable[[Any, str], Any]


RESOURCE_VIEWS: tuple[ResourceView, ...] = (
    ResourceView(
        "agents",
        "Agents",
        ("name", "status", "kind"),
        lambda c, p: c.pod(p).agents.list(limit=100),
    ),
    ResourceView(
        "conversations",
        "Conversations",
        ("title", "status", "created_at", "id"),
        lambda c, p: c.pod(p).conversations.list(limit=100),
    ),
    ResourceView(
        "functions",
        "Functions",
        ("name", "status", "created_at"),
        lambda c, p: c.pod(p).functions.list(limit=100),
    ),
    ResourceView(
        "workflows",
        "Workflows",
        ("name", "status", "created_at"),
        lambda c, p: c.pod(p).workflows.list(limit=100),
    ),
    ResourceView(
        "schedules",
        "Schedules",
        ("name", "status", "schedule_type"),
        lambda c, p: c.pod(p).schedules.list(limit=100),
    ),
    ResourceView(
        "tables",
        "Tables",
        ("name", "created_at", "updated_at"),
        lambda c, p: c.pod(p).tables.list(limit=100),
    ),
    ResourceView(
        "files",
        "Files",
        ("path", "type", "updated_at"),
        lambda c, p: c.pod(p).files.list("/", limit=100),
    ),
    ResourceView(
        "surfaces",
        "Surfaces",
        ("platform", "status", "agent_name", "credential_mode"),
        lambda c, p: c.pod(p).surfaces.list(limit=100),
    ),
)


def resource_view(name: str) -> ResourceView:
    for view in RESOURCE_VIEWS:
        if view.name == name:
            return view
    return RESOURCE_VIEWS[0]


def load_rows(state: CliState, view_name: str) -> list[dict[str, Any]]:
    view = resource_view(view_name)
    pod_id = resolve_pod_id(state)
    if not pod_id:
        raise ValueError("No pod selected. Press 'p' to pick a pod.")
    with client_session(state) as client:
        payload = view.load(client, pod_id)
    return [to_plain(item) for item in list_items(payload)]


def cell_value(row: dict[str, Any], key: str) -> str:
    value = row.get(key)
    if value is None:
        return ""
    if isinstance(value, list):
        return ", ".join(str(item) for item in value[:3])
    if isinstance(value, dict):
        return ", ".join(f"{k}={v}" for k, v in list(value.items())[:3])
    text = str(value).replace("\n", " ").strip()
    return text if len(text) <= 80 else text[:79] + "…"
