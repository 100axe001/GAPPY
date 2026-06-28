from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersThreadsDeleteToolInput, GmailUsersThreadsDeleteToolOutput, GmailUsersThreadsGetToolInput, GmailUsersThreadsGetToolOutput, GmailUsersThreadsListToolInput, GmailUsersThreadsListToolOutput, GmailUsersThreadsModifyToolInput, GmailUsersThreadsModifyToolOutput, GmailUsersThreadsTrashToolInput, GmailUsersThreadsTrashToolOutput, GmailUsersThreadsUntrashToolInput, GmailUsersThreadsUntrashToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ThreadsDeleteInput(GmailUsersThreadsDeleteToolInput):
    """Operation input for `threads_delete`."""
    pass

class ThreadsDeleteOutput(GmailUsersThreadsDeleteToolOutput):
    """Operation output for `threads_delete`."""
    pass

class ThreadsGetInput(GmailUsersThreadsGetToolInput):
    """Operation input for `threads_get`."""
    pass

class ThreadsGetOutput(GmailUsersThreadsGetToolOutput):
    """Operation output for `threads_get`."""
    pass

class ThreadsListInput(GmailUsersThreadsListToolInput):
    """Operation input for `threads_list`."""
    pass

class ThreadsListOutput(GmailUsersThreadsListToolOutput):
    """Operation output for `threads_list`."""
    pass

class ThreadsModifyInput(GmailUsersThreadsModifyToolInput):
    """Operation input for `threads_modify`."""
    pass

class ThreadsModifyOutput(GmailUsersThreadsModifyToolOutput):
    """Operation output for `threads_modify`."""
    pass

class ThreadsTrashInput(GmailUsersThreadsTrashToolInput):
    """Operation input for `threads_trash`."""
    pass

class ThreadsTrashOutput(GmailUsersThreadsTrashToolOutput):
    """Operation output for `threads_trash`."""
    pass

class ThreadsUntrashInput(GmailUsersThreadsUntrashToolInput):
    """Operation input for `threads_untrash`."""
    pass

class ThreadsUntrashOutput(GmailUsersThreadsUntrashToolOutput):
    """Operation output for `threads_untrash`."""
    pass

class GmailThreadsResource(BaseResourceClient):
    """Operations for the `threads` resource."""

    @operation(
        name='threads_delete',
        title='ThreadsDelete',
        input_model=ThreadsDeleteInput,
        output_model=ThreadsDeleteOutput,
        tools_used=('gmail_users_threads_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: ThreadsDeleteInput) -> ThreadsDeleteOutput:
        """Immediately and permanently deletes the specified thread. Any messages that belong to the thread are also deleted. This operation cannot be undone. Prefer `threads.trash` instead.

Important inputs: fields, user_id, id"""
        tool = self._client.get_tool('gmail_users_threads_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ThreadsDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='threads_get',
        title='ThreadsGet',
        input_model=ThreadsGetInput,
        output_model=ThreadsGetOutput,
        tools_used=('gmail_users_threads_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: ThreadsGetInput) -> ThreadsGetOutput:
        """Gets the specified thread.

Important inputs: fields, user_id, id, format, metadata_headers"""
        tool = self._client.get_tool('gmail_users_threads_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ThreadsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='threads_list',
        title='ThreadsList',
        input_model=ThreadsListInput,
        output_model=ThreadsListOutput,
        tools_used=('gmail_users_threads_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: ThreadsListInput) -> ThreadsListOutput:
        """Lists the threads in the user's mailbox.

Important inputs: fields, user_id, include_spam_trash, label_ids, max_results, page_token, q"""
        tool = self._client.get_tool('gmail_users_threads_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ThreadsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='threads_modify',
        title='ThreadsModify',
        input_model=ThreadsModifyInput,
        output_model=ThreadsModifyOutput,
        tools_used=('gmail_users_threads_modify',),
        tags=tuple(['users']),
    )
    async def modify(self, data: ThreadsModifyInput) -> ThreadsModifyOutput:
        """Modifies the labels applied to the thread. This applies to all messages in the thread.

Important inputs: fields, user_id, id, body"""
        tool = self._client.get_tool('gmail_users_threads_modify')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ThreadsModifyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='threads_trash',
        title='ThreadsTrash',
        input_model=ThreadsTrashInput,
        output_model=ThreadsTrashOutput,
        tools_used=('gmail_users_threads_trash',),
        tags=tuple(['users']),
    )
    async def trash(self, data: ThreadsTrashInput) -> ThreadsTrashOutput:
        """Moves the specified thread to the trash. Any messages that belong to the thread are also moved to the trash.

Important inputs: fields, user_id, id"""
        tool = self._client.get_tool('gmail_users_threads_trash')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ThreadsTrashOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='threads_untrash',
        title='ThreadsUntrash',
        input_model=ThreadsUntrashInput,
        output_model=ThreadsUntrashOutput,
        tools_used=('gmail_users_threads_untrash',),
        tags=tuple(['users']),
    )
    async def untrash(self, data: ThreadsUntrashInput) -> ThreadsUntrashOutput:
        """Removes the specified thread from the trash. Any messages that belong to the thread are also removed from the trash.

Important inputs: fields, user_id, id"""
        tool = self._client.get_tool('gmail_users_threads_untrash')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ThreadsUntrashOutput.model_validate(coerce_tool_result(result))
