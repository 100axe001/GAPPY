from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetRemoteIssueLinksToolInput, GetRemoteIssueLinksToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetRemoteIssueLinksInput(GetRemoteIssueLinksToolInput):
    """Operation input for `get_remote_issue_links`."""
    pass

class GetRemoteIssueLinksOutput(GetRemoteIssueLinksToolOutput):
    """Operation output for `get_remote_issue_links`."""
    pass

class JiraRemoteIssueLinksResource(BaseResourceClient):
    """Operations for the `remote_issue_links` resource."""

    @operation(
        name='get_remote_issue_links',
        title='GetRemoteIssueLinks',
        input_model=GetRemoteIssueLinksInput,
        output_model=GetRemoteIssueLinksOutput,
        tools_used=('get_remote_issue_links',),
        tags=tuple(['Issue remote links']),
    )
    async def get(self, data: GetRemoteIssueLinksInput) -> GetRemoteIssueLinksOutput:
        """Returns the remote issue links for an issue. When a remote issue link global ID is provided the record with that global ID is returned, otherwise all remote issue links are returned. Where a global ID includes reserved URL characters these must be escaped in the request. For example, pass `system=http://www.mycompany.com/support&id=1` as `system%3Dhttp%3A%2F%2Fwww.mycompany.com%2Fsupport%26id%3D1`. This operation requires [issue linking to be active](https://confluence.atlassian.com/x/yoXKM). This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, global_id"""
        tool = self._client.get_tool('get_remote_issue_links')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetRemoteIssueLinksOutput.model_validate(coerce_tool_result(result))
