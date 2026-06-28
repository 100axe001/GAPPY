from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetVersionRelatedIssuesToolInput, GetVersionRelatedIssuesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetVersionRelatedIssuesInput(GetVersionRelatedIssuesToolInput):
    """Operation input for `get_version_related_issues`."""
    pass

class GetVersionRelatedIssuesOutput(GetVersionRelatedIssuesToolOutput):
    """Operation output for `get_version_related_issues`."""
    pass

class JiraVersionRelatedIssuesResource(BaseResourceClient):
    """Operations for the `version_related_issues` resource."""

    @operation(
        name='get_version_related_issues',
        title='GetVersionRelatedIssues',
        input_model=GetVersionRelatedIssuesInput,
        output_model=GetVersionRelatedIssuesOutput,
        tools_used=('get_version_related_issues',),
        tags=tuple(['Project versions']),
    )
    async def get(self, data: GetVersionRelatedIssuesInput) -> GetVersionRelatedIssuesOutput:
        """Returns the following counts for a version: * Number of issues where the `fixVersion` is set to the version. * Number of issues where the `affectedVersion` is set to the version. * Number of issues where a version custom field is set to the version. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.

Important inputs: id"""
        tool = self._client.get_tool('get_version_related_issues')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetVersionRelatedIssuesOutput.model_validate(coerce_tool_result(result))
