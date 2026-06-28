from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAttachmentContentToolInput, GetAttachmentContentToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAttachmentContentInput(GetAttachmentContentToolInput):
    """Operation input for `get_attachment_content`."""
    pass

class GetAttachmentContentOutput(GetAttachmentContentToolOutput):
    """Operation output for `get_attachment_content`."""
    pass

class JiraAttachmentContentResource(BaseResourceClient):
    """Operations for the `attachment_content` resource."""

    @operation(
        name='get_attachment_content',
        title='GetAttachmentContent',
        input_model=GetAttachmentContentInput,
        output_model=GetAttachmentContentOutput,
        tools_used=('get_attachment_content',),
        tags=tuple(['Issue attachments']),
    )
    async def get(self, data: GetAttachmentContentInput) -> GetAttachmentContentOutput:
        """Returns the contents of an attachment. A `Range` header can be set to define a range of bytes within the attachment to download. See the [HTTP Range header standard](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Range) for details. To return a thumbnail of the attachment, use [Get attachment thumbnail](#api-rest-api-3-attachment-thumbnail-id-get). This operation can be accessed anonymously. **[Permissions](#permissions) required:** For the issue containing the attachment: * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: id, redirect"""
        tool = self._client.get_tool('get_attachment_content')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAttachmentContentOutput.model_validate(coerce_tool_result(result))
