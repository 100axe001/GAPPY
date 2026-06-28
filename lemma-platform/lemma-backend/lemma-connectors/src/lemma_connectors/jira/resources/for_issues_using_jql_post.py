from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import SearchForIssuesUsingJqlPostToolInput, SearchForIssuesUsingJqlPostToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SearchForIssuesUsingJqlPostInput(SearchForIssuesUsingJqlPostToolInput):
    """Operation input for `search_for_issues_using_jql_post`."""
    pass

class SearchForIssuesUsingJqlPostOutput(SearchForIssuesUsingJqlPostToolOutput):
    """Operation output for `search_for_issues_using_jql_post`."""
    pass

class JiraForIssuesUsingJqlPostResource(BaseResourceClient):
    """Operations for the `for_issues_using_jql_post` resource."""

    @operation(
        name='search_for_issues_using_jql_post',
        title='SearchForIssuesUsingJqlPost',
        input_model=SearchForIssuesUsingJqlPostInput,
        output_model=SearchForIssuesUsingJqlPostOutput,
        tools_used=('search_for_issues_using_jql_post',),
        tags=tuple(['Issue search']),
    )
    async def search(self, data: SearchForIssuesUsingJqlPostInput) -> SearchForIssuesUsingJqlPostOutput:
        """Searches for issues using [JQL](https://confluence.atlassian.com/x/egORLQ). There is a [GET](#api-rest-api-3-search-get) version of this resource that can be used for smaller JQL query expressions. This operation can be accessed anonymously. **[Permissions](#permissions) required:** Issues are included in the response where the user has: * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: body"""
        tool = self._client.get_tool('search_for_issues_using_jql_post')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SearchForIssuesUsingJqlPostOutput.model_validate(coerce_tool_result(result))
