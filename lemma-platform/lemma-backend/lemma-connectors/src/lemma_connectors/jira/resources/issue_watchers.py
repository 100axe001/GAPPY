from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueWatchersToolInput, GetIssueWatchersToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueWatchersInput(GetIssueWatchersToolInput):
    """Operation input for `get_issue_watchers`."""
    pass

class GetIssueWatchersOutput(GetIssueWatchersToolOutput):
    """Operation output for `get_issue_watchers`."""
    pass

class JiraIssueWatchersResource(BaseResourceClient):
    """Operations for the `issue_watchers` resource."""

    @operation(
        name='get_issue_watchers',
        title='GetIssueWatchers',
        input_model=GetIssueWatchersInput,
        output_model=GetIssueWatchersOutput,
        tools_used=('get_issue_watchers',),
        tags=tuple(['Issue watchers']),
    )
    async def get(self, data: GetIssueWatchersInput) -> GetIssueWatchersOutput:
        """Returns the watchers for an issue. This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is ini * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * To see details of users on the watchlist other than themselves, *View voters and watchers* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.

Important inputs: issue_id_or_key"""
        tool = self._client.get_tool('get_issue_watchers')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueWatchersOutput.model_validate(coerce_tool_result(result))
