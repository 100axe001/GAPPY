from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAttachmentThumbnailToolInput, GetAttachmentThumbnailToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAttachmentThumbnailInput(GetAttachmentThumbnailToolInput):
    """Operation input for `get_attachment_thumbnail`."""
    pass

class GetAttachmentThumbnailOutput(GetAttachmentThumbnailToolOutput):
    """Operation output for `get_attachment_thumbnail`."""
    pass

class JiraAttachmentThumbnailResource(BaseResourceClient):
    """Operations for the `attachment_thumbnail` resource."""

    @operation(
        name='get_attachment_thumbnail',
        title='GetAttachmentThumbnail',
        input_model=GetAttachmentThumbnailInput,
        output_model=GetAttachmentThumbnailOutput,
        tools_used=('get_attachment_thumbnail',),
        tags=tuple(['Issue attachments']),
    )
    async def get(self, data: GetAttachmentThumbnailInput) -> GetAttachmentThumbnailOutput:
        """Returns the thumbnail of an attachment. To return the attachment contents, use [Get attachment content](#api-rest-api-3-attachment-content-id-get). This operation can be accessed anonymously. **[Permissions](#permissions) required:** For the issue containing the attachment: * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: id, redirect, fallback_to_default, width, height"""
        tool = self._client.get_tool('get_attachment_thumbnail')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAttachmentThumbnailOutput.model_validate(coerce_tool_result(result))
