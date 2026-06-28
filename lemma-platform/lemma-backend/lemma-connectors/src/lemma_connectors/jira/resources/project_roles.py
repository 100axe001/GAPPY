from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetProjectRolesToolInput, GetProjectRolesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProjectRolesInput(GetProjectRolesToolInput):
    """Operation input for `get_project_roles`."""
    pass

class GetProjectRolesOutput(GetProjectRolesToolOutput):
    """Operation output for `get_project_roles`."""
    pass

class JiraProjectRolesResource(BaseResourceClient):
    """Operations for the `project_roles` resource."""

    @operation(
        name='get_project_roles',
        title='GetProjectRoles',
        input_model=GetProjectRolesInput,
        output_model=GetProjectRolesOutput,
        tools_used=('get_project_roles',),
        tags=tuple(['Project roles']),
    )
    async def get(self, data: GetProjectRolesInput) -> GetProjectRolesOutput:
        """Returns a list of [project roles](https://confluence.atlassian.com/x/3odKLg) for the project returning the name and self URL for each role. Note that all project roles are shared with all projects in Jira Cloud. See [Get all project roles](#api-rest-api-3-role-get) for more information. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for any project on the site or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: project_id_or_key"""
        tool = self._client.get_tool('get_project_roles')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectRolesOutput.model_validate(coerce_tool_result(result))
