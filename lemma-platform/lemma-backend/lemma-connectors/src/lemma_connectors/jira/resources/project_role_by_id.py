from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetProjectRoleByIdToolInput, GetProjectRoleByIdToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProjectRoleByIdInput(GetProjectRoleByIdToolInput):
    """Operation input for `get_project_role_by_id`."""
    pass

class GetProjectRoleByIdOutput(GetProjectRoleByIdToolOutput):
    """Operation output for `get_project_role_by_id`."""
    pass

class JiraProjectRoleByIdResource(BaseResourceClient):
    """Operations for the `project_role_by_id` resource."""

    @operation(
        name='get_project_role_by_id',
        title='GetProjectRoleById',
        input_model=GetProjectRoleByIdInput,
        output_model=GetProjectRoleByIdOutput,
        tools_used=('get_project_role_by_id',),
        tags=tuple(['Project roles']),
    )
    async def get(self, data: GetProjectRoleByIdInput) -> GetProjectRoleByIdOutput:
        """Gets the project role details and the default actors associated with the role. The list of default actors is sorted by display name. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('get_project_role_by_id')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectRoleByIdOutput.model_validate(coerce_tool_result(result))
