from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetProjectRoleActorsForRoleToolInput, GetProjectRoleActorsForRoleToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProjectRoleActorsForRoleInput(GetProjectRoleActorsForRoleToolInput):
    """Operation input for `get_project_role_actors_for_role`."""
    pass

class GetProjectRoleActorsForRoleOutput(GetProjectRoleActorsForRoleToolOutput):
    """Operation output for `get_project_role_actors_for_role`."""
    pass

class JiraProjectRoleActorsForRoleResource(BaseResourceClient):
    """Operations for the `project_role_actors_for_role` resource."""

    @operation(
        name='get_project_role_actors_for_role',
        title='GetProjectRoleActorsForRole',
        input_model=GetProjectRoleActorsForRoleInput,
        output_model=GetProjectRoleActorsForRoleOutput,
        tools_used=('get_project_role_actors_for_role',),
        tags=tuple(['Project role actors']),
    )
    async def get(self, data: GetProjectRoleActorsForRoleInput) -> GetProjectRoleActorsForRoleOutput:
        """Returns the [default actors](#api-rest-api-3-resolution-get) for the project role. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('get_project_role_actors_for_role')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectRoleActorsForRoleOutput.model_validate(coerce_tool_result(result))
