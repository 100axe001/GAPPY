from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import FilesDeleteToolInput, FilesDeleteToolOutput, FilesInfoToolInput, FilesInfoToolOutput, FilesListToolInput, FilesListToolOutput, FilesUploadToolInput, FilesUploadToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FilesDeleteInput(FilesDeleteToolInput):
    """Operation input for `files_delete`."""
    pass

class FilesDeleteOutput(FilesDeleteToolOutput):
    """Operation output for `files_delete`."""
    pass

class FilesInfoInput(FilesInfoToolInput):
    """Operation input for `files_info`."""
    pass

class FilesInfoOutput(FilesInfoToolOutput):
    """Operation output for `files_info`."""
    pass

class FilesListInput(FilesListToolInput):
    """Operation input for `files_list`."""
    pass

class FilesListOutput(FilesListToolOutput):
    """Operation output for `files_list`."""
    pass

class FilesUploadInput(FilesUploadToolInput):
    """Operation input for `files_upload`."""
    pass

class FilesUploadOutput(FilesUploadToolOutput):
    """Operation output for `files_upload`."""
    pass

class SlackFilesResource(BaseResourceClient):
    """Operations for the `files` resource."""

    @operation(
        name='files_delete',
        title='FilesDelete',
        input_model=FilesDeleteInput,
        output_model=FilesDeleteOutput,
        tools_used=('files_delete',),
        tags=tuple(['files']),
    )
    async def delete(self, data: FilesDeleteInput) -> FilesDeleteOutput:
        """Deletes a file.

Important inputs: token, body"""
        tool = self._client.get_tool('files_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_info',
        title='FilesInfo',
        input_model=FilesInfoInput,
        output_model=FilesInfoOutput,
        tools_used=('files_info',),
        tags=tuple(['files']),
    )
    async def info(self, data: FilesInfoInput) -> FilesInfoOutput:
        """Gets information about a file.

Important inputs: token, file, count, page, limit, cursor"""
        tool = self._client.get_tool('files_info')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesInfoOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_list',
        title='FilesList',
        input_model=FilesListInput,
        output_model=FilesListOutput,
        tools_used=('files_list',),
        tags=tuple(['files']),
    )
    async def list(self, data: FilesListInput) -> FilesListOutput:
        """List for a team, in a channel, or from a user with applied filters.

Important inputs: token, user, channel, ts_from, ts_to, types, count, page, show_files_hidden_by_limit"""
        tool = self._client.get_tool('files_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_upload',
        title='FilesUpload',
        input_model=FilesUploadInput,
        output_model=FilesUploadOutput,
        tools_used=('files_upload',),
        tags=tuple(['files']),
    )
    async def upload(self, data: FilesUploadInput) -> FilesUploadOutput:
        """Uploads or creates a file.

Important inputs: body"""
        tool = self._client.get_tool('files_upload')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesUploadOutput.model_validate(coerce_tool_result(result))
