from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllPermissionsToolInput, GetAllPermissionsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllPermissionsInput(GetAllPermissionsToolInput):
    """Operation input for `get_all_permissions`."""
    pass

class GetAllPermissionsOutput(GetAllPermissionsToolOutput):
    """Operation output for `get_all_permissions`."""
    pass

class JiraAllPermissionsResource(BaseResourceClient):
    """Operations for the `all_permissions` resource."""

    @operation(
        name='get_all_permissions',
        title='GetAllPermissions',
        input_model=GetAllPermissionsInput,
        output_model=GetAllPermissionsOutput,
        tools_used=('get_all_permissions',),
        tags=tuple(['Permissions']),
    )
    async def get(self, data: GetAllPermissionsInput) -> GetAllPermissionsOutput:
        """Returns all permissions, including: * global permissions. * project permissions. * global permissions added by plugins. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_all_permissions')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllPermissionsOutput.model_validate(coerce_tool_result(result))
