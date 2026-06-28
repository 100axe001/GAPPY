from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllProjectCategoriesToolInput, GetAllProjectCategoriesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllProjectCategoriesInput(GetAllProjectCategoriesToolInput):
    """Operation input for `get_all_project_categories`."""
    pass

class GetAllProjectCategoriesOutput(GetAllProjectCategoriesToolOutput):
    """Operation output for `get_all_project_categories`."""
    pass

class JiraAllProjectCategoriesResource(BaseResourceClient):
    """Operations for the `all_project_categories` resource."""

    @operation(
        name='get_all_project_categories',
        title='GetAllProjectCategories',
        input_model=GetAllProjectCategoriesInput,
        output_model=GetAllProjectCategoriesOutput,
        tools_used=('get_all_project_categories',),
        tags=tuple(['Project categories']),
    )
    async def get(self, data: GetAllProjectCategoriesInput) -> GetAllProjectCategoriesOutput:
        """Returns all project categories. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_all_project_categories')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllProjectCategoriesOutput.model_validate(coerce_tool_result(result))
