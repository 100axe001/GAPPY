from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersThreadsDeleteToolInput, GmailUsersThreadsDeleteToolOutput, GmailUsersThreadsGetToolInput, GmailUsersThreadsGetToolOutput, GmailUsersThreadsListToolInput, GmailUsersThreadsListToolOutput, GmailUsersThreadsModifyToolInput, GmailUsersThreadsModifyToolOutput, GmailUsersThreadsTrashToolInput, GmailUsersThreadsTrashToolOutput, GmailUsersThreadsUntrashToolInput, GmailUsersThreadsUntrashToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersThreadsDeleteInput(GmailUsersThreadsDeleteToolInput):
    """Operation input for `users_threads_delete`."""
    pass

class UsersThreadsDeleteOutput(GmailUsersThreadsDeleteToolOutput):
    """Operation output for `users_threads_delete`."""
    pass

class UsersThreadsGetInput(GmailUsersThreadsGetToolInput):
    """Operation input for `users_threads_get`."""
    pass

class UsersThreadsGetOutput(GmailUsersThreadsGetToolOutput):
    """Operation output for `users_threads_get`."""
    pass

class UsersThreadsListInput(GmailUsersThreadsListToolInput):
    """Operation input for `users_threads_list`."""
    pass

class UsersThreadsListOutput(GmailUsersThreadsListToolOutput):
    """Operation output for `users_threads_list`."""
    pass

class UsersThreadsModifyInput(GmailUsersThreadsModifyToolInput):
    """Operation input for `users_threads_modify`."""
    pass

class UsersThreadsModifyOutput(GmailUsersThreadsModifyToolOutput):
    """Operation output for `users_threads_modify`."""
    pass

class UsersThreadsTrashInput(GmailUsersThreadsTrashToolInput):
    """Operation input for `users_threads_trash`."""
    pass

class UsersThreadsTrashOutput(GmailUsersThreadsTrashToolOutput):
    """Operation output for `users_threads_trash`."""
    pass

class UsersThreadsUntrashInput(GmailUsersThreadsUntrashToolInput):
    """Operation input for `users_threads_untrash`."""
    pass

class UsersThreadsUntrashOutput(GmailUsersThreadsUntrashToolOutput):
    """Operation output for `users_threads_untrash`."""
    pass

class GmailUsersThreadsResource(BaseResourceClient):
    """Operations grouped around the `users_threads` resource."""

    @operation(
        name='users_threads_delete',
        title='UsersThreadsDelete',
        input_model=UsersThreadsDeleteInput,
        output_model=UsersThreadsDeleteOutput,
        tools_used=('gmail_users_threads_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: UsersThreadsDeleteInput) -> UsersThreadsDeleteOutput:
        """Immediately and permanently deletes the specified thread. Any messages that belong to the thread are also deleted. This operation cannot be undone. Prefer `threads.trash` instead.

Use this when you want to immediately and permanently deletes the specified thread. Any messages that belong to the thread are also deleted. This operation cannot be undone. Prefer `threads.trash` instead.
Key inputs: fields, user_id, id."""
        tool = self._client.get_tool('gmail_users_threads_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersThreadsDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_threads_get',
        title='UsersThreadsGet',
        input_model=UsersThreadsGetInput,
        output_model=UsersThreadsGetOutput,
        tools_used=('gmail_users_threads_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: UsersThreadsGetInput) -> UsersThreadsGetOutput:
        """Gets the specified thread.

Use this when you want to gets the specified thread.
Key inputs: fields, user_id, id, format, metadata_headers."""
        tool = self._client.get_tool('gmail_users_threads_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersThreadsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_threads_list',
        title='UsersThreadsList',
        input_model=UsersThreadsListInput,
        output_model=UsersThreadsListOutput,
        tools_used=('gmail_users_threads_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: UsersThreadsListInput) -> UsersThreadsListOutput:
        """Lists the threads in the user's mailbox.

Use this when you want to lists the threads in the user's mailbox.
Key inputs: fields, user_id, include_spam_trash, label_ids, max_results, page_token, q."""
        tool = self._client.get_tool('gmail_users_threads_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersThreadsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_threads_modify',
        title='UsersThreadsModify',
        input_model=UsersThreadsModifyInput,
        output_model=UsersThreadsModifyOutput,
        tools_used=('gmail_users_threads_modify',),
        tags=tuple(['users']),
    )
    async def modify(self, data: UsersThreadsModifyInput) -> UsersThreadsModifyOutput:
        """Modifies the labels applied to the thread. This applies to all messages in the thread.

Use this when you want to modifies the labels applied to the thread. This applies to all messages in the thread.
Key inputs: fields, user_id, id, body."""
        tool = self._client.get_tool('gmail_users_threads_modify')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersThreadsModifyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_threads_trash',
        title='UsersThreadsTrash',
        input_model=UsersThreadsTrashInput,
        output_model=UsersThreadsTrashOutput,
        tools_used=('gmail_users_threads_trash',),
        tags=tuple(['users']),
    )
    async def trash(self, data: UsersThreadsTrashInput) -> UsersThreadsTrashOutput:
        """Moves the specified thread to the trash. Any messages that belong to the thread are also moved to the trash.

Use this when you want to moves the specified thread to the trash. Any messages that belong to the thread are also moved to the trash.
Key inputs: fields, user_id, id."""
        tool = self._client.get_tool('gmail_users_threads_trash')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersThreadsTrashOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_threads_untrash',
        title='UsersThreadsUntrash',
        input_model=UsersThreadsUntrashInput,
        output_model=UsersThreadsUntrashOutput,
        tools_used=('gmail_users_threads_untrash',),
        tags=tuple(['users']),
    )
    async def untrash(self, data: UsersThreadsUntrashInput) -> UsersThreadsUntrashOutput:
        """Removes the specified thread from the trash. Any messages that belong to the thread are also removed from the trash.

Use this when you want to removes the specified thread from the trash. Any messages that belong to the thread are also removed from the trash.
Key inputs: fields, user_id, id."""
        tool = self._client.get_tool('gmail_users_threads_untrash')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersThreadsUntrashOutput.model_validate(coerce_tool_result(result))
