from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersMessagesBatchDeleteToolInput, GmailUsersMessagesBatchDeleteToolOutput, GmailUsersMessagesBatchModifyToolInput, GmailUsersMessagesBatchModifyToolOutput, GmailUsersMessagesDeleteToolInput, GmailUsersMessagesDeleteToolOutput, GmailUsersMessagesGetToolInput, GmailUsersMessagesGetToolOutput, GmailUsersMessagesImportToolInput, GmailUsersMessagesImportToolOutput, GmailUsersMessagesInsertToolInput, GmailUsersMessagesInsertToolOutput, GmailUsersMessagesListToolInput, GmailUsersMessagesListToolOutput, GmailUsersMessagesModifyToolInput, GmailUsersMessagesModifyToolOutput, GmailUsersMessagesSendToolInput, GmailUsersMessagesSendToolOutput, GmailUsersMessagesTrashToolInput, GmailUsersMessagesTrashToolOutput, GmailUsersMessagesUntrashToolInput, GmailUsersMessagesUntrashToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class MessagesBatchDeleteInput(GmailUsersMessagesBatchDeleteToolInput):
    """Operation input for `messages_batch_delete`."""
    pass

class MessagesBatchDeleteOutput(GmailUsersMessagesBatchDeleteToolOutput):
    """Operation output for `messages_batch_delete`."""
    pass

class MessagesBatchModifyInput(GmailUsersMessagesBatchModifyToolInput):
    """Operation input for `messages_batch_modify`."""
    pass

class MessagesBatchModifyOutput(GmailUsersMessagesBatchModifyToolOutput):
    """Operation output for `messages_batch_modify`."""
    pass

class MessagesDeleteInput(GmailUsersMessagesDeleteToolInput):
    """Operation input for `messages_delete`."""
    pass

class MessagesDeleteOutput(GmailUsersMessagesDeleteToolOutput):
    """Operation output for `messages_delete`."""
    pass

class MessagesGetInput(GmailUsersMessagesGetToolInput):
    """Operation input for `messages_get`."""
    pass

class MessagesGetOutput(GmailUsersMessagesGetToolOutput):
    """Operation output for `messages_get`."""
    pass

class MessagesImportInput(GmailUsersMessagesImportToolInput):
    """Operation input for `messages_import`."""
    pass

class MessagesImportOutput(GmailUsersMessagesImportToolOutput):
    """Operation output for `messages_import`."""
    pass

class MessagesInsertInput(GmailUsersMessagesInsertToolInput):
    """Operation input for `messages_insert`."""
    pass

class MessagesInsertOutput(GmailUsersMessagesInsertToolOutput):
    """Operation output for `messages_insert`."""
    pass

class MessagesListInput(GmailUsersMessagesListToolInput):
    """Operation input for `messages_list`."""
    pass

class MessagesListOutput(GmailUsersMessagesListToolOutput):
    """Operation output for `messages_list`."""
    pass

class MessagesModifyInput(GmailUsersMessagesModifyToolInput):
    """Operation input for `messages_modify`."""
    pass

class MessagesModifyOutput(GmailUsersMessagesModifyToolOutput):
    """Operation output for `messages_modify`."""
    pass

class MessagesSendInput(GmailUsersMessagesSendToolInput):
    """Operation input for `messages_send`."""
    pass

class MessagesSendOutput(GmailUsersMessagesSendToolOutput):
    """Operation output for `messages_send`."""
    pass

class MessagesTrashInput(GmailUsersMessagesTrashToolInput):
    """Operation input for `messages_trash`."""
    pass

class MessagesTrashOutput(GmailUsersMessagesTrashToolOutput):
    """Operation output for `messages_trash`."""
    pass

class MessagesUntrashInput(GmailUsersMessagesUntrashToolInput):
    """Operation input for `messages_untrash`."""
    pass

class MessagesUntrashOutput(GmailUsersMessagesUntrashToolOutput):
    """Operation output for `messages_untrash`."""
    pass

