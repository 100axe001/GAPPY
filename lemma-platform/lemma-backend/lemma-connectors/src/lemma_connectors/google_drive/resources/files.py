from __future__ import annotations

from lemma_connectors.google_drive.generated.tool_types import DriveFilesCopyToolInput, DriveFilesCopyToolOutput, DriveFilesCreateToolInput, DriveFilesCreateToolOutput, DriveFilesDeleteToolInput, DriveFilesDeleteToolOutput, DriveFilesEmptyTrashToolInput, DriveFilesEmptyTrashToolOutput, DriveFilesExportToolInput, DriveFilesExportToolOutput, DriveFilesGenerateIdsToolInput, DriveFilesGenerateIdsToolOutput, DriveFilesGetToolInput, DriveFilesGetToolOutput, DriveFilesListLabelsToolInput, DriveFilesListLabelsToolOutput, DriveFilesListToolInput, DriveFilesListToolOutput, DriveFilesModifyLabelsToolInput, DriveFilesModifyLabelsToolOutput, DriveFilesUpdateToolInput, DriveFilesUpdateToolOutput, DriveFilesWatchToolInput, DriveFilesWatchToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FilesCopyInput(DriveFilesCopyToolInput):
    """Operation input for `files_copy`."""
    pass

class FilesCopyOutput(DriveFilesCopyToolOutput):
    """Operation output for `files_copy`."""
    pass

class FilesCreateInput(DriveFilesCreateToolInput):
    """Operation input for `files_create`."""
    pass

class FilesCreateOutput(DriveFilesCreateToolOutput):
    """Operation output for `files_create`."""
    pass

class FilesDeleteInput(DriveFilesDeleteToolInput):
    """Operation input for `files_delete`."""
    pass

class FilesDeleteOutput(DriveFilesDeleteToolOutput):
    """Operation output for `files_delete`."""
    pass

class FilesEmptyTrashInput(DriveFilesEmptyTrashToolInput):
    """Operation input for `files_empty_trash`."""
    pass

class FilesEmptyTrashOutput(DriveFilesEmptyTrashToolOutput):
    """Operation output for `files_empty_trash`."""
    pass

class FilesExportInput(DriveFilesExportToolInput):
    """Operation input for `files_export`."""
    pass

class FilesExportOutput(DriveFilesExportToolOutput):
    """Operation output for `files_export`."""
    pass

class FilesGenerateIdsInput(DriveFilesGenerateIdsToolInput):
    """Operation input for `files_generate_ids`."""
    pass

class FilesGenerateIdsOutput(DriveFilesGenerateIdsToolOutput):
    """Operation output for `files_generate_ids`."""
    pass

class FilesGetInput(DriveFilesGetToolInput):
    """Operation input for `files_get`."""
    pass

class FilesGetOutput(DriveFilesGetToolOutput):
    """Operation output for `files_get`."""
    pass

class FilesListInput(DriveFilesListToolInput):
    """Operation input for `files_list`."""
    pass

class FilesListOutput(DriveFilesListToolOutput):
    """Operation output for `files_list`."""
    pass

class FilesListLabelsInput(DriveFilesListLabelsToolInput):
    """Operation input for `files_list_labels`."""
    pass

class FilesListLabelsOutput(DriveFilesListLabelsToolOutput):
    """Operation output for `files_list_labels`."""
    pass

class FilesModifyLabelsInput(DriveFilesModifyLabelsToolInput):
    """Operation input for `files_modify_labels`."""
    pass

class FilesModifyLabelsOutput(DriveFilesModifyLabelsToolOutput):
    """Operation output for `files_modify_labels`."""
    pass

class FilesUpdateInput(DriveFilesUpdateToolInput):
    """Operation input for `files_update`."""
    pass

class FilesUpdateOutput(DriveFilesUpdateToolOutput):
    """Operation output for `files_update`."""
    pass

class FilesWatchInput(DriveFilesWatchToolInput):
    """Operation input for `files_watch`."""
    pass

class FilesWatchOutput(DriveFilesWatchToolOutput):
    """Operation output for `files_watch`."""
    pass

