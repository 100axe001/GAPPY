from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIsWatchingIssueBulkToolInput, GetIsWatchingIssueBulkToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIsWatchingIssueBulkInput(GetIsWatchingIssueBulkToolInput):
    """Operation input for `get_is_watching_issue_bulk`."""
    pass

class GetIsWatchingIssueBulkOutput(GetIsWatchingIssueBulkToolOutput):
    """Operation output for `get_is_watching_issue_bulk`."""
    pass

class JiraIsWatchingIssueBulkResource(BaseResourceClient):
    """Operations for the `is_watching_issue_bulk` resource."""

    @operation(
        name='get_is_watching_issue_bulk',
        title='GetIsWatchingIssueBulk',
        input_model=GetIsWatchingIssueBulkInput,
        output_model=GetIsWatchingIssueBulkOutput,
        tools_used=('get_is_watching_issue_bulk',),
        tags=tuple(['Issue watchers']),
    )
    async def get(self, data: GetIsWatchingIssueBulkInput) -> GetIsWatchingIssueBulkOutput:
        """Returns, for the user, details of the watched status of issues from a list. If an issue ID is invalid, the returned watched status is `false`. This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: body"""
        tool = self._client.get_tool('get_is_watching_issue_bulk')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIsWatchingIssueBulkOutput.model_validate(coerce_tool_result(result))
