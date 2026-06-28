from __future__ import annotations

from lemma_connectors.google_drive.generated.tool_types import DriveRevisionsDeleteToolInput, DriveRevisionsDeleteToolOutput, DriveRevisionsGetToolInput, DriveRevisionsGetToolOutput, DriveRevisionsListToolInput, DriveRevisionsListToolOutput, DriveRevisionsUpdateToolInput, DriveRevisionsUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class RevisionsDeleteInput(DriveRevisionsDeleteToolInput):
    """Operation input for `revisions_delete`."""
    pass

class RevisionsDeleteOutput(DriveRevisionsDeleteToolOutput):
    """Operation output for `revisions_delete`."""
    pass

class RevisionsGetInput(DriveRevisionsGetToolInput):
    """Operation input for `revisions_get`."""
    pass

class RevisionsGetOutput(DriveRevisionsGetToolOutput):
    """Operation output for `revisions_get`."""
    pass

class RevisionsListInput(DriveRevisionsListToolInput):
    """Operation input for `revisions_list`."""
    pass

class RevisionsListOutput(DriveRevisionsListToolOutput):
    """Operation output for `revisions_list`."""
    pass

class RevisionsUpdateInput(DriveRevisionsUpdateToolInput):
    """Operation input for `revisions_update`."""
    pass

class RevisionsUpdateOutput(DriveRevisionsUpdateToolOutput):
    """Operation output for `revisions_update`."""
    pass

class GoogleDriveRevisionsResource(BaseResourceClient):
    """Operations for the `revisions` resource."""

    @operation(
        name='revisions_delete',
        title='RevisionsDelete',
        input_model=RevisionsDeleteInput,
        output_model=RevisionsDeleteOutput,
        tools_used=('drive_revisions_delete',),
        tags=tuple(['revisions']),
    )
    async def delete(self, data: RevisionsDeleteInput) -> RevisionsDeleteOutput:
        """Permanently deletes a file version. You can only delete revisions for files with binary content in Google Drive, like images or videos. Revisions for other files, like Google Docs or Sheets, and the last remaining file version can't be deleted.

Important inputs: fields, file_id, revision_id"""
        tool = self._client.get_tool('drive_revisions_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RevisionsDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='revisions_get',
        title='RevisionsGet',
        input_model=RevisionsGetInput,
        output_model=RevisionsGetOutput,
        tools_used=('drive_revisions_get',),
        tags=tuple(['revisions']),
    )
    async def get(self, data: RevisionsGetInput) -> RevisionsGetOutput:
        """Gets a revision's metadata or content by ID.

Important inputs: fields, file_id, revision_id, acknowledge_abuse"""
        tool = self._client.get_tool('drive_revisions_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RevisionsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='revisions_list',
        title='RevisionsList',
        input_model=RevisionsListInput,
        output_model=RevisionsListOutput,
        tools_used=('drive_revisions_list',),
        tags=tuple(['revisions']),
    )
    async def list(self, data: RevisionsListInput) -> RevisionsListOutput:
        """Lists a file's revisions.

Important inputs: fields, file_id, page_size, page_token"""
        tool = self._client.get_tool('drive_revisions_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RevisionsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='revisions_update',
        title='RevisionsUpdate',
        input_model=RevisionsUpdateInput,
        output_model=RevisionsUpdateOutput,
        tools_used=('drive_revisions_update',),
        tags=tuple(['revisions']),
    )
    async def update(self, data: RevisionsUpdateInput) -> RevisionsUpdateOutput:
        """Updates a revision with patch semantics.

Important inputs: fields, file_id, revision_id, body"""
        tool = self._client.get_tool('drive_revisions_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RevisionsUpdateOutput.model_validate(coerce_tool_result(result))
