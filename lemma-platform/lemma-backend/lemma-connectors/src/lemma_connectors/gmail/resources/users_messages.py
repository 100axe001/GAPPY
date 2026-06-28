from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersMessagesBatchDeleteToolInput, GmailUsersMessagesBatchDeleteToolOutput, GmailUsersMessagesBatchModifyToolInput, GmailUsersMessagesBatchModifyToolOutput, GmailUsersMessagesDeleteToolInput, GmailUsersMessagesDeleteToolOutput, GmailUsersMessagesGetToolInput, GmailUsersMessagesGetToolOutput, GmailUsersMessagesImportToolInput, GmailUsersMessagesImportToolOutput, GmailUsersMessagesInsertToolInput, GmailUsersMessagesInsertToolOutput, GmailUsersMessagesListToolInput, GmailUsersMessagesListToolOutput, GmailUsersMessagesModifyToolInput, GmailUsersMessagesModifyToolOutput, GmailUsersMessagesSendToolInput, GmailUsersMessagesSendToolOutput, GmailUsersMessagesTrashToolInput, GmailUsersMessagesTrashToolOutput, GmailUsersMessagesUntrashToolInput, GmailUsersMessagesUntrashToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersMessagesBatchDeleteInput(GmailUsersMessagesBatchDeleteToolInput):
    """Operation input for `users_messages_batch_delete`."""
    pass

class UsersMessagesBatchDeleteOutput(GmailUsersMessagesBatchDeleteToolOutput):
    """Operation output for `users_messages_batch_delete`."""
    pass

class UsersMessagesBatchModifyInput(GmailUsersMessagesBatchModifyToolInput):
    """Operation input for `users_messages_batch_modify`."""
    pass

class UsersMessagesBatchModifyOutput(GmailUsersMessagesBatchModifyToolOutput):
    """Operation output for `users_messages_batch_modify`."""
    pass

class UsersMessagesDeleteInput(GmailUsersMessagesDeleteToolInput):
    """Operation input for `users_messages_delete`."""
    pass

class UsersMessagesDeleteOutput(GmailUsersMessagesDeleteToolOutput):
    """Operation output for `users_messages_delete`."""
    pass

class UsersMessagesGetInput(GmailUsersMessagesGetToolInput):
    """Operation input for `users_messages_get`."""
    pass

class UsersMessagesGetOutput(GmailUsersMessagesGetToolOutput):
    """Operation output for `users_messages_get`."""
    pass

class UsersMessagesImportInput(GmailUsersMessagesImportToolInput):
    """Operation input for `users_messages_import`."""
    pass

class UsersMessagesImportOutput(GmailUsersMessagesImportToolOutput):
    """Operation output for `users_messages_import`."""
    pass

class UsersMessagesInsertInput(GmailUsersMessagesInsertToolInput):
    """Operation input for `users_messages_insert`."""
    pass

class UsersMessagesInsertOutput(GmailUsersMessagesInsertToolOutput):
    """Operation output for `users_messages_insert`."""
    pass

class UsersMessagesListInput(GmailUsersMessagesListToolInput):
    """Operation input for `users_messages_list`."""
    pass

class UsersMessagesListOutput(GmailUsersMessagesListToolOutput):
    """Operation output for `users_messages_list`."""
    pass

class UsersMessagesModifyInput(GmailUsersMessagesModifyToolInput):
    """Operation input for `users_messages_modify`."""
    pass

class UsersMessagesModifyOutput(GmailUsersMessagesModifyToolOutput):
    """Operation output for `users_messages_modify`."""
    pass

class UsersMessagesSendInput(GmailUsersMessagesSendToolInput):
    """Operation input for `users_messages_send`."""
    pass

class UsersMessagesSendOutput(GmailUsersMessagesSendToolOutput):
    """Operation output for `users_messages_send`."""
    pass

class UsersMessagesTrashInput(GmailUsersMessagesTrashToolInput):
    """Operation input for `users_messages_trash`."""
    pass

