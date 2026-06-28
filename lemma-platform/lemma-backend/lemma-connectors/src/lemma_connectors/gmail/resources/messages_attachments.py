from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersMessagesAttachmentsGetToolInput, GmailUsersMessagesAttachmentsGetToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class MessagesAttachmentsGetInput(GmailUsersMessagesAttachmentsGetToolInput):
    """Operation input for `messages_attachments_get`."""
    pass

class MessagesAttachmentsGetOutput(GmailUsersMessagesAttachmentsGetToolOutput):
    """Operation output for `messages_attachments_get`."""
    pass

class GmailMessagesAttachmentsResource(BaseResourceClient):
    """Operations for the `messages_attachments` resource."""

    @operation(
        name='messages_attachments_get',
        title='MessagesAttachmentsGet',
        input_model=MessagesAttachmentsGetInput,
        output_model=MessagesAttachmentsGetOutput,
        tools_used=('gmail_users_messages_attachments_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: MessagesAttachmentsGetInput) -> MessagesAttachmentsGetOutput:
        """Gets the specified message attachment.

Important inputs: fields, user_id, message_id, id"""
        tool = self._client.get_tool('gmail_users_messages_attachments_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MessagesAttachmentsGetOutput.model_validate(coerce_tool_result(result))
