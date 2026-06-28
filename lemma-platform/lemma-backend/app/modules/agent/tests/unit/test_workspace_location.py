"""Unit tests for conversation workspace/cwd resolution."""

from __future__ import annotations

from uuid import uuid4

from app.modules.agent.domain.entities import Conversation
from app.modules.agent.services.workspace_location import resolve_workspace_location


def test_defaults_to_conversation_scoped_cwd_and_single_workspace():
    conversation = Conversation(pod_id=uuid4(), user_id=uuid4())

    location = resolve_workspace_location(conversation)

    assert location.cwd == f"/workspace/conversations/{conversation.id}"
    assert location.workspace_id == "default"


def test_conversation_metadata_overrides_cwd_and_workspace():
    conversation = Conversation(
        pod_id=uuid4(),
        user_id=uuid4(),
        metadata={"cwd": "/workspace/project", "workspace_name": "research"},
    )

    location = resolve_workspace_location(conversation)

    assert location.cwd == "/workspace/project"
    assert location.workspace_id == "research"


def test_nested_workspace_block_takes_precedence():
    conversation = Conversation(
        pod_id=uuid4(),
        user_id=uuid4(),
        metadata={"workspace": {"id": "ws-7", "cwd": "/workspace/ws7"}, "cwd": "/ignored"},
    )

    location = resolve_workspace_location(conversation)

    assert location.workspace_id == "ws-7"
    assert location.cwd == "/workspace/ws7"
