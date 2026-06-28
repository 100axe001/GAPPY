"""Cross-module contract for reading a conversation widget's HTML.

A widget's HTML fragment is authored by the agent's ``display_resource`` tool and
stored in the conversation. Both the widget serving path and "save widget as
app" need that content, but the app module must not depend on agent
internals. This port is the shared contract: the agent module implements it,
and consumers (app service / controllers) depend only on this core interface.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol
from uuid import UUID


@dataclass(frozen=True)
class WidgetArtifact:
    """A resolved widget: its HTML fragment plus the pod it belongs to."""

    content: str
    pod_id: UUID
    title: str = ""


class WidgetContentReader(Protocol):
    """Resolves a widget's content by ``(conversation_id, tool_call_id)``."""

    async def get_widget(
        self, conversation_id: UUID, tool_call_id: str
    ) -> WidgetArtifact | None: ...
