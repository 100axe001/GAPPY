from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import AppsPermissionsUsersListToolInput, AppsPermissionsUsersListToolOutput, AppsPermissionsUsersRequestToolInput, AppsPermissionsUsersRequestToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AppsPermissionsUsersListInput(AppsPermissionsUsersListToolInput):
    """Operation input for `apps_permissions_users_list`."""
    pass

class AppsPermissionsUsersListOutput(AppsPermissionsUsersListToolOutput):
    """Operation output for `apps_permissions_users_list`."""
    pass

class AppsPermissionsUsersRequestInput(AppsPermissionsUsersRequestToolInput):
    """Operation input for `apps_permissions_users_request`."""
    pass

class AppsPermissionsUsersRequestOutput(AppsPermissionsUsersRequestToolOutput):
    """Operation output for `apps_permissions_users_request`."""
    pass

class SlackAppsPermissionsUsersResource(BaseResourceClient):
    """Operations for the `apps_permissions_users` resource."""

    @operation(
        name='apps_permissions_users_list',
        title='AppsPermissionsUsersList',
        input_model=AppsPermissionsUsersListInput,
        output_model=AppsPermissionsUsersListOutput,
        tools_used=('apps_permissions_users_list',),
        tags=tuple(['apps.permissions.users', 'apps']),
    )
    async def list(self, data: AppsPermissionsUsersListInput) -> AppsPermissionsUsersListOutput:
        """Returns list of user grants and corresponding scopes this app has on a team.

Important inputs: token, cursor, limit"""
        tool = self._client.get_tool('apps_permissions_users_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AppsPermissionsUsersListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='apps_permissions_users_request',
        title='AppsPermissionsUsersRequest',
        input_model=AppsPermissionsUsersRequestInput,
        output_model=AppsPermissionsUsersRequestOutput,
        tools_used=('apps_permissions_users_request',),
        tags=tuple(['apps.permissions.users', 'apps']),
    )
    async def request(self, data: AppsPermissionsUsersRequestInput) -> AppsPermissionsUsersRequestOutput:
        """Enables an app to trigger a permissions modal to grant an app access to a user access scope.

Important inputs: token, scopes, trigger_id, user"""
        tool = self._client.get_tool('apps_permissions_users_request')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AppsPermissionsUsersRequestOutput.model_validate(coerce_tool_result(result))
