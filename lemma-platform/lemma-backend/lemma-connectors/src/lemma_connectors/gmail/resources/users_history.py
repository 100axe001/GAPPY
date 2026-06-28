from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersHistoryListToolInput, GmailUsersHistoryListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersHistoryListInput(GmailUsersHistoryListToolInput):
    """Operation input for `users_history_list`."""
    pass

class UsersHistoryListOutput(GmailUsersHistoryListToolOutput):
    """Operation output for `users_history_list`."""
    pass

class GmailUsersHistoryResource(BaseResourceClient):
    """Operations grouped around the `users_history` resource."""

    @operation(
        name='users_history_list',
        title='UsersHistoryList',
        input_model=UsersHistoryListInput,
        output_model=UsersHistoryListOutput,
        tools_used=('gmail_users_history_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: UsersHistoryListInput) -> UsersHistoryListOutput:
        """Lists the history of all changes to the given mailbox. History results are returned in chronological order (increasing `historyId`).

Use this when you want to lists the history of all changes to the given mailbox. History results are returned in chronological order (increasing `historyId`).
Key inputs: fields, user_id, history_types, label_id, max_results, page_token, start_history_id."""
        tool = self._client.get_tool('gmail_users_history_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersHistoryListOutput.model_validate(coerce_tool_result(result))
