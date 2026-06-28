from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetComponentRelatedIssuesToolInput, GetComponentRelatedIssuesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetComponentRelatedIssuesInput(GetComponentRelatedIssuesToolInput):
    """Operation input for `get_component_related_issues`."""
    pass

class GetComponentRelatedIssuesOutput(GetComponentRelatedIssuesToolOutput):
    """Operation output for `get_component_related_issues`."""
    pass

class JiraComponentRelatedIssuesResource(BaseResourceClient):
    """Operations for the `component_related_issues` resource."""

    @operation(
        name='get_component_related_issues',
        title='GetComponentRelatedIssues',
        input_model=GetComponentRelatedIssuesInput,
        output_model=GetComponentRelatedIssuesOutput,
        tools_used=('get_component_related_issues',),
        tags=tuple(['Project components']),
    )
    async def get(self, data: GetComponentRelatedIssuesInput) -> GetComponentRelatedIssuesOutput:
        """Returns the counts of issues assigned to the component. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: id"""
        tool = self._client.get_tool('get_component_related_issues')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetComponentRelatedIssuesOutput.model_validate(coerce_tool_result(result))
