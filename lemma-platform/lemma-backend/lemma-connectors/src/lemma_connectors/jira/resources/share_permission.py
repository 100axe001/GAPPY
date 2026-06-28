from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddSharePermissionToolInput, AddSharePermissionToolOutput, DeleteSharePermissionToolInput, DeleteSharePermissionToolOutput, GetSharePermissionToolInput, GetSharePermissionToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddSharePermissionInput(AddSharePermissionToolInput):
    """Operation input for `add_share_permission`."""
    pass

class AddSharePermissionOutput(AddSharePermissionToolOutput):
    """Operation output for `add_share_permission`."""
    pass

class DeleteSharePermissionInput(DeleteSharePermissionToolInput):
    """Operation input for `delete_share_permission`."""
    pass

class DeleteSharePermissionOutput(DeleteSharePermissionToolOutput):
    """Operation output for `delete_share_permission`."""
    pass

class GetSharePermissionInput(GetSharePermissionToolInput):
    """Operation input for `get_share_permission`."""
    pass

class GetSharePermissionOutput(GetSharePermissionToolOutput):
    """Operation output for `get_share_permission`."""
    pass

class JiraSharePermissionResource(BaseResourceClient):
    """Operations for the `share_permission` resource."""

    @operation(
        name='add_share_permission',
        title='AddSharePermission',
        input_model=AddSharePermissionInput,
        output_model=AddSharePermissionOutput,
        tools_used=('add_share_permission',),
        tags=tuple(['Filter sharing']),
    )
    async def add(self, data: AddSharePermissionInput) -> AddSharePermissionOutput:
        """Add a share permissions to a filter. If you add a global share permission (one for all logged-in users or the public) it will overwrite all share permissions for the filter. Be aware that this operation uses different objects for updating share permissions compared to [Update filter](#api-rest-api-3-filter-id-put). **[Permissions](#permissions) required:** *Share dashboards and filters* [global permission](https://confluence.atlassian.com/x/x4dKLg) and the user must own the filter.

Important inputs: id, body"""
        tool = self._client.get_tool('add_share_permission')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddSharePermissionOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_share_permission',
        title='DeleteSharePermission',
        input_model=DeleteSharePermissionInput,
        output_model=DeleteSharePermissionOutput,
        tools_used=('delete_share_permission',),
        tags=tuple(['Filter sharing']),
    )
    async def delete(self, data: DeleteSharePermissionInput) -> DeleteSharePermissionOutput:
        """Deletes a share permission from a filter. **[Permissions](#permissions) required:** Permission to access Jira and the user must own the filter.

Important inputs: id, permission_id"""
        tool = self._client.get_tool('delete_share_permission')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteSharePermissionOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_share_permission',
        title='GetSharePermission',
        input_model=GetSharePermissionInput,
        output_model=GetSharePermissionOutput,
        tools_used=('get_share_permission',),
        tags=tuple(['Filter sharing']),
    )
    async def get(self, data: GetSharePermissionInput) -> GetSharePermissionOutput:
        """Returns a share permission for a filter. A filter can be shared with groups, projects, all logged-in users, or the public. Sharing with all logged-in users or the public is known as a global share permission. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None, however, a share permission is only returned for: * filters owned by the user. * filters shared with a group that the user is a member of. * filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for. * filters shared with a public project. * filters shared with the public.

Important inputs: id, permission_id"""
        tool = self._client.get_tool('get_share_permission')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetSharePermissionOutput.model_validate(coerce_tool_result(result))
