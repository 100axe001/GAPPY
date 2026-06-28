from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllIssueTypeSchemesToolInput, GetAllIssueTypeSchemesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllIssueTypeSchemesInput(GetAllIssueTypeSchemesToolInput):
    """Operation input for `get_all_issue_type_schemes`."""
    pass

class GetAllIssueTypeSchemesOutput(GetAllIssueTypeSchemesToolOutput):
    """Operation output for `get_all_issue_type_schemes`."""
    pass

class JiraAllIssueTypeSchemesResource(BaseResourceClient):
    """Operations for the `all_issue_type_schemes` resource."""

    @operation(
        name='get_all_issue_type_schemes',
        title='GetAllIssueTypeSchemes',
        input_model=GetAllIssueTypeSchemesInput,
        output_model=GetAllIssueTypeSchemesOutput,
        tools_used=('get_all_issue_type_schemes',),
        tags=tuple(['Issue type schemes']),
    )
    async def get(self, data: GetAllIssueTypeSchemesInput) -> GetAllIssueTypeSchemesOutput:
        """Returns a [paginated](#pagination) list of issue type schemes. Only issue type schemes used in classic projects are returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, id, order_by, expand, query_string"""
        tool = self._client.get_tool('get_all_issue_type_schemes')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllIssueTypeSchemesOutput.model_validate(coerce_tool_result(result))
