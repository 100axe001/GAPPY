from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import ChatMeMessageToolInput, ChatMeMessageToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ChatMeMessageInput(ChatMeMessageToolInput):
    """Operation input for `chat_me_message`."""
    pass

class ChatMeMessageOutput(ChatMeMessageToolOutput):
    """Operation output for `chat_me_message`."""
    pass

class SlackChatMeResource(BaseResourceClient):
    """Operations for the `chat_me` resource."""

    @operation(
        name='chat_me_message',
        title='ChatMeMessage',
        input_model=ChatMeMessageInput,
        output_model=ChatMeMessageOutput,
        tools_used=('chat_me_message',),
        tags=tuple(['chat']),
    )
    async def message(self, data: ChatMeMessageInput) -> ChatMeMessageOutput:
        """Share a me message into a channel.

Important inputs: token, body"""
        tool = self._client.get_tool('chat_me_message')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ChatMeMessageOutput.model_validate(coerce_tool_result(result))
