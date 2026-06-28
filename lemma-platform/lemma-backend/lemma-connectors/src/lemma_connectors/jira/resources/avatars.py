from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAvatarsToolInput, GetAvatarsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAvatarsInput(GetAvatarsToolInput):
    """Operation input for `get_avatars`."""
    pass

class GetAvatarsOutput(GetAvatarsToolOutput):
    """Operation output for `get_avatars`."""
    pass

class JiraAvatarsResource(BaseResourceClient):
    """Operations for the `avatars` resource."""

    @operation(
        name='get_avatars',
        title='GetAvatars',
        input_model=GetAvatarsInput,
        output_model=GetAvatarsOutput,
        tools_used=('get_avatars',),
        tags=tuple(['Avatars']),
    )
    async def get(self, data: GetAvatarsInput) -> GetAvatarsOutput:
        """Returns the system and custom avatars for a project or issue type. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * for custom project avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the avatar belongs to. * for custom issue type avatars, *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the issue type is used in. * for system avatars, none.

Important inputs: type, entity_id"""
        tool = self._client.get_tool('get_avatars')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAvatarsOutput.model_validate(coerce_tool_result(result))
