from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import ChatGetPermalinkToolInput, ChatGetPermalinkToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ChatGetPermalinkInput(ChatGetPermalinkToolInput):
    """Operation input for `chat_get_permalink`."""
    pass

class ChatGetPermalinkOutput(ChatGetPermalinkToolOutput):
    """Operation output for `chat_get_permalink`."""
    pass

class SlackChatGetResource(BaseResourceClient):
    """Operations for the `chat_get` resource."""

    @operation(
        name='chat_get_permalink',
        title='ChatGetPermalink',
        input_model=ChatGetPermalinkInput,
        output_model=ChatGetPermalinkOutput,
        tools_used=('chat_get_permalink',),
        tags=tuple(['chat']),
    )
    async def permalink(self, data: ChatGetPermalinkInput) -> ChatGetPermalinkOutput:
        """Retrieve a permalink URL for a specific extant message.

Important inputs: token, channel, message_ts"""
        tool = self._client.get_tool('chat_get_permalink')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ChatGetPermalinkOutput.model_validate(coerce_tool_result(result))
