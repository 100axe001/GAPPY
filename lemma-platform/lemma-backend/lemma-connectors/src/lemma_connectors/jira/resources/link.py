from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import LinkIssuesToolInput, LinkIssuesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class LinkIssuesInput(LinkIssuesToolInput):
    """Operation input for `link_issues`."""
    pass

class LinkIssuesOutput(LinkIssuesToolOutput):
    """Operation output for `link_issues`."""
    pass

class JiraLinkResource(BaseResourceClient):
    """Operations for the `link` resource."""

    @operation(
        name='link_issues',
        title='LinkIssues',
        input_model=LinkIssuesInput,
        output_model=LinkIssuesOutput,
        tools_used=('link_issues',),
        tags=tuple(['Issue links']),
    )
    async def issues(self, data: LinkIssuesInput) -> LinkIssuesOutput:
        """Creates a link between two issues. Use this operation to indicate a relationship between two issues and optionally add a comment to the from (outward) issue. To use this resource the site must have [Issue Linking](https://confluence.atlassian.com/x/yoXKM) enabled. This resource returns nothing on the creation of an issue link. To obtain the ID of the issue link, use `https://your-domain.atlassian.net/rest/api/3/issue/[linked issue key]?fields=issuelinks`. If the link request duplicates a link, the response indicates that the issue link was created. If the request included a comment, the comment is added. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse project* [project permission](https://confluence.atlassian.com/x/yodKLg) for all the projects containing the issues to be linked, * *Link issues* [project permission](https://confluence.atlassian.com/x/yodKLg) on the project containing the from (outward) issue, * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * If the comment has visibility restrictions, belongs to the group or has the role visibility is restricted to.

Important inputs: body"""
        tool = self._client.get_tool('link_issues')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return LinkIssuesOutput.model_validate(coerce_tool_result(result))
