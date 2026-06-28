from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllAvailableDashboardGadgetsToolInput, GetAllAvailableDashboardGadgetsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllAvailableDashboardGadgetsInput(GetAllAvailableDashboardGadgetsToolInput):
    """Operation input for `get_all_available_dashboard_gadgets`."""
    pass

class GetAllAvailableDashboardGadgetsOutput(GetAllAvailableDashboardGadgetsToolOutput):
    """Operation output for `get_all_available_dashboard_gadgets`."""
    pass

class JiraAllAvailableDashboardGadgetsResource(BaseResourceClient):
    """Operations for the `all_available_dashboard_gadgets` resource."""

    @operation(
        name='get_all_available_dashboard_gadgets',
        title='GetAllAvailableDashboardGadgets',
        input_model=GetAllAvailableDashboardGadgetsInput,
        output_model=GetAllAvailableDashboardGadgetsOutput,
        tools_used=('get_all_available_dashboard_gadgets',),
        tags=tuple(['Dashboards']),
    )
    async def get(self, data: GetAllAvailableDashboardGadgetsInput) -> GetAllAvailableDashboardGadgetsOutput:
        """Gets a list of all available gadgets that can be added to all dashboards. **[Permissions](#permissions) required:** None.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_all_available_dashboard_gadgets')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllAvailableDashboardGadgetsOutput.model_validate(coerce_tool_result(result))
