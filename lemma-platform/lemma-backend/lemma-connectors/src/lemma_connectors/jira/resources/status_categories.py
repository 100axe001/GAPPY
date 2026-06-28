from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetStatusCategoriesToolInput, GetStatusCategoriesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetStatusCategoriesInput(GetStatusCategoriesToolInput):
    """Operation input for `get_status_categories`."""
    pass

class GetStatusCategoriesOutput(GetStatusCategoriesToolOutput):
    """Operation output for `get_status_categories`."""
    pass

class JiraStatusCategoriesResource(BaseResourceClient):
    """Operations for the `status_categories` resource."""

    @operation(
        name='get_status_categories',
        title='GetStatusCategories',
        input_model=GetStatusCategoriesInput,
        output_model=GetStatusCategoriesOutput,
        tools_used=('get_status_categories',),
        tags=tuple(['Workflow status categories']),
    )
    async def get(self, data: GetStatusCategoriesInput) -> GetStatusCategoriesOutput:
        """Returns a list of all status categories. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_status_categories')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetStatusCategoriesOutput.model_validate(coerce_tool_result(result))
