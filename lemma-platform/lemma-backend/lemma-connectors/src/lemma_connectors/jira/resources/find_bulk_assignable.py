from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import FindBulkAssignableUsersToolInput, FindBulkAssignableUsersToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FindBulkAssignableUsersInput(FindBulkAssignableUsersToolInput):
    """Operation input for `find_bulk_assignable_users`."""
    pass

class FindBulkAssignableUsersOutput(FindBulkAssignableUsersToolOutput):
    """Operation output for `find_bulk_assignable_users`."""
    pass

class JiraFindBulkAssignableResource(BaseResourceClient):
    """Operations for the `find_bulk_assignable` resource."""

    @operation(
        name='find_bulk_assignable_users',
        title='FindBulkAssignableUsers',
        input_model=FindBulkAssignableUsersInput,
        output_model=FindBulkAssignableUsersOutput,
        tools_used=('find_bulk_assignable_users',),
        tags=tuple(['User search']),
    )
    async def users(self, data: FindBulkAssignableUsersInput) -> FindBulkAssignableUsersOutput:
        """Returns a list of users who can be assigned issues in one or more projects. The list may be restricted to users whose attributes match a string. This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that can be assigned issues in the projects. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who can be assigned issues in the projects, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code. Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: query, username, account_id, project_keys, start_at, max_results"""
        tool = self._client.get_tool('find_bulk_assignable_users')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FindBulkAssignableUsersOutput.model_validate(coerce_tool_result(result))
