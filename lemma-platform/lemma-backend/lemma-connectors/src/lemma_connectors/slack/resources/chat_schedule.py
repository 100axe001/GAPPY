from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import ChatScheduleMessageToolInput, ChatScheduleMessageToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ChatScheduleMessageInput(ChatScheduleMessageToolInput):
    """Operation input for `chat_schedule_message`."""
    pass

class ChatScheduleMessageOutput(ChatScheduleMessageToolOutput):
    """Operation output for `chat_schedule_message`."""
    pass

class SlackChatScheduleResource(BaseResourceClient):
    """Operations for the `chat_schedule` resource."""

    @operation(
        name='chat_schedule_message',
        title='ChatScheduleMessage',
        input_model=ChatScheduleMessageInput,
        output_model=ChatScheduleMessageOutput,
        tools_used=('chat_schedule_message',),
        tags=tuple(['chat']),
    )
    async def message(self, data: ChatScheduleMessageInput) -> ChatScheduleMessageOutput:
        """Schedules a message to be sent to a channel.

Important inputs: token, body"""
        tool = self._client.get_tool('chat_schedule_message')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ChatScheduleMessageOutput.model_validate(coerce_tool_result(result))
