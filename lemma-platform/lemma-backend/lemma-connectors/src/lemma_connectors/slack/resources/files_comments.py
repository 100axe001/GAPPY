from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import FilesCommentsDeleteToolInput, FilesCommentsDeleteToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FilesCommentsDeleteInput(FilesCommentsDeleteToolInput):
    """Operation input for `files_comments_delete`."""
    pass

class FilesCommentsDeleteOutput(FilesCommentsDeleteToolOutput):
    """Operation output for `files_comments_delete`."""
    pass

class SlackFilesCommentsResource(BaseResourceClient):
    """Operations for the `files_comments` resource."""

    @operation(
        name='files_comments_delete',
        title='FilesCommentsDelete',
        input_model=FilesCommentsDeleteInput,
        output_model=FilesCommentsDeleteOutput,
        tools_used=('files_comments_delete',),
        tags=tuple(['files.comments', 'files']),
    )
    async def delete(self, data: FilesCommentsDeleteInput) -> FilesCommentsDeleteOutput:
        """Deletes an existing comment on a file.

Important inputs: token, body"""
        tool = self._client.get_tool('files_comments_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesCommentsDeleteOutput.model_validate(coerce_tool_result(result))
