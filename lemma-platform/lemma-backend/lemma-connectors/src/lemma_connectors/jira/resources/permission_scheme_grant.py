from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetPermissionSchemeGrantToolInput, GetPermissionSchemeGrantToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetPermissionSchemeGrantInput(GetPermissionSchemeGrantToolInput):
    """Operation input for `get_permission_scheme_grant`."""
    pass

class GetPermissionSchemeGrantOutput(GetPermissionSchemeGrantToolOutput):
    """Operation output for `get_permission_scheme_grant`."""
    pass

class JiraPermissionSchemeGrantResource(BaseResourceClient):
    """Operations for the `permission_scheme_grant` resource."""

    @operation(
        name='get_permission_scheme_grant',
        title='GetPermissionSchemeGrant',
        input_model=GetPermissionSchemeGrantInput,
        output_model=GetPermissionSchemeGrantOutput,
        tools_used=('get_permission_scheme_grant',),
        tags=tuple(['Permission schemes']),
    )
    async def get(self, data: GetPermissionSchemeGrantInput) -> GetPermissionSchemeGrantOutput:
        """Returns a permission grant. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: scheme_id, permission_id, expand"""
        tool = self._client.get_tool('get_permission_scheme_grant')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetPermissionSchemeGrantOutput.model_validate(coerce_tool_result(result))
