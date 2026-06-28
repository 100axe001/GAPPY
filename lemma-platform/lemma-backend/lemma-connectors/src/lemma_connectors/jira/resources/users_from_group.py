from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetUsersFromGroupToolInput, GetUsersFromGroupToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetUsersFromGroupInput(GetUsersFromGroupToolInput):
    """Operation input for `get_users_from_group`."""
    pass

class GetUsersFromGroupOutput(GetUsersFromGroupToolOutput):
    """Operation output for `get_users_from_group`."""
    pass

class JiraUsersFromGroupResource(BaseResourceClient):
    """Operations for the `users_from_group` resource."""

    @operation(
        name='get_users_from_group',
        title='GetUsersFromGroup',
        input_model=GetUsersFromGroupInput,
        output_model=GetUsersFromGroupOutput,
        tools_used=('get_users_from_group',),
        tags=tuple(['Groups']),
    )
    async def get(self, data: GetUsersFromGroupInput) -> GetUsersFromGroupOutput:
        """Returns a [paginated](#pagination) list of all users in a group. Note that users are ordered by username, however the username is not returned in the results due to privacy reasons. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: groupname, group_id, include_inactive_users, start_at, max_results"""
        tool = self._client.get_tool('get_users_from_group')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetUsersFromGroupOutput.model_validate(coerce_tool_result(result))
