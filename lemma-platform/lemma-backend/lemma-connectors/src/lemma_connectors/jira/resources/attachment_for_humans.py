from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import ExpandAttachmentForHumansToolInput, ExpandAttachmentForHumansToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ExpandAttachmentForHumansInput(ExpandAttachmentForHumansToolInput):
    """Operation input for `expand_attachment_for_humans`."""
    pass

class ExpandAttachmentForHumansOutput(ExpandAttachmentForHumansToolOutput):
    """Operation output for `expand_attachment_for_humans`."""
    pass

class JiraAttachmentForHumansResource(BaseResourceClient):
    """Operations for the `attachment_for_humans` resource."""

    @operation(
        name='expand_attachment_for_humans',
        title='ExpandAttachmentForHumans',
        input_model=ExpandAttachmentForHumansInput,
        output_model=ExpandAttachmentForHumansOutput,
        tools_used=('expand_attachment_for_humans',),
        tags=tuple(['Issue attachments']),
    )
    async def expand(self, data: ExpandAttachmentForHumansInput) -> ExpandAttachmentForHumansOutput:
        """Returns the metadata for the contents of an attachment, if it is an archive, and metadata for the attachment itself. For example, if the attachment is a ZIP archive, then information about the files in the archive is returned and metadata for the ZIP archive. Currently, only the ZIP archive format is supported. Use this operation to retrieve data that is presented to the user, as this operation returns the metadata for the attachment itself, such as the attachment's ID and name. Otherwise, use [ Get contents metadata for an expanded attachment](#api-rest-api-3-attachment-id-expand-raw-get), which only returns the metadata for the attachment's contents. This operation can be accessed anonymously. **[Permissions](#permissions) required:** For the issue containing the attachment: * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: id"""
        tool = self._client.get_tool('expand_attachment_for_humans')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ExpandAttachmentForHumansOutput.model_validate(coerce_tool_result(result))
