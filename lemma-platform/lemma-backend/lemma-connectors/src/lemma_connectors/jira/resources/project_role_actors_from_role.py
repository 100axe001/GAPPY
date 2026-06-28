from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteProjectRoleActorsFromRoleToolInput, DeleteProjectRoleActorsFromRoleToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteProjectRoleActorsFromRoleInput(DeleteProjectRoleActorsFromRoleToolInput):
    """Operation input for `delete_project_role_actors_from_role`."""
    pass

class DeleteProjectRoleActorsFromRoleOutput(DeleteProjectRoleActorsFromRoleToolOutput):
    """Operation output for `delete_project_role_actors_from_role`."""
    pass

class JiraProjectRoleActorsFromRoleResource(BaseResourceClient):
    """Operations for the `project_role_actors_from_role` resource."""

    @operation(
        name='delete_project_role_actors_from_role',
        title='DeleteProjectRoleActorsFromRole',
        input_model=DeleteProjectRoleActorsFromRoleInput,
        output_model=DeleteProjectRoleActorsFromRoleOutput,
        tools_used=('delete_project_role_actors_from_role',),
        tags=tuple(['Project role actors']),
    )
    async def delete(self, data: DeleteProjectRoleActorsFromRoleInput) -> DeleteProjectRoleActorsFromRoleOutput:
        """Deletes the [default actors](#api-rest-api-3-resolution-get) from a project role. You may delete a group or user, but you cannot delete a group and a user in the same request. Changing a project role's default actors does not affect project role members for projects already created. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, user, group_id, group"""
        tool = self._client.get_tool('delete_project_role_actors_from_role')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteProjectRoleActorsFromRoleOutput.model_validate(coerce_tool_result(result))
