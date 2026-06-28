from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import ChatDeleteToolInput, ChatDeleteToolOutput, ChatUnfurlToolInput, ChatUnfurlToolOutput, ChatUpdateToolInput, ChatUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ChatDeleteInput(ChatDeleteToolInput):
    """Operation input for `chat_delete`."""
    pass

class ChatDeleteOutput(ChatDeleteToolOutput):
    """Operation output for `chat_delete`."""
    pass

class ChatUnfurlInput(ChatUnfurlToolInput):
    """Operation input for `chat_unfurl`."""
    pass

class ChatUnfurlOutput(ChatUnfurlToolOutput):
    """Operation output for `chat_unfurl`."""
    pass

class ChatUpdateInput(ChatUpdateToolInput):
    """Operation input for `chat_update`."""
    pass

class ChatUpdateOutput(ChatUpdateToolOutput):
    """Operation output for `chat_update`."""
    pass

class SlackChatResource(BaseResourceClient):
    """Operations for the `chat` resource."""

    @operation(
        name='chat_delete',
        title='ChatDelete',
        input_model=ChatDeleteInput,
        output_model=ChatDeleteOutput,
        tools_used=('chat_delete',),
        tags=tuple(['chat']),
    )
    async def delete(self, data: ChatDeleteInput) -> ChatDeleteOutput:
        """Deletes a message.

Important inputs: token, body"""
        tool = self._client.get_tool('chat_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ChatDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='chat_unfurl',
        title='ChatUnfurl',
        input_model=ChatUnfurlInput,
        output_model=ChatUnfurlOutput,
        tools_used=('chat_unfurl',),
        tags=tuple(['chat']),
    )
    async def unfurl(self, data: ChatUnfurlInput) -> ChatUnfurlOutput:
        """Provide custom unfurl behavior for user-posted URLs.

Important inputs: token, body"""
        tool = self._client.get_tool('chat_unfurl')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ChatUnfurlOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='chat_update',
        title='ChatUpdate',
        input_model=ChatUpdateInput,
        output_model=ChatUpdateOutput,
        tools_used=('chat_update',),
        tags=tuple(['chat']),
    )
    async def update(self, data: ChatUpdateInput) -> ChatUpdateOutput:
        """Updates a message.

Important inputs: token, body"""
        tool = self._client.get_tool('chat_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ChatUpdateOutput.model_validate(coerce_tool_result(result))
