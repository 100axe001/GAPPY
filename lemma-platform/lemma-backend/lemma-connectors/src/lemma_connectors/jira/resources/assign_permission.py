from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AssignPermissionSchemeToolInput, AssignPermissionSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AssignPermissionSchemeInput(AssignPermissionSchemeToolInput):
    """Operation input for `assign_permission_scheme`."""
    pass

class AssignPermissionSchemeOutput(AssignPermissionSchemeToolOutput):
    """Operation output for `assign_permission_scheme`."""
    pass

class JiraAssignPermissionResource(BaseResourceClient):
    """Operations for the `assign_permission` resource."""

    @operation(
        name='assign_permission_scheme',
        title='AssignPermissionScheme',
        input_model=AssignPermissionSchemeInput,
        output_model=AssignPermissionSchemeOutput,
        tools_used=('assign_permission_scheme',),
        tags=tuple(['Project permission schemes']),
    )
    async def scheme(self, data: AssignPermissionSchemeInput) -> AssignPermissionSchemeOutput:
        """Assigns a permission scheme with a project. See [Managing project permissions](https://confluence.atlassian.com/x/yodKLg) for more information about permission schemes. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: project_key_or_id, expand, body"""
        tool = self._client.get_tool('assign_permission_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AssignPermissionSchemeOutput.model_validate(coerce_tool_result(result))
