from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetProjectCategoryByIdToolInput, GetProjectCategoryByIdToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProjectCategoryByIdInput(GetProjectCategoryByIdToolInput):
    """Operation input for `get_project_category_by_id`."""
    pass

class GetProjectCategoryByIdOutput(GetProjectCategoryByIdToolOutput):
    """Operation output for `get_project_category_by_id`."""
    pass

class JiraProjectCategoryByIdResource(BaseResourceClient):
    """Operations for the `project_category_by_id` resource."""

    @operation(
        name='get_project_category_by_id',
        title='GetProjectCategoryById',
        input_model=GetProjectCategoryByIdInput,
        output_model=GetProjectCategoryByIdOutput,
        tools_used=('get_project_category_by_id',),
        tags=tuple(['Project categories']),
    )
    async def get(self, data: GetProjectCategoryByIdInput) -> GetProjectCategoryByIdOutput:
        """Returns a project category. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: id"""
        tool = self._client.get_tool('get_project_category_by_id')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectCategoryByIdOutput.model_validate(coerce_tool_result(result))
