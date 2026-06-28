from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllDashboardsToolInput, GetAllDashboardsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllDashboardsInput(GetAllDashboardsToolInput):
    """Operation input for `get_all_dashboards`."""
    pass

class GetAllDashboardsOutput(GetAllDashboardsToolOutput):
    """Operation output for `get_all_dashboards`."""
    pass

class JiraAllDashboardsResource(BaseResourceClient):
    """Operations for the `all_dashboards` resource."""

    @operation(
        name='get_all_dashboards',
        title='GetAllDashboards',
        input_model=GetAllDashboardsInput,
        output_model=GetAllDashboardsOutput,
        tools_used=('get_all_dashboards',),
        tags=tuple(['Dashboards']),
    )
    async def get(self, data: GetAllDashboardsInput) -> GetAllDashboardsOutput:
        """Returns a list of dashboards owned by or shared with the user. The list may be filtered to include only favorite or owned dashboards. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: filter, start_at, max_results"""
        tool = self._client.get_tool('get_all_dashboards')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllDashboardsOutput.model_validate(coerce_tool_result(result))
