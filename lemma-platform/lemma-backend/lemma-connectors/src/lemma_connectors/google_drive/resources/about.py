from __future__ import annotations

from lemma_connectors.google_drive.generated.tool_types import DriveAboutGetToolInput, DriveAboutGetToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AboutGetInput(DriveAboutGetToolInput):
    """Operation input for `about_get`."""
    pass

class AboutGetOutput(DriveAboutGetToolOutput):
    """Operation output for `about_get`."""
    pass

class GoogleDriveAboutResource(BaseResourceClient):
    """Operations for the `about` resource."""

    @operation(
        name='about_get',
        title='AboutGet',
        input_model=AboutGetInput,
        output_model=AboutGetOutput,
        tools_used=('drive_about_get',),
        tags=tuple(['about']),
    )
    async def get(self, data: AboutGetInput) -> AboutGetOutput:
        """Gets information about the user, the user's Drive, and system capabilities.

Important inputs: fields"""
        tool = self._client.get_tool('drive_about_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AboutGetOutput.model_validate(coerce_tool_result(result))
