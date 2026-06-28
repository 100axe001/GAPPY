from __future__ import annotations

from lemma_connectors.google_drive.generated.tool_types import DriveRepliesCreateToolInput, DriveRepliesCreateToolOutput, DriveRepliesDeleteToolInput, DriveRepliesDeleteToolOutput, DriveRepliesGetToolInput, DriveRepliesGetToolOutput, DriveRepliesListToolInput, DriveRepliesListToolOutput, DriveRepliesUpdateToolInput, DriveRepliesUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class RepliesCreateInput(DriveRepliesCreateToolInput):
    """Operation input for `replies_create`."""
    pass

class RepliesCreateOutput(DriveRepliesCreateToolOutput):
    """Operation output for `replies_create`."""
    pass

class RepliesDeleteInput(DriveRepliesDeleteToolInput):
    """Operation input for `replies_delete`."""
    pass

class RepliesDeleteOutput(DriveRepliesDeleteToolOutput):
    """Operation output for `replies_delete`."""
    pass

class RepliesGetInput(DriveRepliesGetToolInput):
    """Operation input for `replies_get`."""
    pass

class RepliesGetOutput(DriveRepliesGetToolOutput):
    """Operation output for `replies_get`."""
    pass

class RepliesListInput(DriveRepliesListToolInput):
    """Operation input for `replies_list`."""
    pass

class RepliesListOutput(DriveRepliesListToolOutput):
    """Operation output for `replies_list`."""
    pass

class RepliesUpdateInput(DriveRepliesUpdateToolInput):
    """Operation input for `replies_update`."""
    pass

class RepliesUpdateOutput(DriveRepliesUpdateToolOutput):
    """Operation output for `replies_update`."""
    pass

class GoogleDriveRepliesResource(BaseResourceClient):
    """Operations for the `replies` resource."""

    @operation(
        name='replies_create',
        title='RepliesCreate',
        input_model=RepliesCreateInput,
        output_model=RepliesCreateOutput,
        tools_used=('drive_replies_create',),
        tags=tuple(['replies']),
    )
    async def create(self, data: RepliesCreateInput) -> RepliesCreateOutput:
        """Creates a reply to a comment.

Important inputs: fields, file_id, comment_id, body"""
        tool = self._client.get_tool('drive_replies_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RepliesCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='replies_delete',
        title='RepliesDelete',
        input_model=RepliesDeleteInput,
        output_model=RepliesDeleteOutput,
        tools_used=('drive_replies_delete',),
        tags=tuple(['replies']),
    )
    async def delete(self, data: RepliesDeleteInput) -> RepliesDeleteOutput:
        """Deletes a reply.

Important inputs: fields, file_id, comment_id, reply_id"""
        tool = self._client.get_tool('drive_replies_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RepliesDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='replies_get',
        title='RepliesGet',
        input_model=RepliesGetInput,
        output_model=RepliesGetOutput,
        tools_used=('drive_replies_get',),
        tags=tuple(['replies']),
    )
    async def get(self, data: RepliesGetInput) -> RepliesGetOutput:
        """Gets a reply by ID.

Important inputs: fields, file_id, comment_id, reply_id, include_deleted"""
        tool = self._client.get_tool('drive_replies_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RepliesGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='replies_list',
        title='RepliesList',
        input_model=RepliesListInput,
        output_model=RepliesListOutput,
        tools_used=('drive_replies_list',),
        tags=tuple(['replies']),
    )
    async def list(self, data: RepliesListInput) -> RepliesListOutput:
        """Lists a comment's replies.

Important inputs: fields, file_id, comment_id, include_deleted, page_size, page_token"""
        tool = self._client.get_tool('drive_replies_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RepliesListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='replies_update',
        title='RepliesUpdate',
        input_model=RepliesUpdateInput,
        output_model=RepliesUpdateOutput,
        tools_used=('drive_replies_update',),
        tags=tuple(['replies']),
    )
    async def update(self, data: RepliesUpdateInput) -> RepliesUpdateOutput:
        """Updates a reply with patch semantics.

Important inputs: fields, file_id, comment_id, reply_id, body"""
        tool = self._client.get_tool('drive_replies_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RepliesUpdateOutput.model_validate(coerce_tool_result(result))
