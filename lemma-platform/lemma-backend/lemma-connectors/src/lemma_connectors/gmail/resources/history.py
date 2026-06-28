from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersHistoryListToolInput, GmailUsersHistoryListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class HistoryListInput(GmailUsersHistoryListToolInput):
    """Operation input for `history_list`."""
    pass

class HistoryListOutput(GmailUsersHistoryListToolOutput):
    """Operation output for `history_list`."""
    pass

class GmailHistoryResource(BaseResourceClient):
    """Operations for the `history` resource."""

    @operation(
        name='history_list',
        title='HistoryList',
        input_model=HistoryListInput,
        output_model=HistoryListOutput,
        tools_used=('gmail_users_history_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: HistoryListInput) -> HistoryListOutput:
        """Lists the history of all changes to the given mailbox. History results are returned in chronological order (increasing `historyId`).

Important inputs: fields, user_id, history_types, label_id, max_results, page_token, start_history_id"""
        tool = self._client.get_tool('gmail_users_history_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return HistoryListOutput.model_validate(coerce_tool_result(result))
