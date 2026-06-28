"""Conversation-metadata-backed todo storage.

Persists the agent's todo list as a plain list of ``{content, done}`` dicts under
a single ``todos`` key in the conversation's metadata JSON blob (via
non-clobbering ``jsonb_set``), so planning survives across turns without a
dedicated table.
"""

from __future__ import annotations

from uuid import UUID

from app.core.infrastructure.db.uow_factory import UnitOfWorkFactory
from app.modules.agent.domain.value_objects import JsonObject
from app.modules.agent.infrastructure.repositories import ConversationRepository

_TODOS_KEY = "todos"


class ConversationTodoStore:
    """Read/replace the todo list for one conversation."""

    def __init__(
        self, *, uow_factory: UnitOfWorkFactory, conversation_id: UUID
    ) -> None:
        self._uow_factory = uow_factory
        self._conversation_id = conversation_id

    async def read(self) -> list[JsonObject]:
        async with self._uow_factory() as uow:
            raw = await ConversationRepository(uow).get_conversation_metadata_key(
                self._conversation_id, _TODOS_KEY
            )
        return (
            [item for item in raw if isinstance(item, dict)]
            if isinstance(raw, list)
            else []
        )

    async def write(self, todos: list[JsonObject]) -> None:
        async with self._uow_factory() as uow:
            await ConversationRepository(uow).set_conversation_metadata_key(
                self._conversation_id, _TODOS_KEY, todos
            )
            await uow.commit()
