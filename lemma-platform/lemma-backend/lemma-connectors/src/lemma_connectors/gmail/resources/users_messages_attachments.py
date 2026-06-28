from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersMessagesAttachmentsGetToolInput, GmailUsersMessagesAttachmentsGetToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersMessagesAttachmentsGetInput(GmailUsersMessagesAttachmentsGetToolInput):
    """Operation input for `users_messages_attachments_get`."""
    pass

class UsersMessagesAttachmentsGetOutput(GmailUsersMessagesAttachmentsGetToolOutput):
    """Operation output for `users_messages_attachments_get`."""
    pass

class GmailUsersMessagesAttachmentsResource(BaseResourceClient):
    """Operations grouped around the `users_messages_attachments` resource."""

    @operation(
        name='users_messages_attachments_get',
        title='UsersMessagesAttachmentsGet',
        input_model=UsersMessagesAttachmentsGetInput,
        output_model=UsersMessagesAttachmentsGetOutput,
        tools_used=('gmail_users_messages_attachments_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: UsersMessagesAttachmentsGetInput) -> UsersMessagesAttachmentsGetOutput:
        """Gets the specified message attachment.

Use this when you want to gets the specified message attachment.
Key inputs: fields, user_id, message_id, id."""
        tool = self._client.get_tool('gmail_users_messages_attachments_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersMessagesAttachmentsGetOutput.model_validate(coerce_tool_result(result))