class GoogleDriveFilesResource(BaseResourceClient):
    """Operations for the `files` resource."""

    @operation(
        name='files_copy',
        title='FilesCopy',
        input_model=FilesCopyInput,
        output_model=FilesCopyOutput,
        tools_used=('drive_files_copy',),
        tags=tuple(['files']),
    )
    async def copy(self, data: FilesCopyInput) -> FilesCopyOutput:
        """Creates a copy of a file and applies any requested updates with patch semantics. Folders cannot be copied.

Important inputs: fields, file_id, enforce_single_parent, ignore_default_visibility, include_labels, include_permissions_for_view, keep_revision_forever, ocr_language, supports_all_drives, supports_team_drives, body"""
        tool = self._client.get_tool('drive_files_copy')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesCopyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_create',
        title='FilesCreate',
        input_model=FilesCreateInput,
        output_model=FilesCreateOutput,
        tools_used=('drive_files_create',),
        tags=tuple(['files']),
    )
    async def create(self, data: FilesCreateInput) -> FilesCreateOutput:
        """Creates a file.

Important inputs: fields, enforce_single_parent, ignore_default_visibility, include_labels, include_permissions_for_view, keep_revision_forever, ocr_language, supports_all_drives, supports_team_drives, use_content_as_indexable_text, body"""
        tool = self._client.get_tool('drive_files_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_delete',
        title='FilesDelete',
        input_model=FilesDeleteInput,
        output_model=FilesDeleteOutput,
        tools_used=('drive_files_delete',),
        tags=tuple(['files']),
    )
    async def delete(self, data: FilesDeleteInput) -> FilesDeleteOutput:
        """Permanently deletes a file owned by the user without moving it to the trash. If the file belongs to a shared drive the user must be an organizer on the parent. If the target is a folder, all descendants owned by the user are also deleted.

Important inputs: fields, file_id, enforce_single_parent, supports_all_drives, supports_team_drives"""
        tool = self._client.get_tool('drive_files_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_empty_trash',
        title='FilesEmptyTrash',
        input_model=FilesEmptyTrashInput,
        output_model=FilesEmptyTrashOutput,
        tools_used=('drive_files_empty_trash',),
        tags=tuple(['files']),
    )
    async def empty_trash(self, data: FilesEmptyTrashInput) -> FilesEmptyTrashOutput:
        """Permanently deletes all of the user's trashed files.

Important inputs: fields, drive_id, enforce_single_parent"""
        tool = self._client.get_tool('drive_files_empty_trash')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesEmptyTrashOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_export',
        title='FilesExport',
        input_model=FilesExportInput,
        output_model=FilesExportOutput,
        tools_used=('drive_files_export',),
        tags=tuple(['files']),
    )
    async def export(self, data: FilesExportInput) -> FilesExportOutput:
        """Exports a Google Workspace document to the requested MIME type and returns exported byte content. Note that the exported content is limited to 10MB.

Important inputs: fields, file_id, mime_type"""
        tool = self._client.get_tool('drive_files_export')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesExportOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_generate_ids',
        title='FilesGenerateIds',
        input_model=FilesGenerateIdsInput,
        output_model=FilesGenerateIdsOutput,
        tools_used=('drive_files_generate_ids',),
        tags=tuple(['files']),
    )
    async def generate_ids(self, data: FilesGenerateIdsInput) -> FilesGenerateIdsOutput:
        """Generates a set of file IDs which can be provided in create or copy requests.

Important inputs: fields, count, space, type"""
        tool = self._client.get_tool('drive_files_generate_ids')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesGenerateIdsOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_get',
        title='FilesGet',
        input_model=FilesGetInput,
        output_model=FilesGetOutput,
        tools_used=('drive_files_get',),
        tags=tuple(['files']),
    )
    async def get(self, data: FilesGetInput) -> FilesGetOutput:
        """Gets a file's metadata or content by ID.

Important inputs: fields, file_id, acknowledge_abuse, include_labels, include_permissions_for_view, supports_all_drives, supports_team_drives"""
        tool = self._client.get_tool('drive_files_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_list',
        title='FilesList',
        input_model=FilesListInput,
        output_model=FilesListOutput,
        tools_used=('drive_files_list',),
        tags=tuple(['files']),
    )
    async def list(self, data: FilesListInput) -> FilesListOutput:
        """Lists or searches files.

Important inputs: fields, corpora, corpus, drive_id, include_items_from_all_drives, include_labels, include_permissions_for_view, include_team_drive_items, order_by, page_size, page_token, q, spaces, supports_all_drives, supports_team_drives, team_drive_id"""
        tool = self._client.get_tool('drive_files_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_list_labels',
        title='FilesListLabels',
        input_model=FilesListLabelsInput,
        output_model=FilesListLabelsOutput,
        tools_used=('drive_files_list_labels',),
        tags=tuple(['files']),
    )
    async def list_labels(self, data: FilesListLabelsInput) -> FilesListLabelsOutput:
        """Lists the labels on a file.

Important inputs: fields, file_id, max_results, page_token"""
        tool = self._client.get_tool('drive_files_list_labels')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesListLabelsOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_modify_labels',
        title='FilesModifyLabels',
        input_model=FilesModifyLabelsInput,
        output_model=FilesModifyLabelsOutput,
        tools_used=('drive_files_modify_labels',),
        tags=tuple(['files']),
    )
    async def modify_labels(self, data: FilesModifyLabelsInput) -> FilesModifyLabelsOutput:
        """Modifies the set of labels on a file.

Important inputs: fields, file_id, body"""
        tool = self._client.get_tool('drive_files_modify_labels')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesModifyLabelsOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_update',
        title='FilesUpdate',
        input_model=FilesUpdateInput,
        output_model=FilesUpdateOutput,
        tools_used=('drive_files_update',),
        tags=tuple(['files']),
    )
    async def update(self, data: FilesUpdateInput) -> FilesUpdateOutput:
        """Updates a file's metadata and/or content. When calling this method, only populate fields in the request that you want to modify. When updating fields, some fields might change automatically, such as modifiedDate. This method supports patch semantics.

Important inputs: fields, file_id, add_parents, enforce_single_parent, include_labels, include_permissions_for_view, keep_revision_forever, ocr_language, remove_parents, supports_all_drives, supports_team_drives, use_content_as_indexable_text, body"""
        tool = self._client.get_tool('drive_files_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesUpdateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_watch',
        title='FilesWatch',
        input_model=FilesWatchInput,
        output_model=FilesWatchOutput,
        tools_used=('drive_files_watch',),
        tags=tuple(['files']),
    )
    async def watch(self, data: FilesWatchInput) -> FilesWatchOutput:
        """Subscribes to changes to a file.

Important inputs: fields, file_id, acknowledge_abuse, include_labels, include_permissions_for_view, supports_all_drives, supports_team_drives, body"""
        tool = self._client.get_tool('drive_files_watch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesWatchOutput.model_validate(coerce_tool_result(result))
