from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import MatchIssuesToolInput, MatchIssuesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class MatchIssuesInput(MatchIssuesToolInput):
    """Operation input for `match_issues`."""
    pass

class MatchIssuesOutput(MatchIssuesToolOutput):
    """Operation output for `match_issues`."""
    pass

class JiraMatchResource(BaseResourceClient):
    """Operations for the `match` resource."""

    @operation(
        name='match_issues',
        title='MatchIssues',
        input_model=MatchIssuesInput,
        output_model=MatchIssuesOutput,
        tools_used=('match_issues',),
        tags=tuple(['Issue search']),
    )
    async def issues(self, data: MatchIssuesInput) -> MatchIssuesOutput:
        """Checks whether one or more issues would be returned by one or more JQL queries. **[Permissions](#permissions) required:** None, however, issues are only matched against JQL queries where the user has: * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: body"""
        tool = self._client.get_tool('match_issues')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MatchIssuesOutput.model_validate(coerce_tool_result(result))
