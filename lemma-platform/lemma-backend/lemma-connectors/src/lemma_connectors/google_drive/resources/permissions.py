from __future__ import annotations

from lemma_connectors.google_drive.generated.tool_types import DrivePermissionsCreateToolInput, DrivePermissionsCreateToolOutput, DrivePermissionsDeleteToolInput, DrivePermissionsDeleteToolOutput, DrivePermissionsGetToolInput, DrivePermissionsGetToolOutput, DrivePermissionsListToolInput, DrivePermissionsListToolOutput, DrivePermissionsUpdateToolInput, DrivePermissionsUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class PermissionsCreateInput(DrivePermissionsCreateToolInput):
    """Operation input for `permissions_create`."""
    pass

class PermissionsCreateOutput(DrivePermissionsCreateToolOutput):
    """Operation output for `permissions_create`."""
    pass

class PermissionsDeleteInput(DrivePermissionsDeleteToolInput):
    """Operation input for `permissions_delete`."""
    pass

class PermissionsDeleteOutput(DrivePermissionsDeleteToolOutput):
    """Operation output for `permissions_delete`."""
    pass

class PermissionsGetInput(DrivePermissionsGetToolInput):
    """Operation input for `permissions_get`."""
    pass

class PermissionsGetOutput(DrivePermissionsGetToolOutput):
    """Operation output for `permissions_get`."""
    pass

class PermissionsListInput(DrivePermissionsListToolInput):
    """Operation input for `permissions_list`."""
    pass

class PermissionsListOutput(DrivePermissionsListToolOutput):
    """Operation output for `permissions_list`."""
    pass

class PermissionsUpdateInput(DrivePermissionsUpdateToolInput):
    """Operation input for `permissions_update`."""
    pass

class PermissionsUpdateOutput(DrivePermissionsUpdateToolOutput):
    """Operation output for `permissions_update`."""
    pass

class GoogleDrivePermissionsResource(BaseResourceClient):
    """Operations for the `permissions` resource."""

    @operation(
        name='permissions_create',
        title='PermissionsCreate',
        input_model=PermissionsCreateInput,
        output_model=PermissionsCreateOutput,
        tools_used=('drive_permissions_create',),
        tags=tuple(['permissions']),
    )
    async def create(self, data: PermissionsCreateInput) -> PermissionsCreateOutput:
        """Creates a permission for a file or shared drive. For more information on creating permissions, see Share files, folders & drives.

Important inputs: fields, file_id, email_message, enforce_single_parent, move_to_new_owners_root, send_notification_email, supports_all_drives, supports_team_drives, transfer_ownership, use_domain_admin_access, body"""
        tool = self._client.get_tool('drive_permissions_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return PermissionsCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='permissions_delete',
        title='PermissionsDelete',
        input_model=PermissionsDeleteInput,
        output_model=PermissionsDeleteOutput,
        tools_used=('drive_permissions_delete',),
        tags=tuple(['permissions']),
    )
    async def delete(self, data: PermissionsDeleteInput) -> PermissionsDeleteOutput:
        """Deletes a permission.

Important inputs: fields, file_id, permission_id, supports_all_drives, supports_team_drives, use_domain_admin_access"""
        tool = self._client.get_tool('drive_permissions_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return PermissionsDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='permissions_get',
        title='PermissionsGet',
        input_model=PermissionsGetInput,
        output_model=PermissionsGetOutput,
        tools_used=('drive_permissions_get',),
        tags=tuple(['permissions']),
    )
    async def get(self, data: PermissionsGetInput) -> PermissionsGetOutput:
        """Gets a permission by ID.

Important inputs: fields, file_id, permission_id, supports_all_drives, supports_team_drives, use_domain_admin_access"""
        tool = self._client.get_tool('drive_permissions_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return PermissionsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='permissions_list',
        title='PermissionsList',
        input_model=PermissionsListInput,
        output_model=PermissionsListOutput,
        tools_used=('drive_permissions_list',),
        tags=tuple(['permissions']),
    )
    async def list(self, data: PermissionsListInput) -> PermissionsListOutput:
        """Lists a file's or shared drive's permissions.

Important inputs: fields, file_id, include_permissions_for_view, page_size, page_token, supports_all_drives, supports_team_drives, use_domain_admin_access"""
        tool = self._client.get_tool('drive_permissions_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return PermissionsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='permissions_update',
        title='PermissionsUpdate',
        input_model=PermissionsUpdateInput,
        output_model=PermissionsUpdateOutput,
        tools_used=('drive_permissions_update',),
        tags=tuple(['permissions']),
    )
    async def update(self, data: PermissionsUpdateInput) -> PermissionsUpdateOutput:
        """Updates a permission with patch semantics.

Important inputs: fields, file_id, permission_id, remove_expiration, supports_all_drives, supports_team_drives, transfer_ownership, use_domain_admin_access, body"""
        tool = self._client.get_tool('drive_permissions_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return PermissionsUpdateOutput.model_validate(coerce_tool_result(result))
