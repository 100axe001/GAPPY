from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllProjectRolesToolInput, GetAllProjectRolesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllProjectRolesInput(GetAllProjectRolesToolInput):
    """Operation input for `get_all_project_roles`."""
    pass

class GetAllProjectRolesOutput(GetAllProjectRolesToolOutput):
    """Operation output for `get_all_project_roles`."""
    pass

class JiraAllProjectRolesResource(BaseResourceClient):
    """Operations for the `all_project_roles` resource."""

    @operation(
        name='get_all_project_roles',
        title='GetAllProjectRoles',
        input_model=GetAllProjectRolesInput,
        output_model=GetAllProjectRolesOutput,
        tools_used=('get_all_project_roles',),
        tags=tuple(['Project roles']),
    )
    async def get(self, data: GetAllProjectRolesInput) -> GetAllProjectRolesOutput:
        """Gets a list of all project roles, complete with project role details and default actors. ### About project roles ### [Project roles](https://confluence.atlassian.com/x/3odKLg) are a flexible way to to associate users and groups with projects. In Jira Cloud, the list of project roles is shared globally with all projects, but each project can have a different set of actors associated with it (unlike groups, which have the same membership throughout all Jira applications). Project roles are used in [permission schemes](#api-rest-api-3-permissionscheme-get), [email notification schemes](#api-rest-api-3-notificationscheme-get), [issue security levels](#api-rest-api-3-issuesecurityschemes-get), [comment visibility](#api-rest-api-3-comment-list-post), and workflow conditions. #### Members and actors #### In the Jira REST API, a member of a project role is called an *actor*. An *actor* is a group or user associated with a project role. Actors may be set as [default members](https://confluence.atlassian.com/x/3odKLg#Managingprojectroles-Specifying'defaultmembers'foraprojectrole) of the project role or set at the project level: * Default actors: Users and groups that are assigned to the project role for all newly created projects. The default actors can be removed at the project level later if desired. * Actors: Users and groups that are associated with a project role for a project, which may differ from the default actors. This enables you to assign a user to different roles in different projects. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_all_project_roles')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllProjectRolesOutput.model_validate(coerce_tool_result(result))
