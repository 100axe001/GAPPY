from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetVersionUnresolvedIssuesToolInput, GetVersionUnresolvedIssuesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetVersionUnresolvedIssuesInput(GetVersionUnresolvedIssuesToolInput):
    """Operation input for `get_version_unresolved_issues`."""
    pass

class GetVersionUnresolvedIssuesOutput(GetVersionUnresolvedIssuesToolOutput):
    """Operation output for `get_version_unresolved_issues`."""
    pass

class JiraVersionUnresolvedIssuesResource(BaseResourceClient):
    """Operations for the `version_unresolved_issues` resource."""

    @operation(
        name='get_version_unresolved_issues',
        title='GetVersionUnresolvedIssues',
        input_model=GetVersionUnresolvedIssuesInput,
        output_model=GetVersionUnresolvedIssuesOutput,
        tools_used=('get_version_unresolved_issues',),
        tags=tuple(['Project versions']),
    )
    async def get(self, data: GetVersionUnresolvedIssuesInput) -> GetVersionUnresolvedIssuesOutput:
        """Returns counts of the issues and unresolved issues for the project version. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.

Important inputs: id"""
        tool = self._client.get_tool('get_version_unresolved_issues')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetVersionUnresolvedIssuesOutput.model_validate(coerce_tool_result(result))
