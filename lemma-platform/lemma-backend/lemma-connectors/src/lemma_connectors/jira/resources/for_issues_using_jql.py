from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import SearchForIssuesUsingJqlToolInput, SearchForIssuesUsingJqlToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SearchForIssuesUsingJqlInput(SearchForIssuesUsingJqlToolInput):
    """Operation input for `search_for_issues_using_jql`."""
    pass

class SearchForIssuesUsingJqlOutput(SearchForIssuesUsingJqlToolOutput):
    """Operation output for `search_for_issues_using_jql`."""
    pass

class JiraForIssuesUsingJqlResource(BaseResourceClient):
    """Operations for the `for_issues_using_jql` resource."""

    @operation(
        name='search_for_issues_using_jql',
        title='SearchForIssuesUsingJql',
        input_model=SearchForIssuesUsingJqlInput,
        output_model=SearchForIssuesUsingJqlOutput,
        tools_used=('search_for_issues_using_jql',),
        tags=tuple(['Issue search']),
    )
    async def search(self, data: SearchForIssuesUsingJqlInput) -> SearchForIssuesUsingJqlOutput:
        """Searches for issues using [JQL](https://confluence.atlassian.com/x/egORLQ). If the JQL query expression is too large to be encoded as a query parameter, use the [POST](#api-rest-api-3-search-post) version of this resource. This operation can be accessed anonymously. **[Permissions](#permissions) required:** Issues are included in the response where the user has: * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the issue. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: jql, start_at, max_results, validate_query, fields, expand, properties, fields_by_keys"""
        tool = self._client.get_tool('search_for_issues_using_jql')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SearchForIssuesUsingJqlOutput.model_validate(coerce_tool_result(result))
