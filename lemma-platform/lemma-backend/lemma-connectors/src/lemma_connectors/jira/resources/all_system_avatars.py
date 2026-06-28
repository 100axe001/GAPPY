from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllSystemAvatarsToolInput, GetAllSystemAvatarsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllSystemAvatarsInput(GetAllSystemAvatarsToolInput):
    """Operation input for `get_all_system_avatars`."""
    pass

class GetAllSystemAvatarsOutput(GetAllSystemAvatarsToolOutput):
    """Operation output for `get_all_system_avatars`."""
    pass

class JiraAllSystemAvatarsResource(BaseResourceClient):
    """Operations for the `all_system_avatars` resource."""

    @operation(
        name='get_all_system_avatars',
        title='GetAllSystemAvatars',
        input_model=GetAllSystemAvatarsInput,
        output_model=GetAllSystemAvatarsOutput,
        tools_used=('get_all_system_avatars',),
        tags=tuple(['Avatars']),
    )
    async def get(self, data: GetAllSystemAvatarsInput) -> GetAllSystemAvatarsOutput:
        """Returns a list of system avatar details by owner type, where the owner types are issue type, project, or user. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: type"""
        tool = self._client.get_tool('get_all_system_avatars')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllSystemAvatarsOutput.model_validate(coerce_tool_result(result))
