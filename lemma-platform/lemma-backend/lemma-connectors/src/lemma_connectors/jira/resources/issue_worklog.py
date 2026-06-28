from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueWorklogToolInput, GetIssueWorklogToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueWorklogInput(GetIssueWorklogToolInput):
    """Operation input for `get_issue_worklog`."""
    pass

class GetIssueWorklogOutput(GetIssueWorklogToolOutput):
    """Operation output for `get_issue_worklog`."""
    pass

class JiraIssueWorklogResource(BaseResourceClient):
    """Operations for the `issue_worklog` resource."""

    @operation(
        name='get_issue_worklog',
        title='GetIssueWorklog',
        input_model=GetIssueWorklogInput,
        output_model=GetIssueWorklogOutput,
        tools_used=('get_issue_worklog',),
        tags=tuple(['Issue worklogs']),
    )
    async def get(self, data: GetIssueWorklogInput) -> GetIssueWorklogOutput:
        """Returns worklogs for an issue, starting from the oldest worklog or from the worklog started on or after a date and time. Time tracking must be enabled in Jira, otherwise this operation returns an error. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM). This operation can be accessed anonymously. **[Permissions](#permissions) required:** Workloads are only returned where the user has: * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

Important inputs: issue_id_or_key, start_at, max_results, started_after, started_before, expand"""
        tool = self._client.get_tool('get_issue_worklog')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueWorklogOutput.model_validate(coerce_tool_result(result))
