from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteAndReplaceVersionToolInput, DeleteAndReplaceVersionToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteAndReplaceVersionInput(DeleteAndReplaceVersionToolInput):
    """Operation input for `delete_and_replace_version`."""
    pass

class DeleteAndReplaceVersionOutput(DeleteAndReplaceVersionToolOutput):
    """Operation output for `delete_and_replace_version`."""
    pass

class JiraAndReplaceVersionResource(BaseResourceClient):
    """Operations for the `and_replace_version` resource."""

    @operation(
        name='delete_and_replace_version',
        title='DeleteAndReplaceVersion',
        input_model=DeleteAndReplaceVersionInput,
        output_model=DeleteAndReplaceVersionOutput,
        tools_used=('delete_and_replace_version',),
        tags=tuple(['Project versions']),
    )
    async def delete(self, data: DeleteAndReplaceVersionInput) -> DeleteAndReplaceVersionOutput:
        """Deletes a project version. Alternative versions can be provided to update issues that use the deleted version in `fixVersion`, `affectedVersion`, or any version picker custom fields. If alternatives are not provided, occurrences of `fixVersion`, `affectedVersion`, and any version picker custom field, that contain the deleted version, are cleared. Any replacement version must be in the same project as the version being deleted and cannot be the version being deleted. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

Important inputs: id, body"""
        tool = self._client.get_tool('delete_and_replace_version')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteAndReplaceVersionOutput.model_validate(coerce_tool_result(result))
