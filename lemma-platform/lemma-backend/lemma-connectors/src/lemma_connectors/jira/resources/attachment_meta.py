from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAttachmentMetaToolInput, GetAttachmentMetaToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAttachmentMetaInput(GetAttachmentMetaToolInput):
    """Operation input for `get_attachment_meta`."""
    pass

class GetAttachmentMetaOutput(GetAttachmentMetaToolOutput):
    """Operation output for `get_attachment_meta`."""
    pass

class JiraAttachmentMetaResource(BaseResourceClient):
    """Operations for the `attachment_meta` resource."""

    @operation(
        name='get_attachment_meta',
        title='GetAttachmentMeta',
        input_model=GetAttachmentMetaInput,
        output_model=GetAttachmentMetaOutput,
        tools_used=('get_attachment_meta',),
        tags=tuple(['Issue attachments']),
    )
    async def get(self, data: GetAttachmentMetaInput) -> GetAttachmentMetaOutput:
        """Returns the attachment settings, that is, whether attachments are enabled and the maximum attachment size allowed. Note that there are also [project permissions](https://confluence.atlassian.com/x/yodKLg) that restrict whether users can create and delete attachments. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_attachment_meta')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAttachmentMetaOutput.model_validate(coerce_tool_result(result))
