from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import ExpandAttachmentForMachinesToolInput, ExpandAttachmentForMachinesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ExpandAttachmentForMachinesInput(ExpandAttachmentForMachinesToolInput):
    """Operation input for `expand_attachment_for_machines`."""
    pass

class ExpandAttachmentForMachinesOutput(ExpandAttachmentForMachinesToolOutput):
    """Operation output for `expand_attachment_for_machines`."""
    pass

class JiraAttachmentForMachinesResource(BaseResourceClient):
    """Operations for the `attachment_for_machines` resource."""

    @operation(
        name='expand_attachment_for_machines',
        title='ExpandAttachmentForMachines',
        input_model=ExpandAttachmentForMachinesInput,
        output_model=ExpandAttachmentForMachinesOutput,
        tools_used=('expand_attachment_for_machines',),
        tags=tuple(['Issue attachments']),
    )
    async def expand(self, data: ExpandAttachmentForMachinesInput) -> ExpandAttachmentForMachinesOutput:
        """Returns the metadata for the contents of an attachment, if it is an archive. For example, if the attachment is a ZIP archive, then information about the files in the archive is returned. Currently, only the ZIP archive format is supported. Use this operation if you are processing the data without presenting it to the user, as this operation only returns the metadata for the contents of the attachment. Otherwise, to retrieve data to present to the user, use [ Get all metadata for an expanded attachment](#api-rest-api-3-attachment-id-expand-human-get) which also returns the metadata for the attachment itself, such as the attachment's ID and name. This operation can be accessed anonymously. **[Permissions](#permissions) required:** For the issue containing the attachment: * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: id"""
        tool = self._client.get_tool('expand_attachment_for_machines')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ExpandAttachmentForMachinesOutput.model_validate(coerce_tool_result(result))
