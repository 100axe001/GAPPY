from __future__ import annotations

from lemma_connectors.google_drive.generated.tool_types import DriveTeamdrivesCreateToolInput, DriveTeamdrivesCreateToolOutput, DriveTeamdrivesDeleteToolInput, DriveTeamdrivesDeleteToolOutput, DriveTeamdrivesGetToolInput, DriveTeamdrivesGetToolOutput, DriveTeamdrivesListToolInput, DriveTeamdrivesListToolOutput, DriveTeamdrivesUpdateToolInput, DriveTeamdrivesUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class TeamdrivesCreateInput(DriveTeamdrivesCreateToolInput):
    """Operation input for `teamdrives_create`."""
    pass

class TeamdrivesCreateOutput(DriveTeamdrivesCreateToolOutput):
    """Operation output for `teamdrives_create`."""
    pass

class TeamdrivesDeleteInput(DriveTeamdrivesDeleteToolInput):
    """Operation input for `teamdrives_delete`."""
    pass

class TeamdrivesDeleteOutput(DriveTeamdrivesDeleteToolOutput):
    """Operation output for `teamdrives_delete`."""
    pass

class TeamdrivesGetInput(DriveTeamdrivesGetToolInput):
    """Operation input for `teamdrives_get`."""
    pass

class TeamdrivesGetOutput(DriveTeamdrivesGetToolOutput):
    """Operation output for `teamdrives_get`."""
    pass

class TeamdrivesListInput(DriveTeamdrivesListToolInput):
    """Operation input for `teamdrives_list`."""
    pass

class TeamdrivesListOutput(DriveTeamdrivesListToolOutput):
    """Operation output for `teamdrives_list`."""
    pass

class TeamdrivesUpdateInput(DriveTeamdrivesUpdateToolInput):
    """Operation input for `teamdrives_update`."""
    pass

class TeamdrivesUpdateOutput(DriveTeamdrivesUpdateToolOutput):
    """Operation output for `teamdrives_update`."""
    pass

class GoogleDriveTeamdrivesResource(BaseResourceClient):
    """Operations for the `teamdrives` resource."""

    @operation(
        name='teamdrives_create',
        title='TeamdrivesCreate',
        input_model=TeamdrivesCreateInput,
        output_model=TeamdrivesCreateOutput,
        tools_used=('drive_teamdrives_create',),
        tags=tuple(['teamdrives']),
    )
    async def create(self, data: TeamdrivesCreateInput) -> TeamdrivesCreateOutput:
        """Deprecated use drives.create instead.

Important inputs: fields, request_id, body"""
        tool = self._client.get_tool('drive_teamdrives_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return TeamdrivesCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='teamdrives_delete',
        title='TeamdrivesDelete',
        input_model=TeamdrivesDeleteInput,
        output_model=TeamdrivesDeleteOutput,
        tools_used=('drive_teamdrives_delete',),
        tags=tuple(['teamdrives']),
    )
    async def delete(self, data: TeamdrivesDeleteInput) -> TeamdrivesDeleteOutput:
        """Deprecated use drives.delete instead.

Important inputs: fields, team_drive_id"""
        tool = self._client.get_tool('drive_teamdrives_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return TeamdrivesDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='teamdrives_get',
        title='TeamdrivesGet',
        input_model=TeamdrivesGetInput,
        output_model=TeamdrivesGetOutput,
        tools_used=('drive_teamdrives_get',),
        tags=tuple(['teamdrives']),
    )
    async def get(self, data: TeamdrivesGetInput) -> TeamdrivesGetOutput:
        """Deprecated use drives.get instead.

Important inputs: fields, team_drive_id, use_domain_admin_access"""
        tool = self._client.get_tool('drive_teamdrives_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return TeamdrivesGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='teamdrives_list',
        title='TeamdrivesList',
        input_model=TeamdrivesListInput,
        output_model=TeamdrivesListOutput,
        tools_used=('drive_teamdrives_list',),
        tags=tuple(['teamdrives']),
    )
    async def list(self, data: TeamdrivesListInput) -> TeamdrivesListOutput:
        """Deprecated use drives.list instead.

Important inputs: fields, page_size, page_token, q, use_domain_admin_access"""
        tool = self._client.get_tool('drive_teamdrives_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return TeamdrivesListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='teamdrives_update',
        title='TeamdrivesUpdate',
        input_model=TeamdrivesUpdateInput,
        output_model=TeamdrivesUpdateOutput,
        tools_used=('drive_teamdrives_update',),
        tags=tuple(['teamdrives']),
    )
    async def update(self, data: TeamdrivesUpdateInput) -> TeamdrivesUpdateOutput:
        """Deprecated use drives.update instead.

Important inputs: fields, team_drive_id, use_domain_admin_access, body"""
        tool = self._client.get_tool('drive_teamdrives_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return TeamdrivesUpdateOutput.model_validate(coerce_tool_result(result))
