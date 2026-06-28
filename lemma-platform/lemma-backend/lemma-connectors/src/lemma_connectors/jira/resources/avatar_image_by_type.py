from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAvatarImageByTypeToolInput, GetAvatarImageByTypeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAvatarImageByTypeInput(GetAvatarImageByTypeToolInput):
    """Operation input for `get_avatar_image_by_type`."""
    pass

class GetAvatarImageByTypeOutput(GetAvatarImageByTypeToolOutput):
    """Operation output for `get_avatar_image_by_type`."""
    pass

class JiraAvatarImageByTypeResource(BaseResourceClient):
    """Operations for the `avatar_image_by_type` resource."""

    @operation(
        name='get_avatar_image_by_type',
        title='GetAvatarImageByType',
        input_model=GetAvatarImageByTypeInput,
        output_model=GetAvatarImageByTypeOutput,
        tools_used=('get_avatar_image_by_type',),
        tags=tuple(['Avatars']),
    )
    async def get(self, data: GetAvatarImageByTypeInput) -> GetAvatarImageByTypeOutput:
        """Returns the default project or issue type avatar image. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: type, size, format"""
        tool = self._client.get_tool('get_avatar_image_by_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAvatarImageByTypeOutput.model_validate(coerce_tool_result(result))
