from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteDashboardItemPropertyToolInput, DeleteDashboardItemPropertyToolOutput, GetDashboardItemPropertyToolInput, GetDashboardItemPropertyToolOutput, SetDashboardItemPropertyToolInput, SetDashboardItemPropertyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteDashboardItemPropertyInput(DeleteDashboardItemPropertyToolInput):
    """Operation input for `delete_dashboard_item_property`."""
    pass

class DeleteDashboardItemPropertyOutput(DeleteDashboardItemPropertyToolOutput):
    """Operation output for `delete_dashboard_item_property`."""
    pass

class GetDashboardItemPropertyInput(GetDashboardItemPropertyToolInput):
    """Operation input for `get_dashboard_item_property`."""
    pass

class GetDashboardItemPropertyOutput(GetDashboardItemPropertyToolOutput):
    """Operation output for `get_dashboard_item_property`."""
    pass

class SetDashboardItemPropertyInput(SetDashboardItemPropertyToolInput):
    """Operation input for `set_dashboard_item_property`."""
    pass

class SetDashboardItemPropertyOutput(SetDashboardItemPropertyToolOutput):
    """Operation output for `set_dashboard_item_property`."""
    pass

class JiraDashboardItemPropertyResource(BaseResourceClient):
    """Operations for the `dashboard_item_property` resource."""

    @operation(
        name='delete_dashboard_item_property',
        title='DeleteDashboardItemProperty',
        input_model=DeleteDashboardItemPropertyInput,
        output_model=DeleteDashboardItemPropertyOutput,
        tools_used=('delete_dashboard_item_property',),
        tags=tuple(['Dashboards']),
    )
    async def delete(self, data: DeleteDashboardItemPropertyInput) -> DeleteDashboardItemPropertyOutput:
        """Deletes a dashboard item property. This operation can be accessed anonymously. **[Permissions](#permissions) required:** The user must be the owner of the dashboard. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard.

Important inputs: dashboard_id, item_id, property_key"""
        tool = self._client.get_tool('delete_dashboard_item_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteDashboardItemPropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_dashboard_item_property',
        title='GetDashboardItemProperty',
        input_model=GetDashboardItemPropertyInput,
        output_model=GetDashboardItemPropertyOutput,
        tools_used=('get_dashboard_item_property',),
        tags=tuple(['Dashboards']),
    )
    async def get(self, data: GetDashboardItemPropertyInput) -> GetDashboardItemPropertyOutput:
        """Returns the key and value of a dashboard item property. A dashboard item enables an app to add user-specific information to a user dashboard. Dashboard items are exposed to users as gadgets that users can add to their dashboards. For more information on how users do this, see [Adding and customizing gadgets](https://confluence.atlassian.com/x/7AeiLQ). When an app creates a dashboard item it registers a callback to receive the dashboard item ID. The callback fires whenever the item is rendered or, where the item is configurable, the user edits the item. The app then uses this resource to store the item's content or configuration details. For more information on working with dashboard items, see [ Building a dashboard item for a JIRA Connect add-on](https://developer.atlassian.com/server/jira/platform/guide-building-a-dashboard-item-for-a-jira-connect-add-on-33746254/) and the [Dashboard Item](https://developer.atlassian.com/cloud/jira/platform/modules/dashboard-item/) documentation. There is no resource to set or get dashboard items. This operation can be accessed anonymously. **[Permissions](#permissions) required:** The user must be the owner of the dashboard or have the dashboard shared with them. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard. The System dashboard is considered to be shared with all other users, and is accessible to anonymous users when Jira’s anonymous access is permitted.

Important inputs: dashboard_id, item_id, property_key"""
        tool = self._client.get_tool('get_dashboard_item_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetDashboardItemPropertyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_dashboard_item_property',
        title='SetDashboardItemProperty',
        input_model=SetDashboardItemPropertyInput,
        output_model=SetDashboardItemPropertyOutput,
        tools_used=('set_dashboard_item_property',),
        tags=tuple(['Dashboards']),
    )
    async def set(self, data: SetDashboardItemPropertyInput) -> SetDashboardItemPropertyOutput:
        """Sets the value of a dashboard item property. Use this resource in apps to store custom data against a dashboard item. A dashboard item enables an app to add user-specific information to a user dashboard. Dashboard items are exposed to users as gadgets that users can add to their dashboards. For more information on how users do this, see [Adding and customizing gadgets](https://confluence.atlassian.com/x/7AeiLQ). When an app creates a dashboard item it registers a callback to receive the dashboard item ID. The callback fires whenever the item is rendered or, where the item is configurable, the user edits the item. The app then uses this resource to store the item's content or configuration details. For more information on working with dashboard items, see [ Building a dashboard item for a JIRA Connect add-on](https://developer.atlassian.com/server/jira/platform/guide-building-a-dashboard-item-for-a-jira-connect-add-on-33746254/) and the [Dashboard Item](https://developer.atlassian.com/cloud/jira/platform/modules/dashboard-item/) documentation. There is no resource to set or get dashboard items. The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON blob. The maximum length is 32768 characters. This operation can be accessed anonymously. **[Permissions](#permissions) required:** The user must be the owner of the dashboard. Note, users with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System dashboard.

Important inputs: dashboard_id, item_id, property_key, body"""
        tool = self._client.get_tool('set_dashboard_item_property')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetDashboardItemPropertyOutput.model_validate(coerce_tool_result(result))