class GmailMessagesResource(BaseResourceClient):
    """Operations for the `messages` resource."""

    @operation(
        name='messages_batch_delete',
        title='MessagesBatchDelete',
        input_model=MessagesBatchDeleteInput,
        output_model=MessagesBatchDeleteOutput,
        tools_used=('gmail_users_messages_batch_delete',),
        tags=tuple(['users']),
    )
    async def batch_delete(self, data: MessagesBatchDeleteInput) -> MessagesBatchDeleteOutput:
        """Deletes many messages by message ID. Provides no guarantees that messages were not already deleted or even existed at all.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_messages_batch_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MessagesBatchDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='messages_batch_modify',
        title='MessagesBatchModify',
        input_model=MessagesBatchModifyInput,
        output_model=MessagesBatchModifyOutput,
        tools_used=('gmail_users_messages_batch_modify',),
        tags=tuple(['users']),
    )
    async def batch_modify(self, data: MessagesBatchModifyInput) -> MessagesBatchModifyOutput:
        """Modifies the labels on the specified messages.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_messages_batch_modify')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MessagesBatchModifyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='messages_delete',
        title='MessagesDelete',
        input_model=MessagesDeleteInput,
        output_model=MessagesDeleteOutput,
        tools_used=('gmail_users_messages_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: MessagesDeleteInput) -> MessagesDeleteOutput:
        """Immediately and permanently deletes the specified message. This operation cannot be undone. Prefer `messages.trash` instead.

Important inputs: fields, user_id, id"""
        tool = self._client.get_tool('gmail_users_messages_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MessagesDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='messages_get',
        title='MessagesGet',
        input_model=MessagesGetInput,
        output_model=MessagesGetOutput,
        tools_used=('gmail_users_messages_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: MessagesGetInput) -> MessagesGetOutput:
        """Gets the specified message.

Important inputs: fields, user_id, id, format, metadata_headers"""
        tool = self._client.get_tool('gmail_users_messages_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MessagesGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='messages_import',
        title='MessagesImport',
        input_model=MessagesImportInput,
        output_model=MessagesImportOutput,
        tools_used=('gmail_users_messages_import',),
        tags=tuple(['users']),
    )
    async def import_(self, data: MessagesImportInput) -> MessagesImportOutput:
        """Imports a message into only this user's mailbox, with standard email delivery scanning and classification similar to receiving via SMTP. This method doesn't perform SPF checks, so it might not work for some spam messages, such as those attempting to perform domain spoofing. This method does not send a message. Note: This function doesn't trigger forwarding rules or filters set up by the user.

Important inputs: fields, user_id, deleted, internal_date_source, never_mark_spam, process_for_calendar, body"""
        tool = self._client.get_tool('gmail_users_messages_import')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MessagesImportOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='messages_insert',
        title='MessagesInsert',
        input_model=MessagesInsertInput,
        output_model=MessagesInsertOutput,
        tools_used=('gmail_users_messages_insert',),
        tags=tuple(['users']),
    )
    async def insert(self, data: MessagesInsertInput) -> MessagesInsertOutput:
        """Directly inserts a message into only this user's mailbox similar to `IMAP APPEND`, bypassing most scanning and classification. Does not send a message.

Important inputs: fields, user_id, deleted, internal_date_source, body"""
        tool = self._client.get_tool('gmail_users_messages_insert')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MessagesInsertOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='messages_list',
        title='MessagesList',
        input_model=MessagesListInput,
        output_model=MessagesListOutput,
        tools_used=('gmail_users_messages_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: MessagesListInput) -> MessagesListOutput:
        """Lists the messages in the user's mailbox.

Important inputs: fields, user_id, include_spam_trash, label_ids, max_results, page_token, q"""
        tool = self._client.get_tool('gmail_users_messages_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MessagesListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='messages_modify',
        title='MessagesModify',
        input_model=MessagesModifyInput,
        output_model=MessagesModifyOutput,
        tools_used=('gmail_users_messages_modify',),
        tags=tuple(['users']),
    )
    async def modify(self, data: MessagesModifyInput) -> MessagesModifyOutput:
        """Modifies the labels on the specified message.

Important inputs: fields, user_id, id, body"""
        tool = self._client.get_tool('gmail_users_messages_modify')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MessagesModifyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='messages_send',
        title='MessagesSend',
        input_model=MessagesSendInput,
        output_model=MessagesSendOutput,
        tools_used=('gmail_users_messages_send',),
        tags=tuple(['users']),
    )
    async def send(self, data: MessagesSendInput) -> MessagesSendOutput:
        """Sends the specified message to the recipients in the `To`, `Cc`, and `Bcc` headers. For example usage, see [Sending email](https://developers.google.com/gmail/api/guides/sending).

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_messages_send')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MessagesSendOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='messages_trash',
        title='MessagesTrash',
        input_model=MessagesTrashInput,
        output_model=MessagesTrashOutput,
        tools_used=('gmail_users_messages_trash',),
        tags=tuple(['users']),
    )
    async def trash(self, data: MessagesTrashInput) -> MessagesTrashOutput:
        """Moves the specified message to the trash.

Important inputs: fields, user_id, id"""
        tool = self._client.get_tool('gmail_users_messages_trash')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MessagesTrashOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='messages_untrash',
        title='MessagesUntrash',
        input_model=MessagesUntrashInput,
        output_model=MessagesUntrashOutput,
        tools_used=('gmail_users_messages_untrash',),
        tags=tuple(['users']),
    )
    async def untrash(self, data: MessagesUntrashInput) -> MessagesUntrashOutput:
        """Removes the specified message from the trash.

Important inputs: fields, user_id, id"""
        tool = self._client.get_tool('gmail_users_messages_untrash')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MessagesUntrashOutput.model_validate(coerce_tool_result(result))
