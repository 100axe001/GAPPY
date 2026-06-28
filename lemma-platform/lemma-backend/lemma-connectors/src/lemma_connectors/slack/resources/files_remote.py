from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import FilesRemoteAddToolInput, FilesRemoteAddToolOutput, FilesRemoteInfoToolInput, FilesRemoteInfoToolOutput, FilesRemoteListToolInput, FilesRemoteListToolOutput, FilesRemoteRemoveToolInput, FilesRemoteRemoveToolOutput, FilesRemoteShareToolInput, FilesRemoteShareToolOutput, FilesRemoteUpdateToolInput, FilesRemoteUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FilesRemoteAddInput(FilesRemoteAddToolInput):
    """Operation input for `files_remote_add`."""
    pass

class FilesRemoteAddOutput(FilesRemoteAddToolOutput):
    """Operation output for `files_remote_add`."""
    pass

class FilesRemoteInfoInput(FilesRemoteInfoToolInput):
    """Operation input for `files_remote_info`."""
    pass

class FilesRemoteInfoOutput(FilesRemoteInfoToolOutput):
    """Operation output for `files_remote_info`."""
    pass

class FilesRemoteListInput(FilesRemoteListToolInput):
    """Operation input for `files_remote_list`."""
    pass

class FilesRemoteListOutput(FilesRemoteListToolOutput):
    """Operation output for `files_remote_list`."""
    pass

class FilesRemoteRemoveInput(FilesRemoteRemoveToolInput):
    """Operation input for `files_remote_remove`."""
    pass

class FilesRemoteRemoveOutput(FilesRemoteRemoveToolOutput):
    """Operation output for `files_remote_remove`."""
    pass

class FilesRemoteShareInput(FilesRemoteShareToolInput):
    """Operation input for `files_remote_share`."""
    pass

class FilesRemoteShareOutput(FilesRemoteShareToolOutput):
    """Operation output for `files_remote_share`."""
    pass

class FilesRemoteUpdateInput(FilesRemoteUpdateToolInput):
    """Operation input for `files_remote_update`."""
    pass

class FilesRemoteUpdateOutput(FilesRemoteUpdateToolOutput):
    """Operation output for `files_remote_update`."""
    pass

class SlackFilesRemoteResource(BaseResourceClient):
    """Operations for the `files_remote` resource."""

    @operation(
        name='files_remote_add',
        title='FilesRemoteAdd',
        input_model=FilesRemoteAddInput,
        output_model=FilesRemoteAddOutput,
        tools_used=('files_remote_add',),
        tags=tuple(['files.remote', 'files']),
    )
    async def add(self, data: FilesRemoteAddInput) -> FilesRemoteAddOutput:
        """Adds a file from a remote service.

Important inputs: body"""
        tool = self._client.get_tool('files_remote_add')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesRemoteAddOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_remote_info',
        title='FilesRemoteInfo',
        input_model=FilesRemoteInfoInput,
        output_model=FilesRemoteInfoOutput,
        tools_used=('files_remote_info',),
        tags=tuple(['files.remote', 'files']),
    )
    async def info(self, data: FilesRemoteInfoInput) -> FilesRemoteInfoOutput:
        """Retrieve information about a remote file added to Slack.

Important inputs: token, file, external_id"""
        tool = self._client.get_tool('files_remote_info')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesRemoteInfoOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_remote_list',
        title='FilesRemoteList',
        input_model=FilesRemoteListInput,
        output_model=FilesRemoteListOutput,
        tools_used=('files_remote_list',),
        tags=tuple(['files.remote', 'files']),
    )
    async def list(self, data: FilesRemoteListInput) -> FilesRemoteListOutput:
        """Retrieve information about a remote file added to Slack.

Important inputs: token, channel, ts_from, ts_to, limit, cursor"""
        tool = self._client.get_tool('files_remote_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesRemoteListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_remote_remove',
        title='FilesRemoteRemove',
        input_model=FilesRemoteRemoveInput,
        output_model=FilesRemoteRemoveOutput,
        tools_used=('files_remote_remove',),
        tags=tuple(['files.remote', 'files']),
    )
    async def remove(self, data: FilesRemoteRemoveInput) -> FilesRemoteRemoveOutput:
        """Remove a remote file.

Important inputs: body"""
        tool = self._client.get_tool('files_remote_remove')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesRemoteRemoveOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_remote_share',
        title='FilesRemoteShare',
        input_model=FilesRemoteShareInput,
        output_model=FilesRemoteShareOutput,
        tools_used=('files_remote_share',),
        tags=tuple(['files.remote', 'files']),
    )
    async def share(self, data: FilesRemoteShareInput) -> FilesRemoteShareOutput:
        """Share a remote file into a channel.

Important inputs: token, file, external_id, channels"""
        tool = self._client.get_tool('files_remote_share')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesRemoteShareOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='files_remote_update',
        title='FilesRemoteUpdate',
        input_model=FilesRemoteUpdateInput,
        output_model=FilesRemoteUpdateOutput,
        tools_used=('files_remote_update',),
        tags=tuple(['files.remote', 'files']),
    )
    async def update(self, data: FilesRemoteUpdateInput) -> FilesRemoteUpdateOutput:
        """Updates an existing remote file.

Important inputs: body"""
        tool = self._client.get_tool('files_remote_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesRemoteUpdateOutput.model_validate(coerce_tool_result(result))
