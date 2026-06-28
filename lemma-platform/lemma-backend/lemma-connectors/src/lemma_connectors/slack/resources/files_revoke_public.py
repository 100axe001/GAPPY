from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import FilesRevokePublicUrlToolInput, FilesRevokePublicUrlToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FilesRevokePublicUrlInput(FilesRevokePublicUrlToolInput):
    """Operation input for `files_revoke_public_url`."""
    pass

class FilesRevokePublicUrlOutput(FilesRevokePublicUrlToolOutput):
    """Operation output for `files_revoke_public_url`."""
    pass

class SlackFilesRevokePublicResource(BaseResourceClient):
    """Operations for the `files_revoke_public` resource."""

    @operation(
        name='files_revoke_public_url',
        title='FilesRevokePublicUrl',
        input_model=FilesRevokePublicUrlInput,
        output_model=FilesRevokePublicUrlOutput,
        tools_used=('files_revoke_public_url',),
        tags=tuple(['files']),
    )
    async def url(self, data: FilesRevokePublicUrlInput) -> FilesRevokePublicUrlOutput:
        """Revokes public/external sharing access for a file.

Important inputs: token, body"""
        tool = self._client.get_tool('files_revoke_public_url')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FilesRevokePublicUrlOutput.model_validate(coerce_tool_result(result))
