from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetDashboardItemPropertyKeysToolInput, GetDashboardItemPropertyKeysToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetDashboardItemPropertyKeysInput(GetDashboardItemPropertyKeysToolInput):
    """Operation input for `get_dashboard_item_property_keys`."""
    pass

class GetDashboardItemPropertyKeysOutput(GetDashboardItemPropertyKeysToolOutput):
    """Operation output for `get_dashboard_item_property_keys`."""
    pass

class JiraDashboardItemPropertyKeysResource(BaseResourceClient):
    """Operations for the `dashboard_item_property_keys` resource."""

    @operation(
        name='get_dashboard_item_property_keys',
        title='GetDashboardItemPropertyKeys',
        input_model=GetDashboardItemPropertyKeysInput,
        output_model=GetDashboardItemPropertyKeysOutput,
        tools_used=('get_dashboard_item_property_keys',),
        tags=tuple(['Dashboards']),
    )
    async def get(self, data: GetDashboardItemPropertyKeysInput) -> GetDashboardItemPropertyKeysOutput:
        """Returns the keys of all properties for a dashboard item. This operation can be accessed anonymously. **[Permissions](#permissions) required:** The user must be the owner of the dashboard or have the dashboard shared with them. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard. The System dashboard is considered to be shared with all other users, and is accessible to anonymous users when Jira’s anonymous access is permitted.

Important inputs: dashboard_id, item_id"""
        tool = self._client.get_tool('get_dashboard_item_property_keys')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetDashboardItemPropertyKeysOutput.model_validate(coerce_tool_result(result))
