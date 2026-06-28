from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import PartialUpdateProjectRoleToolInput, PartialUpdateProjectRoleToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class PartialUpdateProjectRoleInput(PartialUpdateProjectRoleToolInput):
    """Operation input for `partial_update_project_role`."""
    pass

class PartialUpdateProjectRoleOutput(PartialUpdateProjectRoleToolOutput):
    """Operation output for `partial_update_project_role`."""
    pass

class JiraPartialUpdateProjectResource(BaseResourceClient):
    """Operations for the `partial_update_project` resource."""

    @operation(
        name='partial_update_project_role',
        title='PartialUpdateProjectRole',
        input_model=PartialUpdateProjectRoleInput,
        output_model=PartialUpdateProjectRoleOutput,
        tools_used=('partial_update_project_role',),
        tags=tuple(['Project roles']),
    )
    async def role(self, data: PartialUpdateProjectRoleInput) -> PartialUpdateProjectRoleOutput:
        """Updates either the project role's name or its description. You cannot update both the name and description at the same time using this operation. If you send a request with a name and a description only the name is updated. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('partial_update_project_role')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return PartialUpdateProjectRoleOutput.model_validate(coerce_tool_result(result))