class UsersMessagesTrashOutput(GmailUsersMessagesTrashToolOutput):
    """Operation output for `users_messages_trash`."""
    pass

class UsersMessagesUntrashInput(GmailUsersMessagesUntrashToolInput):
    """Operation input for `users_messages_untrash`."""
    pass

class UsersMessagesUntrashOutput(GmailUsersMessagesUntrashToolOutput):
    """Operation output for `users_messages_untrash`."""
    pass

class GmailUsersMessagesResource(BaseResourceClient):
    """Operations grouped around the `users_messages` resource."""

    @operation(
        name='users_messages_batch_delete',
        title='UsersMessagesBatchDelete',
        input_model=UsersMessagesBatchDeleteInput,
        output_model=UsersMessagesBatchDeleteOutput,
        tools_used=('gmail_users_messages_batch_delete',),
        tags=tuple(['users']),
    )
    async def batch_delete(self, data: UsersMessagesBatchDeleteInput) -> UsersMessagesBatchDeleteOutput:
        """Deletes many messages by message ID. Provides no guarantees that messages were not already deleted or even existed at all.

Use this when you want to deletes many messages by message ID. Provides no guarantees that messages were not already deleted or even existed at all.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_messages_batch_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersMessagesBatchDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_messages_batch_modify',
        title='UsersMessagesBatchModify',
        input_model=UsersMessagesBatchModifyInput,
        output_model=UsersMessagesBatchModifyOutput,
        tools_used=('gmail_users_messages_batch_modify',),
        tags=tuple(['users']),
    )
    async def batch_modify(self, data: UsersMessagesBatchModifyInput) -> UsersMessagesBatchModifyOutput:
        """Modifies the labels on the specified messages.

