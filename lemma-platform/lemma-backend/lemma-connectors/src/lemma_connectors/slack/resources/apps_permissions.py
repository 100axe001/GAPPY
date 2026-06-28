from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import AppsPermissionsInfoToolInput, AppsPermissionsInfoToolOutput, AppsPermissionsRequestToolInput, AppsPermissionsRequestToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AppsPermissionsInfoInput(AppsPermissionsInfoToolInput):
    """Operation input for `apps_permissions_info`."""
    pass

class AppsPermissionsInfoOutput(AppsPermissionsInfoToolOutput):
    """Operation output for `apps_permissions_info`."""
    pass

class AppsPermissionsRequestInput(AppsPermissionsRequestToolInput):
    """Operation input for `apps_permissions_request`."""
    pass

class AppsPermissionsRequestOutput(AppsPermissionsRequestToolOutput):
    """Operation output for `apps_permissions_request`."""
    pass

class SlackAppsPermissionsResource(BaseResourceClient):
    """Operations for the `apps_permissions` resource."""

    @operation(
        name='apps_permissions_info',
        title='AppsPermissionsInfo',
        input_model=AppsPermissionsInfoInput,
        output_model=AppsPermissionsInfoOutput,
        tools_used=('apps_permissions_info',),
        tags=tuple(['apps.permissions', 'apps']),
    )
    async def info(self, data: AppsPermissionsInfoInput) -> AppsPermissionsInfoOutput:
        """Returns list of permissions this app has on a team.

Important inputs: token"""
        tool = self._client.get_tool('apps_permissions_info')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AppsPermissionsInfoOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='apps_permissions_request',
        title='AppsPermissionsRequest',
        input_model=AppsPermissionsRequestInput,
        output_model=AppsPermissionsRequestOutput,
        tools_used=('apps_permissions_request',),
        tags=tuple(['apps.permissions', 'apps']),
    )
    async def request(self, data: AppsPermissionsRequestInput) -> AppsPermissionsRequestOutput:
        """Allows an app to request additional scopes.

Important inputs: token, scopes, trigger_id"""
        tool = self._client.get_tool('apps_permissions_request')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AppsPermissionsRequestOutput.model_validate(coerce_tool_result(result))
