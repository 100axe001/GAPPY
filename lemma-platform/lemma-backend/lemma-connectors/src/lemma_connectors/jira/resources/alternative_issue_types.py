from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAlternativeIssueTypesToolInput, GetAlternativeIssueTypesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAlternativeIssueTypesInput(GetAlternativeIssueTypesToolInput):
    """Operation input for `get_alternative_issue_types`."""
    pass

class GetAlternativeIssueTypesOutput(GetAlternativeIssueTypesToolOutput):
    """Operation output for `get_alternative_issue_types`."""
    pass

class JiraAlternativeIssueTypesResource(BaseResourceClient):
    """Operations for the `alternative_issue_types` resource."""

    @operation(
        name='get_alternative_issue_types',
        title='GetAlternativeIssueTypes',
        input_model=GetAlternativeIssueTypesInput,
        output_model=GetAlternativeIssueTypesOutput,
        tools_used=('get_alternative_issue_types',),
        tags=tuple(['Issue types']),
    )
    async def get(self, data: GetAlternativeIssueTypesInput) -> GetAlternativeIssueTypesOutput:
        """Returns a list of issue types that can be used to replace the issue type. The alternative issue types are those assigned to the same workflow scheme, field configuration scheme, and screen scheme. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: id"""
        tool = self._client.get_tool('get_alternative_issue_types')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAlternativeIssueTypesOutput.model_validate(coerce_tool_result(result))
