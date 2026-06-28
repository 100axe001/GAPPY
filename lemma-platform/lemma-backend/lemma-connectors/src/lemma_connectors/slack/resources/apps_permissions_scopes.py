from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import AppsPermissionsScopesListToolInput, AppsPermissionsScopesListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AppsPermissionsScopesListInput(AppsPermissionsScopesListToolInput):
    """Operation input for `apps_permissions_scopes_list`."""
    pass

class AppsPermissionsScopesListOutput(AppsPermissionsScopesListToolOutput):
    """Operation output for `apps_permissions_scopes_list`."""
    pass

class SlackAppsPermissionsScopesResource(BaseResourceClient):
    """Operations for the `apps_permissions_scopes` resource."""

    @operation(
        name='apps_permissions_scopes_list',
        title='AppsPermissionsScopesList',
        input_model=AppsPermissionsScopesListInput,
        output_model=AppsPermissionsScopesListOutput,
        tools_used=('apps_permissions_scopes_list',),
        tags=tuple(['apps.permissions.scopes', 'apps']),
    )
    async def list(self, data: AppsPermissionsScopesListInput) -> AppsPermissionsScopesListOutput:
        """Returns list of scopes this app has on a team.

Important inputs: token"""
        tool = self._client.get_tool('apps_permissions_scopes_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AppsPermissionsScopesListOutput.model_validate(coerce_tool_result(result))
