from __future__ import annotations

from lemma_connectors.google_drive.generated.tool_types import DriveChangesGetStartPageTokenToolInput, DriveChangesGetStartPageTokenToolOutput, DriveChangesListToolInput, DriveChangesListToolOutput, DriveChangesWatchToolInput, DriveChangesWatchToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ChangesGetStartPageTokenInput(DriveChangesGetStartPageTokenToolInput):
    """Operation input for `changes_get_start_page_token`."""
    pass

class ChangesGetStartPageTokenOutput(DriveChangesGetStartPageTokenToolOutput):
    """Operation output for `changes_get_start_page_token`."""
    pass

class ChangesListInput(DriveChangesListToolInput):
    """Operation input for `changes_list`."""
    pass

class ChangesListOutput(DriveChangesListToolOutput):
    """Operation output for `changes_list`."""
    pass

class ChangesWatchInput(DriveChangesWatchToolInput):
    """Operation input for `changes_watch`."""
    pass

class ChangesWatchOutput(DriveChangesWatchToolOutput):
    """Operation output for `changes_watch`."""
    pass

class GoogleDriveChangesResource(BaseResourceClient):
    """Operations for the `changes` resource."""

    @operation(
        name='changes_get_start_page_token',
        title='ChangesGetStartPageToken',
        input_model=ChangesGetStartPageTokenInput,
        output_model=ChangesGetStartPageTokenOutput,
        tools_used=('drive_changes_get_start_page_token',),
        tags=tuple(['changes']),
    )
    async def get_start_page_token(self, data: ChangesGetStartPageTokenInput) -> ChangesGetStartPageTokenOutput:
        """Gets the starting pageToken for listing future changes.

Important inputs: fields, drive_id, supports_all_drives, supports_team_drives, team_drive_id"""
        tool = self._client.get_tool('drive_changes_get_start_page_token')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ChangesGetStartPageTokenOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='changes_list',
        title='ChangesList',
        input_model=ChangesListInput,
        output_model=ChangesListOutput,
        tools_used=('drive_changes_list',),
        tags=tuple(['changes']),
    )
    async def list(self, data: ChangesListInput) -> ChangesListOutput:
        """Lists the changes for a user or shared drive.

Important inputs: fields, page_token, drive_id, include_corpus_removals, include_items_from_all_drives, include_labels, include_permissions_for_view, include_removed, include_team_drive_items, page_size, restrict_to_my_drive, spaces, supports_all_drives, supports_team_drives, team_drive_id"""
        tool = self._client.get_tool('drive_changes_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ChangesListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='changes_watch',
        title='ChangesWatch',
        input_model=ChangesWatchInput,
        output_model=ChangesWatchOutput,
        tools_used=('drive_changes_watch',),
        tags=tuple(['changes']),
    )
    async def watch(self, data: ChangesWatchInput) -> ChangesWatchOutput:
        """Subscribes to changes for a user. To use this method, you must include the pageToken query parameter.

Important inputs: fields, page_token, drive_id, include_corpus_removals, include_items_from_all_drives, include_labels, include_permissions_for_view, include_removed, include_team_drive_items, page_size, restrict_to_my_drive, spaces, supports_all_drives, supports_team_drives, team_drive_id, body"""
        tool = self._client.get_tool('drive_changes_watch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ChangesWatchOutput.model_validate(coerce_tool_result(result))