Use this when you want to modifies the labels on the specified messages.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_messages_batch_modify')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersMessagesBatchModifyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_messages_delete',
        title='UsersMessagesDelete',
        input_model=UsersMessagesDeleteInput,
        output_model=UsersMessagesDeleteOutput,
        tools_used=('gmail_users_messages_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: UsersMessagesDeleteInput) -> UsersMessagesDeleteOutput:
        """Immediately and permanently deletes the specified message. This operation cannot be undone. Prefer `messages.trash` instead.

Use this when you want to immediately and permanently deletes the specified message. This operation cannot be undone. Prefer `messages.trash` instead.
Key inputs: fields, user_id, id."""
        tool = self._client.get_tool('gmail_users_messages_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersMessagesDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_messages_get',
        title='UsersMessagesGet',
        input_model=UsersMessagesGetInput,
        output_model=UsersMessagesGetOutput,
        tools_used=('gmail_users_messages_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: UsersMessagesGetInput) -> UsersMessagesGetOutput:
        """Gets the specified message.

Use this when you want to gets the specified message.
Key inputs: fields, user_id, id, format, metadata_headers."""
        tool = self._client.get_tool('gmail_users_messages_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersMessagesGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_messages_import',
        title='UsersMessagesImport',
        input_model=UsersMessagesImportInput,
        output_model=UsersMessagesImportOutput,
        tools_used=('gmail_users_messages_import',),
        tags=tuple(['users']),
    )
    async def import_(self, data: UsersMessagesImportInput) -> UsersMessagesImportOutput:
        """Imports a message into only this user's mailbox, with standard email delivery scanning and classification similar to receiving via SMTP. This method doesn't perform SPF checks, so it might not work for some spam messages, such as those attempting to perform domain spoofing. This method does not send a message. Note: This function doesn't trigger forwarding rules or filters set up by the user.

Use this when you want to imports a message into only this user's mailbox, with standard email delivery scanning and classification similar to receiving via SMTP. This method doesn't perform SPF checks, so it might not work for some spam messages, such as those attempting to perform domain spoofing. This method does not send a message. Note: This function doesn't trigger forwarding rules or filters set up by the user.
Key inputs: fields, user_id, deleted, internal_date_source, never_mark_spam, process_for_calendar, body."""
        tool = self._client.get_tool('gmail_users_messages_import')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersMessagesImportOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_messages_insert',
        title='UsersMessagesInsert',
        input_model=UsersMessagesInsertInput,
        output_model=UsersMessagesInsertOutput,
        tools_used=('gmail_users_messages_insert',),
        tags=tuple(['users']),
    )
    async def insert(self, data: UsersMessagesInsertInput) -> UsersMessagesInsertOutput:
        """Directly inserts a message into only this user's mailbox similar to `IMAP APPEND`, bypassing most scanning and classification. Does not send a message.

Use this when you want to directly inserts a message into only this user's mailbox similar to `IMAP APPEND`, bypassing most scanning and classification. Does not send a message.
Key inputs: fields, user_id, deleted, internal_date_source, body."""
        tool = self._client.get_tool('gmail_users_messages_insert')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersMessagesInsertOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_messages_list',
        title='UsersMessagesList',
        input_model=UsersMessagesListInput,
        output_model=UsersMessagesListOutput,
        tools_used=('gmail_users_messages_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: UsersMessagesListInput) -> UsersMessagesListOutput:
        """Lists the messages in the user's mailbox.

Use this when you want to lists the messages in the user's mailbox.
Key inputs: fields, user_id, include_spam_trash, label_ids, max_results, page_token, q."""
        tool = self._client.get_tool('gmail_users_messages_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersMessagesListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_messages_modify',
        title='UsersMessagesModify',
        input_model=UsersMessagesModifyInput,
        output_model=UsersMessagesModifyOutput,
        tools_used=('gmail_users_messages_modify',),
        tags=tuple(['users']),
    )
    async def modify(self, data: UsersMessagesModifyInput) -> UsersMessagesModifyOutput:
        """Modifies the labels on the specified message.

Use this when you want to modifies the labels on the specified message.
Key inputs: fields, user_id, id, body."""
        tool = self._client.get_tool('gmail_users_messages_modify')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersMessagesModifyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_messages_send',
        title='UsersMessagesSend',
        input_model=UsersMessagesSendInput,
        output_model=UsersMessagesSendOutput,
        tools_used=('gmail_users_messages_send',),
        tags=tuple(['users']),
    )
    async def send(self, data: UsersMessagesSendInput) -> UsersMessagesSendOutput:
        """Sends the specified message to the recipients in the `To`, `Cc`, and `Bcc` headers. For example usage, see [Sending email](https://developers.google.com/gmail/api/guides/sending).

Use this when you want to sends the specified message to the recipients in the `To`, `Cc`, and `Bcc` headers. For example usage, see [Sending email](https://developers.google.com/gmail/api/guides/sending).
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_messages_send')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersMessagesSendOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_messages_trash',
        title='UsersMessagesTrash',
        input_model=UsersMessagesTrashInput,
        output_model=UsersMessagesTrashOutput,
        tools_used=('gmail_users_messages_trash',),
        tags=tuple(['users']),
    )
    async def trash(self, data: UsersMessagesTrashInput) -> UsersMessagesTrashOutput:
        """Moves the specified message to the trash.

Use this when you want to moves the specified message to the trash.
Key inputs: fields, user_id, id."""
        tool = self._client.get_tool('gmail_users_messages_trash')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersMessagesTrashOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_messages_untrash',
        title='UsersMessagesUntrash',
        input_model=UsersMessagesUntrashInput,
        output_model=UsersMessagesUntrashOutput,
        tools_used=('gmail_users_messages_untrash',),
        tags=tuple(['users']),
    )
    async def untrash(self, data: UsersMessagesUntrashInput) -> UsersMessagesUntrashOutput:
        """Removes the specified message from the trash.

Use this when you want to removes the specified message from the trash.
Key inputs: fields, user_id, id."""
        tool = self._client.get_tool('gmail_users_messages_untrash')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersMessagesUntrashOutput.model_validate(coerce_tool_result(result))
