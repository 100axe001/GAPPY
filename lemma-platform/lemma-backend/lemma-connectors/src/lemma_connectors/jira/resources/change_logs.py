from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetChangeLogsToolInput, GetChangeLogsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetChangeLogsInput(GetChangeLogsToolInput):
    """Operation input for `get_change_logs`."""
    pass

class GetChangeLogsOutput(GetChangeLogsToolOutput):
    """Operation output for `get_change_logs`."""
    pass

class JiraChangeLogsResource(BaseResourceClient):
    """Operations for the `change_logs` resource."""

    @operation(
        name='get_change_logs',
        title='GetChangeLogs',
        input_model=GetChangeLogsInput,
        output_model=GetChangeLogsOutput,
        tools_used=('get_change_logs',),
        tags=tuple(['Issues']),
    )
    async def get(self, data: GetChangeLogsInput) -> GetChangeLogsOutput:
        """Returns a [paginated](#pagination) list of all changelogs for an issue sorted by date, starting from the oldest. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, start_at, max_results"""
        tool = self._client.get_tool('get_change_logs')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetChangeLogsOutput.model_validate(coerce_tool_result(result))
