from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import ConversationsSetPurposeToolInput, ConversationsSetPurposeToolOutput, ConversationsSetTopicToolInput, ConversationsSetTopicToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ConversationsSetPurposeInput(ConversationsSetPurposeToolInput):
    """Operation input for `conversations_set_purpose`."""
    pass

class ConversationsSetPurposeOutput(ConversationsSetPurposeToolOutput):
    """Operation output for `conversations_set_purpose`."""
    pass

class ConversationsSetTopicInput(ConversationsSetTopicToolInput):
    """Operation input for `conversations_set_topic`."""
    pass

class ConversationsSetTopicOutput(ConversationsSetTopicToolOutput):
    """Operation output for `conversations_set_topic`."""
    pass

class SlackConversationsSetResource(BaseResourceClient):
    """Operations for the `conversations_set` resource."""

    @operation(
        name='conversations_set_purpose',
        title='ConversationsSetPurpose',
        input_model=ConversationsSetPurposeInput,
        output_model=ConversationsSetPurposeOutput,
        tools_used=('conversations_set_purpose',),
        tags=tuple(['conversations']),
    )
    async def purpose(self, data: ConversationsSetPurposeInput) -> ConversationsSetPurposeOutput:
        """Sets the purpose for a conversation.

Important inputs: token, body"""
        tool = self._client.get_tool('conversations_set_purpose')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsSetPurposeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='conversations_set_topic',
        title='ConversationsSetTopic',
        input_model=ConversationsSetTopicInput,
        output_model=ConversationsSetTopicOutput,
        tools_used=('conversations_set_topic',),
        tags=tuple(['conversations']),
    )
    async def topic(self, data: ConversationsSetTopicInput) -> ConversationsSetTopicOutput:
        """Sets the topic for a conversation.

Important inputs: token, body"""
        tool = self._client.get_tool('conversations_set_topic')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ConversationsSetTopicOutput.model_validate(coerce_tool_result(result))
