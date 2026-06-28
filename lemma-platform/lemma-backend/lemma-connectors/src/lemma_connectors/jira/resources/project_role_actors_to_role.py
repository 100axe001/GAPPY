from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddProjectRoleActorsToRoleToolInput, AddProjectRoleActorsToRoleToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddProjectRoleActorsToRoleInput(AddProjectRoleActorsToRoleToolInput):
    """Operation input for `add_project_role_actors_to_role`."""
    pass

class AddProjectRoleActorsToRoleOutput(AddProjectRoleActorsToRoleToolOutput):
    """Operation output for `add_project_role_actors_to_role`."""
    pass

class JiraProjectRoleActorsToRoleResource(BaseResourceClient):
    """Operations for the `project_role_actors_to_role` resource."""

    @operation(
        name='add_project_role_actors_to_role',
        title='AddProjectRoleActorsToRole',
        input_model=AddProjectRoleActorsToRoleInput,
        output_model=AddProjectRoleActorsToRoleOutput,
        tools_used=('add_project_role_actors_to_role',),
        tags=tuple(['Project role actors']),
    )
    async def add(self, data: AddProjectRoleActorsToRoleInput) -> AddProjectRoleActorsToRoleOutput:
        """Adds [default actors](#api-rest-api-3-resolution-get) to a role. You may add groups or users, but you cannot add groups and users in the same request. Changing a project role's default actors does not affect project role members for projects already created. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('add_project_role_actors_to_role')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddProjectRoleActorsToRoleOutput.model_validate(coerce_tool_result(result))
