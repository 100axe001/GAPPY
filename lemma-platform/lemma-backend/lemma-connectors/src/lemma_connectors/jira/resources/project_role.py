from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateProjectRoleToolInput, CreateProjectRoleToolOutput, DeleteProjectRoleToolInput, DeleteProjectRoleToolOutput, GetProjectRoleToolInput, GetProjectRoleToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateProjectRoleInput(CreateProjectRoleToolInput):
    """Operation input for `create_project_role`."""
    pass

class CreateProjectRoleOutput(CreateProjectRoleToolOutput):
    """Operation output for `create_project_role`."""
    pass

class DeleteProjectRoleInput(DeleteProjectRoleToolInput):
    """Operation input for `delete_project_role`."""
    pass

class DeleteProjectRoleOutput(DeleteProjectRoleToolOutput):
    """Operation output for `delete_project_role`."""
    pass

class GetProjectRoleInput(GetProjectRoleToolInput):
    """Operation input for `get_project_role`."""
    pass

class GetProjectRoleOutput(GetProjectRoleToolOutput):
    """Operation output for `get_project_role`."""
    pass

class JiraProjectRoleResource(BaseResourceClient):
    """Operations for the `project_role` resource."""

    @operation(
        name='create_project_role',
        title='CreateProjectRole',
        input_model=CreateProjectRoleInput,
        output_model=CreateProjectRoleOutput,
        tools_used=('create_project_role',),
        tags=tuple(['Project roles']),
    )
    async def create(self, data: CreateProjectRoleInput) -> CreateProjectRoleOutput:
        """Creates a new project role with no [default actors](#api-rest-api-3-resolution-get). You can use the [Add default actors to project role](#api-rest-api-3-role-id-actors-post) operation to add default actors to the project role after creating it. *Note that although a new project role is available to all projects upon creation, any default actors that are associated with the project role are not added to projects that existed prior to the role being created.*< **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_project_role')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateProjectRoleOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_project_role',
        title='DeleteProjectRole',
        input_model=DeleteProjectRoleInput,
        output_model=DeleteProjectRoleOutput,
        tools_used=('delete_project_role',),
        tags=tuple(['Project roles']),
    )
    async def delete(self, data: DeleteProjectRoleInput) -> DeleteProjectRoleOutput:
        """Deletes a project role. You must specify a replacement project role if you wish to delete a project role that is in use. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, swap"""
        tool = self._client.get_tool('delete_project_role')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteProjectRoleOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_project_role',
        title='GetProjectRole',
        input_model=GetProjectRoleInput,
        output_model=GetProjectRoleOutput,
        tools_used=('get_project_role',),
        tags=tuple(['Project roles']),
    )
    async def get(self, data: GetProjectRoleInput) -> GetProjectRoleOutput:
        """Returns a project role's details and actors associated with the project. The list of actors is sorted by display name. To check whether a user belongs to a role based on their group memberships, use [Get user](#api-rest-api-3-user-get) with the `groups` expand parameter selected. Then check whether the user keys and groups match with the actors returned for the project. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: project_id_or_key, id, exclude_inactive_users"""
        tool = self._client.get_tool('get_project_role')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectRoleOutput.model_validate(coerce_tool_result(result))
