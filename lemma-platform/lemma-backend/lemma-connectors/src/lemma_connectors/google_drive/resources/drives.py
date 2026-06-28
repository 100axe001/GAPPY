from __future__ import annotations

from lemma_connectors.google_drive.generated.tool_types import DriveDrivesCreateToolInput, DriveDrivesCreateToolOutput, DriveDrivesDeleteToolInput, DriveDrivesDeleteToolOutput, DriveDrivesGetToolInput, DriveDrivesGetToolOutput, DriveDrivesHideToolInput, DriveDrivesHideToolOutput, DriveDrivesListToolInput, DriveDrivesListToolOutput, DriveDrivesUnhideToolInput, DriveDrivesUnhideToolOutput, DriveDrivesUpdateToolInput, DriveDrivesUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DrivesCreateInput(DriveDrivesCreateToolInput):
    """Operation input for `drives_create`."""
    pass

class DrivesCreateOutput(DriveDrivesCreateToolOutput):
    """Operation output for `drives_create`."""
    pass

class DrivesDeleteInput(DriveDrivesDeleteToolInput):
    """Operation input for `drives_delete`."""
    pass

class DrivesDeleteOutput(DriveDrivesDeleteToolOutput):
    """Operation output for `drives_delete`."""
    pass

class DrivesGetInput(DriveDrivesGetToolInput):
    """Operation input for `drives_get`."""
    pass

class DrivesGetOutput(DriveDrivesGetToolOutput):
    """Operation output for `drives_get`."""
    pass

class DrivesHideInput(DriveDrivesHideToolInput):
    """Operation input for `drives_hide`."""
    pass

class DrivesHideOutput(DriveDrivesHideToolOutput):
    """Operation output for `drives_hide`."""
    pass

class DrivesListInput(DriveDrivesListToolInput):
    """Operation input for `drives_list`."""
    pass

class DrivesListOutput(DriveDrivesListToolOutput):
    """Operation output for `drives_list`."""
    pass

class DrivesUnhideInput(DriveDrivesUnhideToolInput):
    """Operation input for `drives_unhide`."""
    pass

class DrivesUnhideOutput(DriveDrivesUnhideToolOutput):
    """Operation output for `drives_unhide`."""
    pass

class DrivesUpdateInput(DriveDrivesUpdateToolInput):
    """Operation input for `drives_update`."""
    pass

class DrivesUpdateOutput(DriveDrivesUpdateToolOutput):
    """Operation output for `drives_update`."""
    pass

class GoogleDriveDrivesResource(BaseResourceClient):
    """Operations for the `drives` resource."""

    @operation(
        name='drives_create',
        title='DrivesCreate',
        input_model=DrivesCreateInput,
        output_model=DrivesCreateOutput,
        tools_used=('drive_drives_create',),
        tags=tuple(['drives']),
    )
    async def create(self, data: DrivesCreateInput) -> DrivesCreateOutput:
        """Creates a shared drive.

Important inputs: fields, request_id, body"""
        tool = self._client.get_tool('drive_drives_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DrivesCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='drives_delete',
        title='DrivesDelete',
        input_model=DrivesDeleteInput,
        output_model=DrivesDeleteOutput,
        tools_used=('drive_drives_delete',),
        tags=tuple(['drives']),
    )
    async def delete(self, data: DrivesDeleteInput) -> DrivesDeleteOutput:
        """Permanently deletes a shared drive for which the user is an organizer. The shared drive cannot contain any untrashed items.

Important inputs: fields, drive_id, allow_item_deletion, use_domain_admin_access"""
        tool = self._client.get_tool('drive_drives_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DrivesDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='drives_get',
        title='DrivesGet',
        input_model=DrivesGetInput,
        output_model=DrivesGetOutput,
        tools_used=('drive_drives_get',),
        tags=tuple(['drives']),
    )
    async def get(self, data: DrivesGetInput) -> DrivesGetOutput:
        """Gets a shared drive's metadata by ID.

Important inputs: fields, drive_id, use_domain_admin_access"""
        tool = self._client.get_tool('drive_drives_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DrivesGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='drives_hide',
        title='DrivesHide',
        input_model=DrivesHideInput,
        output_model=DrivesHideOutput,
        tools_used=('drive_drives_hide',),
        tags=tuple(['drives']),
    )
    async def hide(self, data: DrivesHideInput) -> DrivesHideOutput:
        """Hides a shared drive from the default view.

Important inputs: fields, drive_id"""
        tool = self._client.get_tool('drive_drives_hide')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DrivesHideOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='drives_list',
        title='DrivesList',
        input_model=DrivesListInput,
        output_model=DrivesListOutput,
        tools_used=('drive_drives_list',),
        tags=tuple(['drives']),
    )
    async def list(self, data: DrivesListInput) -> DrivesListOutput:
        """Lists the user's shared drives.

Important inputs: fields, page_size, page_token, q, use_domain_admin_access"""
        tool = self._client.get_tool('drive_drives_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DrivesListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='drives_unhide',
        title='DrivesUnhide',
        input_model=DrivesUnhideInput,
        output_model=DrivesUnhideOutput,
        tools_used=('drive_drives_unhide',),
        tags=tuple(['drives']),
    )
    async def unhide(self, data: DrivesUnhideInput) -> DrivesUnhideOutput:
        """Restores a shared drive to the default view.

Important inputs: fields, drive_id"""
        tool = self._client.get_tool('drive_drives_unhide')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DrivesUnhideOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='drives_update',
        title='DrivesUpdate',
        input_model=DrivesUpdateInput,
        output_model=DrivesUpdateOutput,
        tools_used=('drive_drives_update',),
        tags=tuple(['drives']),
    )
    async def update(self, data: DrivesUpdateInput) -> DrivesUpdateOutput:
        """Updates the metadata for a shared drive.

Important inputs: fields, drive_id, use_domain_admin_access, body"""
        tool = self._client.get_tool('drive_drives_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DrivesUpdateOutput.model_validate(coerce_tool_result(result))
