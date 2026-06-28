from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import ChatDeleteScheduledMessageToolInput, ChatDeleteScheduledMessageToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ChatDeleteScheduledMessageInput(ChatDeleteScheduledMessageToolInput):
    """Operation input for `chat_delete_scheduled_message`."""
    pass

class ChatDeleteScheduledMessageOutput(ChatDeleteScheduledMessageToolOutput):
    """Operation output for `chat_delete_scheduled_message`."""
    pass

class SlackChatDeleteScheduledResource(BaseResourceClient):
    """Operations for the `chat_delete_scheduled` resource."""

    @operation(
        name='chat_delete_scheduled_message',
        title='ChatDeleteScheduledMessage',
        input_model=ChatDeleteScheduledMessageInput,
        output_model=ChatDeleteScheduledMessageOutput,
        tools_used=('chat_delete_scheduled_message',),
        tags=tuple(['chat']),
    )
    async def message(self, data: ChatDeleteScheduledMessageInput) -> ChatDeleteScheduledMessageOutput:
        """Deletes a pending scheduled message from the queue.

Important inputs: token, body"""
        tool = self._client.get_tool('chat_delete_scheduled_message')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ChatDeleteScheduledMessageOutput.model_validate(coerce_tool_result(result))
