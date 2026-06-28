from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeletePermissionSchemeEntityToolInput, DeletePermissionSchemeEntityToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeletePermissionSchemeEntityInput(DeletePermissionSchemeEntityToolInput):
    """Operation input for `delete_permission_scheme_entity`."""
    pass

class DeletePermissionSchemeEntityOutput(DeletePermissionSchemeEntityToolOutput):
    """Operation output for `delete_permission_scheme_entity`."""
    pass

class JiraPermissionSchemeEntityResource(BaseResourceClient):
    """Operations for the `permission_scheme_entity` resource."""

    @operation(
        name='delete_permission_scheme_entity',
        title='DeletePermissionSchemeEntity',
        input_model=DeletePermissionSchemeEntityInput,
        output_model=DeletePermissionSchemeEntityOutput,
        tools_used=('delete_permission_scheme_entity',),
        tags=tuple(['Permission schemes']),
    )
    async def delete(self, data: DeletePermissionSchemeEntityInput) -> DeletePermissionSchemeEntityOutput:
        """Deletes a permission grant from a permission scheme. See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-and-grants) for more details. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: scheme_id, permission_id"""
        tool = self._client.get_tool('delete_permission_scheme_entity')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeletePermissionSchemeEntityOutput.model_validate(coerce_tool_result(result))
