from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllProjectAvatarsToolInput, GetAllProjectAvatarsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllProjectAvatarsInput(GetAllProjectAvatarsToolInput):
    """Operation input for `get_all_project_avatars`."""
    pass

class GetAllProjectAvatarsOutput(GetAllProjectAvatarsToolOutput):
    """Operation output for `get_all_project_avatars`."""
    pass

class JiraAllProjectAvatarsResource(BaseResourceClient):
    """Operations for the `all_project_avatars` resource."""

    @operation(
        name='get_all_project_avatars',
        title='GetAllProjectAvatars',
        input_model=GetAllProjectAvatarsInput,
        output_model=GetAllProjectAvatarsOutput,
        tools_used=('get_all_project_avatars',),
        tags=tuple(['Project avatars']),
    )
    async def get(self, data: GetAllProjectAvatarsInput) -> GetAllProjectAvatarsOutput:
        """Returns all project avatars, grouped by system and custom avatars. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

Important inputs: project_id_or_key"""
        tool = self._client.get_tool('get_all_project_avatars')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllProjectAvatarsOutput.model_validate(coerce_tool_result(result))
