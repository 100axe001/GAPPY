from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import FilesSharedPublicUrlToolInput, FilesSharedPublicUrlToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FilesSharedPublicUrlInput(FilesSharedPublicUrlToolInput):
    """Operation input for `files_shared_public_url`."""
    pass

class FilesSharedPublicUrlOutput(FilesSharedPublicUrlToolOutput):
    """Operation output for `files_shared_public_url`."""
    pass

class SlackFilesSharedPublicResource(BaseResourceClient):
    """Operations for the `files_shared_public` resource."""

    @operation(
        name='files_shared_public_url',
        title='FilesSharedPublicUrl',
        input_model=FilesSharedPublicUrlInput,
        output_model=FilesSharedPublicUrlOutput,
        tools_used=('files_shared_public_url',),
        tags=tuple(['files']),
    )
    async def url(self, data: FilesSharedPublicUrlInput) -> FilesSharedPublicUrlOutput:
        """Enables a file for public/external sharing.

Important inputs: token, body"""
        tool = self._client.get_tool('files_shared_public_url')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesSharedPublicUrlOutput.model_validate(coerce_tool_result(result))
