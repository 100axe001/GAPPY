from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetBulkPermissionsToolInput, GetBulkPermissionsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetBulkPermissionsInput(GetBulkPermissionsToolInput):
    """Operation input for `get_bulk_permissions`."""
    pass

class GetBulkPermissionsOutput(GetBulkPermissionsToolOutput):
    """Operation output for `get_bulk_permissions`."""
    pass

class JiraBulkPermissionsResource(BaseResourceClient):
    """Operations for the `bulk_permissions` resource."""

    @operation(
        name='get_bulk_permissions',
        title='GetBulkPermissions',
        input_model=GetBulkPermissionsInput,
        output_model=GetBulkPermissionsOutput,
        tools_used=('get_bulk_permissions',),
        tags=tuple(['Permissions']),
    )
    async def get(self, data: GetBulkPermissionsInput) -> GetBulkPermissionsOutput:
        """Returns: * for a list of global permissions, the global permissions granted to a user. * for a list of project permissions and lists of projects and issues, for each project permission a list of the projects and issues a user can access or manipulate. If no account ID is provided, the operation returns details for the logged in user. Note that: * Invalid project and issue IDs are ignored. * A maximum of 1000 projects and 1000 issues can be checked. * Null values in `globalPermissions`, `projectPermissions`, `projectPermissions.projects`, and `projectPermissions.issues` are ignored. * Empty strings in `projectPermissions.permissions` are ignored. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to check the permissions for other users, otherwise none. However, Connect apps can make a call from the app server to the product to obtain permission details for any user, without admin permission. This Connect app ability doesn't apply to calls made using AP.request() in a browser.

Important inputs: body"""
        tool = self._client.get_tool('get_bulk_permissions')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetBulkPermissionsOutput.model_validate(coerce_tool_result(result))
