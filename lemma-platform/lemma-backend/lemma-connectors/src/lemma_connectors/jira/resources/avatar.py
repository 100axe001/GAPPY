from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteAvatarToolInput, DeleteAvatarToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteAvatarInput(DeleteAvatarToolInput):
    """Operation input for `delete_avatar`."""
    pass

class DeleteAvatarOutput(DeleteAvatarToolOutput):
    """Operation output for `delete_avatar`."""
    pass

class JiraAvatarResource(BaseResourceClient):
    """Operations for the `avatar` resource."""

    @operation(
        name='delete_avatar',
        title='DeleteAvatar',
        input_model=DeleteAvatarInput,
        output_model=DeleteAvatarOutput,
        tools_used=('delete_avatar',),
        tags=tuple(['Avatars']),
    )
    async def delete(self, data: DeleteAvatarInput) -> DeleteAvatarOutput:
        """Deletes an avatar from a project or issue type. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: type, owning_object_id, id"""
        tool = self._client.get_tool('delete_avatar')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteAvatarOutput.model_validate(coerce_tool_result(result))
