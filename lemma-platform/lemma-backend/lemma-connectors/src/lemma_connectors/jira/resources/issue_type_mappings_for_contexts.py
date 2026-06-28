from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueTypeMappingsForContextsToolInput, GetIssueTypeMappingsForContextsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueTypeMappingsForContextsInput(GetIssueTypeMappingsForContextsToolInput):
    """Operation input for `get_issue_type_mappings_for_contexts`."""
    pass

class GetIssueTypeMappingsForContextsOutput(GetIssueTypeMappingsForContextsToolOutput):
    """Operation output for `get_issue_type_mappings_for_contexts`."""
    pass

class JiraIssueTypeMappingsForContextsResource(BaseResourceClient):
    """Operations for the `issue_type_mappings_for_contexts` resource."""

    @operation(
        name='get_issue_type_mappings_for_contexts',
        title='GetIssueTypeMappingsForContexts',
        input_model=GetIssueTypeMappingsForContextsInput,
        output_model=GetIssueTypeMappingsForContextsOutput,
        tools_used=('get_issue_type_mappings_for_contexts',),
        tags=tuple(['Issue custom field contexts']),
    )
    async def get(self, data: GetIssueTypeMappingsForContextsInput) -> GetIssueTypeMappingsForContextsOutput:
        """Returns a [paginated](#pagination) list of context to issue type mappings for a custom field. Mappings are returned for all contexts or a list of contexts. Mappings are ordered first by context ID and then by issue type ID. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, context_id, start_at, max_results"""
        tool = self._client.get_tool('get_issue_type_mappings_for_contexts')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueTypeMappingsForContextsOutput.model_validate(coerce_tool_result(result))
