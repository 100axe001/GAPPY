from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetProjectRoleDetailsToolInput, GetProjectRoleDetailsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProjectRoleDetailsInput(GetProjectRoleDetailsToolInput):
    """Operation input for `get_project_role_details`."""
    pass

class GetProjectRoleDetailsOutput(GetProjectRoleDetailsToolOutput):
    """Operation output for `get_project_role_details`."""
    pass

class JiraProjectRoleDetailsResource(BaseResourceClient):
    """Operations for the `project_role_details` resource."""

    @operation(
        name='get_project_role_details',
        title='GetProjectRoleDetails',
        input_model=GetProjectRoleDetailsInput,
        output_model=GetProjectRoleDetailsOutput,
        tools_used=('get_project_role_details',),
        tags=tuple(['Project roles']),
    )
    async def get(self, data: GetProjectRoleDetailsInput) -> GetProjectRoleDetailsOutput:
        """Returns all [project roles](https://confluence.atlassian.com/x/3odKLg) and the details for each role. Note that the list of project roles is common to all projects. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

Important inputs: project_id_or_key, current_member, exclude_connect_addons"""
        tool = self._client.get_tool('get_project_role_details')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectRoleDetailsOutput.model_validate(coerce_tool_result(result))
