from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAvatarImageByOwnerToolInput, GetAvatarImageByOwnerToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAvatarImageByOwnerInput(GetAvatarImageByOwnerToolInput):
    """Operation input for `get_avatar_image_by_owner`."""
    pass

class GetAvatarImageByOwnerOutput(GetAvatarImageByOwnerToolOutput):
    """Operation output for `get_avatar_image_by_owner`."""
    pass

class JiraAvatarImageByOwnerResource(BaseResourceClient):
    """Operations for the `avatar_image_by_owner` resource."""

    @operation(
        name='get_avatar_image_by_owner',
        title='GetAvatarImageByOwner',
        input_model=GetAvatarImageByOwnerInput,
        output_model=GetAvatarImageByOwnerOutput,
        tools_used=('get_avatar_image_by_owner',),
        tags=tuple(['Avatars']),
    )
    async def get(self, data: GetAvatarImageByOwnerInput) -> GetAvatarImageByOwnerOutput:
        """Returns the avatar image for a project or issue type. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * For system avatars, none. * For custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to. * For custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.

Important inputs: type, entity_id, size, format"""
        tool = self._client.get_tool('get_avatar_image_by_owner')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAvatarImageByOwnerOutput.model_validate(coerce_tool_result(result))
