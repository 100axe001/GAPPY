from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAssignedPermissionSchemeToolInput, GetAssignedPermissionSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAssignedPermissionSchemeInput(GetAssignedPermissionSchemeToolInput):
    """Operation input for `get_assigned_permission_scheme`."""
    pass

class GetAssignedPermissionSchemeOutput(GetAssignedPermissionSchemeToolOutput):
    """Operation output for `get_assigned_permission_scheme`."""
    pass

class JiraAssignedPermissionSchemeResource(BaseResourceClient):
    """Operations for the `assigned_permission_scheme` resource."""

    @operation(
        name='get_assigned_permission_scheme',
        title='GetAssignedPermissionScheme',
        input_model=GetAssignedPermissionSchemeInput,
        output_model=GetAssignedPermissionSchemeOutput,
        tools_used=('get_assigned_permission_scheme',),
        tags=tuple(['Project permission schemes']),
    )
    async def get(self, data: GetAssignedPermissionSchemeInput) -> GetAssignedPermissionSchemeOutput:
        """Gets the [permission scheme](https://confluence.atlassian.com/x/yodKLg) associated with the project. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

Important inputs: project_key_or_id, expand"""
        tool = self._client.get_tool('get_assigned_permission_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAssignedPermissionSchemeOutput.model_validate(coerce_tool_result(result))
