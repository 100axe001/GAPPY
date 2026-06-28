from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetSharePermissionsToolInput, GetSharePermissionsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetSharePermissionsInput(GetSharePermissionsToolInput):
    """Operation input for `get_share_permissions`."""
    pass

class GetSharePermissionsOutput(GetSharePermissionsToolOutput):
    """Operation output for `get_share_permissions`."""
    pass

class JiraSharePermissionsResource(BaseResourceClient):
    """Operations for the `share_permissions` resource."""

    @operation(
        name='get_share_permissions',
        title='GetSharePermissions',
        input_model=GetSharePermissionsInput,
        output_model=GetSharePermissionsOutput,
        tools_used=('get_share_permissions',),
        tags=tuple(['Filter sharing']),
    )
    async def get(self, data: GetSharePermissionsInput) -> GetSharePermissionsOutput:
        """Returns the share permissions for a filter. A filter can be shared with groups, projects, all logged-in users, or the public. Sharing with all logged-in users or the public is known as a global share permission. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None, however, share permissions are only returned for: * filters owned by the user. * filters shared with a group that the user is a member of. * filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for. * filters shared with a public project. * filters shared with the public.

Important inputs: id"""
        tool = self._client.get_tool('get_share_permissions')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetSharePermissionsOutput.model_validate(coerce_tool_result(result))
