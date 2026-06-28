from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreatePermissionGrantToolInput, CreatePermissionGrantToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreatePermissionGrantInput(CreatePermissionGrantToolInput):
    """Operation input for `create_permission_grant`."""
    pass

class CreatePermissionGrantOutput(CreatePermissionGrantToolOutput):
    """Operation output for `create_permission_grant`."""
    pass

class JiraPermissionGrantResource(BaseResourceClient):
    """Operations for the `permission_grant` resource."""

    @operation(
        name='create_permission_grant',
        title='CreatePermissionGrant',
        input_model=CreatePermissionGrantInput,
        output_model=CreatePermissionGrantOutput,
        tools_used=('create_permission_grant',),
        tags=tuple(['Permission schemes']),
    )
    async def create(self, data: CreatePermissionGrantInput) -> CreatePermissionGrantOutput:
        """Creates a permission grant in a permission scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: scheme_id, expand, body"""
        tool = self._client.get_tool('create_permission_grant')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreatePermissionGrantOutput.model_validate(coerce_tool_result(result))
