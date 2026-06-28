from app.modules.agent.domain.value_objects import AgentRunStatus, ConversationStatus


def test_agent_run_status_accepts_legacy_lowercase_values() -> None:
    assert AgentRunStatus("running") == AgentRunStatus.RUNNING
    assert AgentRunStatus("stop_requested") == AgentRunStatus.STOP_REQUESTED
    assert AgentRunStatus("completed") == AgentRunStatus.COMPLETED


def test_conversation_status_accepts_legacy_lowercase_values() -> None:
    assert ConversationStatus("running") == ConversationStatus.RUNNING
    assert ConversationStatus("waiting") == ConversationStatus.WAITING
    assert ConversationStatus("completed") == ConversationStatus.COMPLETED
