from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueTypeSchemesMappingToolInput, GetIssueTypeSchemesMappingToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueTypeSchemesMappingInput(GetIssueTypeSchemesMappingToolInput):
    """Operation input for `get_issue_type_schemes_mapping`."""
    pass

class GetIssueTypeSchemesMappingOutput(GetIssueTypeSchemesMappingToolOutput):
    """Operation output for `get_issue_type_schemes_mapping`."""
    pass

class JiraIssueTypeSchemesMappingResource(BaseResourceClient):
    """Operations for the `issue_type_schemes_mapping` resource."""

    @operation(
        name='get_issue_type_schemes_mapping',
        title='GetIssueTypeSchemesMapping',
        input_model=GetIssueTypeSchemesMappingInput,
        output_model=GetIssueTypeSchemesMappingOutput,
        tools_used=('get_issue_type_schemes_mapping',),
        tags=tuple(['Issue type schemes']),
    )
    async def get(self, data: GetIssueTypeSchemesMappingInput) -> GetIssueTypeSchemesMappingOutput:
        """Returns a [paginated](#pagination) list of issue type scheme items. Only issue type scheme items used in classic projects are returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, issue_type_scheme_id"""
        tool = self._client.get_tool('get_issue_type_schemes_mapping')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueTypeSchemesMappingOutput.model_validate(coerce_tool_result(result))
