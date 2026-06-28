from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetStatusCategoryToolInput, GetStatusCategoryToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetStatusCategoryInput(GetStatusCategoryToolInput):
    """Operation input for `get_status_category`."""
    pass

class GetStatusCategoryOutput(GetStatusCategoryToolOutput):
    """Operation output for `get_status_category`."""
    pass

class JiraStatusCategoryResource(BaseResourceClient):
    """Operations for the `status_category` resource."""

    @operation(
        name='get_status_category',
        title='GetStatusCategory',
        input_model=GetStatusCategoryInput,
        output_model=GetStatusCategoryOutput,
        tools_used=('get_status_category',),
        tags=tuple(['Workflow status categories']),
    )
    async def get(self, data: GetStatusCategoryInput) -> GetStatusCategoryOutput:
        """Returns a status category. Status categories provided a mechanism for categorizing [statuses](#api-rest-api-3-status-idOrName-get). **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: id_or_key"""
        tool = self._client.get_tool('get_status_category')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetStatusCategoryOutput.model_validate(coerce_tool_result(result))
