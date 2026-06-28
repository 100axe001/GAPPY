from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import AppsPermissionsResourcesListToolInput, AppsPermissionsResourcesListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AppsPermissionsResourcesListInput(AppsPermissionsResourcesListToolInput):
    """Operation input for `apps_permissions_resources_list`."""
    pass

class AppsPermissionsResourcesListOutput(AppsPermissionsResourcesListToolOutput):
    """Operation output for `apps_permissions_resources_list`."""
    pass

class SlackAppsPermissionsResourcesResource(BaseResourceClient):
    """Operations for the `apps_permissions_resources` resource."""

    @operation(
        name='apps_permissions_resources_list',
        title='AppsPermissionsResourcesList',
        input_model=AppsPermissionsResourcesListInput,
        output_model=AppsPermissionsResourcesListOutput,
        tools_used=('apps_permissions_resources_list',),
        tags=tuple(['apps.permissions.resources', 'apps']),
    )
    async def list(self, data: AppsPermissionsResourcesListInput) -> AppsPermissionsResourcesListOutput:
        """Returns list of resource grants this app has on a team.

Important inputs: token, cursor, limit"""
        tool = self._client.get_tool('apps_permissions_resources_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AppsPermissionsResourcesListOutput.model_validate(coerce_tool_result(result))
