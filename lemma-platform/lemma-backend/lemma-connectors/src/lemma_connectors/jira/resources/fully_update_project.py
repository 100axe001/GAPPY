from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import FullyUpdateProjectRoleToolInput, FullyUpdateProjectRoleToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FullyUpdateProjectRoleInput(FullyUpdateProjectRoleToolInput):
    """Operation input for `fully_update_project_role`."""
    pass

class FullyUpdateProjectRoleOutput(FullyUpdateProjectRoleToolOutput):
    """Operation output for `fully_update_project_role`."""
    pass

class JiraFullyUpdateProjectResource(BaseResourceClient):
    """Operations for the `fully_update_project` resource."""

    @operation(
        name='fully_update_project_role',
        title='FullyUpdateProjectRole',
        input_model=FullyUpdateProjectRoleInput,
        output_model=FullyUpdateProjectRoleOutput,
        tools_used=('fully_update_project_role',),
        tags=tuple(['Project roles']),
    )
    async def role(self, data: FullyUpdateProjectRoleInput) -> FullyUpdateProjectRoleOutput:
        """Updates the project role's name and description. You must include both a name and a description in the request. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('fully_update_project_role')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FullyUpdateProjectRoleOutput.model_validate(coerce_tool_result(result))
