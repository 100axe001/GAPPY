from __future__ import annotations

from lemma_connectors.google_drive.generated.tool_types import DriveCommentsCreateToolInput, DriveCommentsCreateToolOutput, DriveCommentsDeleteToolInput, DriveCommentsDeleteToolOutput, DriveCommentsGetToolInput, DriveCommentsGetToolOutput, DriveCommentsListToolInput, DriveCommentsListToolOutput, DriveCommentsUpdateToolInput, DriveCommentsUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CommentsCreateInput(DriveCommentsCreateToolInput):
    """Operation input for `comments_create`."""
    pass

class CommentsCreateOutput(DriveCommentsCreateToolOutput):
    """Operation output for `comments_create`."""
    pass

class CommentsDeleteInput(DriveCommentsDeleteToolInput):
    """Operation input for `comments_delete`."""
    pass

class CommentsDeleteOutput(DriveCommentsDeleteToolOutput):
    """Operation output for `comments_delete`."""
    pass

class CommentsGetInput(DriveCommentsGetToolInput):
    """Operation input for `comments_get`."""
    pass

class CommentsGetOutput(DriveCommentsGetToolOutput):
    """Operation output for `comments_get`."""
    pass

class CommentsListInput(DriveCommentsListToolInput):
    """Operation input for `comments_list`."""
    pass

class CommentsListOutput(DriveCommentsListToolOutput):
    """Operation output for `comments_list`."""
    pass

class CommentsUpdateInput(DriveCommentsUpdateToolInput):
    """Operation input for `comments_update`."""
    pass

class CommentsUpdateOutput(DriveCommentsUpdateToolOutput):
    """Operation output for `comments_update`."""
    pass

class GoogleDriveCommentsResource(BaseResourceClient):
    """Operations for the `comments` resource."""

    @operation(
        name='comments_create',
        title='CommentsCreate',
        input_model=CommentsCreateInput,
        output_model=CommentsCreateOutput,
        tools_used=('drive_comments_create',),
        tags=tuple(['comments']),
    )
    async def create(self, data: CommentsCreateInput) -> CommentsCreateOutput:
        """Creates a comment on a file.

Important inputs: fields, file_id, body"""
        tool = self._client.get_tool('drive_comments_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CommentsCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='comments_delete',
        title='CommentsDelete',
        input_model=CommentsDeleteInput,
        output_model=CommentsDeleteOutput,
        tools_used=('drive_comments_delete',),
        tags=tuple(['comments']),
    )
    async def delete(self, data: CommentsDeleteInput) -> CommentsDeleteOutput:
        """Deletes a comment.

Important inputs: fields, file_id, comment_id"""
        tool = self._client.get_tool('drive_comments_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CommentsDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='comments_get',
        title='CommentsGet',
        input_model=CommentsGetInput,
        output_model=CommentsGetOutput,
        tools_used=('drive_comments_get',),
        tags=tuple(['comments']),
    )
    async def get(self, data: CommentsGetInput) -> CommentsGetOutput:
        """Gets a comment by ID.

Important inputs: fields, file_id, comment_id, include_deleted"""
        tool = self._client.get_tool('drive_comments_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CommentsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='comments_list',
        title='CommentsList',
        input_model=CommentsListInput,
        output_model=CommentsListOutput,
        tools_used=('drive_comments_list',),
        tags=tuple(['comments']),
    )
    async def list(self, data: CommentsListInput) -> CommentsListOutput:
        """Lists a file's comments.

Important inputs: fields, file_id, include_deleted, page_size, page_token, start_modified_time"""
        tool = self._client.get_tool('drive_comments_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CommentsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='comments_update',
        title='CommentsUpdate',
        input_model=CommentsUpdateInput,
        output_model=CommentsUpdateOutput,
        tools_used=('drive_comments_update',),
        tags=tuple(['comments']),
    )
    async def update(self, data: CommentsUpdateInput) -> CommentsUpdateOutput:
        """Updates a comment with patch semantics.

Important inputs: fields, file_id, comment_id, body"""
        tool = self._client.get_tool('drive_comments_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CommentsUpdateOutput.model_validate(coerce_tool_result(result))
