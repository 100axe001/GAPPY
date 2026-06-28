from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import ChatPostEphemeralToolInput, ChatPostEphemeralToolOutput, ChatPostMessageToolInput, ChatPostMessageToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ChatPostEphemeralInput(ChatPostEphemeralToolInput):
    """Operation input for `chat_post_ephemeral`."""
    pass

class ChatPostEphemeralOutput(ChatPostEphemeralToolOutput):
    """Operation output for `chat_post_ephemeral`."""
    pass

class ChatPostMessageInput(ChatPostMessageToolInput):
    """Operation input for `chat_post_message`."""
    pass

class ChatPostMessageOutput(ChatPostMessageToolOutput):
    """Operation output for `chat_post_message`."""
    pass

class SlackChatPostResource(BaseResourceClient):
    """Operations for the `chat_post` resource."""

    @operation(
        name='chat_post_ephemeral',
        title='ChatPostEphemeral',
        input_model=ChatPostEphemeralInput,
        output_model=ChatPostEphemeralOutput,
        tools_used=('chat_post_ephemeral',),
        tags=tuple(['chat']),
    )
    async def ephemeral(self, data: ChatPostEphemeralInput) -> ChatPostEphemeralOutput:
        """Sends an ephemeral message to a user in a channel.

Important inputs: token, body"""
        tool = self._client.get_tool('chat_post_ephemeral')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ChatPostEphemeralOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='chat_post_message',
        title='ChatPostMessage',
        input_model=ChatPostMessageInput,
        output_model=ChatPostMessageOutput,
        tools_used=('chat_post_message',),
        tags=tuple(['chat']),
    )
    async def message(self, data: ChatPostMessageInput) -> ChatPostMessageOutput:
        """Sends a message to a channel.

Important inputs: token, body"""
        tool = self._client.get_tool('chat_post_message')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ChatPostMessageOutput.model_validate(coerce_tool_result(result))
