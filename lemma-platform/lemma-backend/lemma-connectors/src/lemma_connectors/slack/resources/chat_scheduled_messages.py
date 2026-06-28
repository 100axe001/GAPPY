from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import ChatScheduledMessagesListToolInput, ChatScheduledMessagesListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ChatScheduledMessagesListInput(ChatScheduledMessagesListToolInput):
    """Operation input for `chat_scheduled_messages_list`."""
    pass

class ChatScheduledMessagesListOutput(ChatScheduledMessagesListToolOutput):
    """Operation output for `chat_scheduled_messages_list`."""
    pass

class SlackChatScheduledMessagesResource(BaseResourceClient):
    """Operations for the `chat_scheduled_messages` resource."""

    @operation(
        name='chat_scheduled_messages_list',
        title='ChatScheduledMessagesList',
        input_model=ChatScheduledMessagesListInput,
        output_model=ChatScheduledMessagesListOutput,
        tools_used=('chat_scheduled_messages_list',),
        tags=tuple(['chat.scheduledMessages', 'chat']),
    )
    async def list(self, data: ChatScheduledMessagesListInput) -> ChatScheduledMessagesListOutput:
        """Returns a list of scheduled messages.

Important inputs: token, channel, latest, oldest, limit, cursor"""
        tool = self._client.get_tool('chat_scheduled_messages_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ChatScheduledMessagesListOutput.model_validate(coerce_tool_result(result))
