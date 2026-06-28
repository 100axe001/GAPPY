from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetPermissionSchemeGrantsToolInput, GetPermissionSchemeGrantsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetPermissionSchemeGrantsInput(GetPermissionSchemeGrantsToolInput):
    """Operation input for `get_permission_scheme_grants`."""
    pass

class GetPermissionSchemeGrantsOutput(GetPermissionSchemeGrantsToolOutput):
    """Operation output for `get_permission_scheme_grants`."""
    pass

class JiraPermissionSchemeGrantsResource(BaseResourceClient):
    """Operations for the `permission_scheme_grants` resource."""

    @operation(
        name='get_permission_scheme_grants',
        title='GetPermissionSchemeGrants',
        input_model=GetPermissionSchemeGrantsInput,
        output_model=GetPermissionSchemeGrantsOutput,
        tools_used=('get_permission_scheme_grants',),
        tags=tuple(['Permission schemes']),
    )
    async def get(self, data: GetPermissionSchemeGrantsInput) -> GetPermissionSchemeGrantsOutput:
        """Returns all permission grants for a permission scheme. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: scheme_id, expand"""
        tool = self._client.get_tool('get_permission_scheme_grants')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetPermissionSchemeGrantsOutput.model_validate(coerce_tool_result(result))
