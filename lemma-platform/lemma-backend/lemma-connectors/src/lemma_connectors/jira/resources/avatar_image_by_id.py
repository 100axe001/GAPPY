from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAvatarImageByIdToolInput, GetAvatarImageByIdToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAvatarImageByIdInput(GetAvatarImageByIdToolInput):
    """Operation input for `get_avatar_image_by_id`."""
    pass

class GetAvatarImageByIdOutput(GetAvatarImageByIdToolOutput):
    """Operation output for `get_avatar_image_by_id`."""
    pass

class JiraAvatarImageByIdResource(BaseResourceClient):
    """Operations for the `avatar_image_by_id` resource."""

    @operation(
        name='get_avatar_image_by_id',
        title='GetAvatarImageById',
        input_model=GetAvatarImageByIdInput,
        output_model=GetAvatarImageByIdOutput,
        tools_used=('get_avatar_image_by_id',),
        tags=tuple(['Avatars']),
    )
    async def get(self, data: GetAvatarImageByIdInput) -> GetAvatarImageByIdOutput:
        """Returns a project or issue type avatar image by ID. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * For system avatars, none. * For custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to. * For custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in.

Important inputs: type, id, size, format"""
        tool = self._client.get_tool('get_avatar_image_by_id')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAvatarImageByIdOutput.model_validate(coerce_tool_result(result))
