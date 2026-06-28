from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetProjectContextMappingToolInput, GetProjectContextMappingToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProjectContextMappingInput(GetProjectContextMappingToolInput):
    """Operation input for `get_project_context_mapping`."""
    pass

class GetProjectContextMappingOutput(GetProjectContextMappingToolOutput):
    """Operation output for `get_project_context_mapping`."""
    pass

class JiraProjectContextMappingResource(BaseResourceClient):
    """Operations for the `project_context_mapping` resource."""

    @operation(
        name='get_project_context_mapping',
        title='GetProjectContextMapping',
        input_model=GetProjectContextMappingInput,
        output_model=GetProjectContextMappingOutput,
        tools_used=('get_project_context_mapping',),
        tags=tuple(['Issue custom field contexts']),
    )
    async def get(self, data: GetProjectContextMappingInput) -> GetProjectContextMappingOutput:
        """Returns a [paginated](#pagination) list of context to project mappings for a custom field. The result can be filtered by `contextId`. Otherwise, all mappings are returned. Invalid IDs are ignored. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, context_id, start_at, max_results"""
        tool = self._client.get_tool('get_project_context_mapping')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectContextMappingOutput.model_validate(coerce_tool_result(result))
