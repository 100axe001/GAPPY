from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import FindUsersWithBrowsePermissionToolInput, FindUsersWithBrowsePermissionToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FindUsersWithBrowsePermissionInput(FindUsersWithBrowsePermissionToolInput):
    """Operation input for `find_users_with_browse_permission`."""
    pass

class FindUsersWithBrowsePermissionOutput(FindUsersWithBrowsePermissionToolOutput):
    """Operation output for `find_users_with_browse_permission`."""
    pass

class JiraFindUsersWithBrowseResource(BaseResourceClient):
    """Operations for the `find_users_with_browse` resource."""

    @operation(
        name='find_users_with_browse_permission',
        title='FindUsersWithBrowsePermission',
        input_model=FindUsersWithBrowsePermissionInput,
        output_model=FindUsersWithBrowsePermissionOutput,
        tools_used=('find_users_with_browse_permission',),
        tags=tuple(['User search']),
    )
    async def permission(self, data: FindUsersWithBrowsePermissionInput) -> FindUsersWithBrowsePermissionOutput:
        """Returns a list of users who fulfill these criteria: * their user attributes match a search string. * they have permission to browse issues. Use this resource to find users who can browse: * an issue, by providing the `issueKey`. * any issue in a project, by providing the `projectKey`. This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the search string and have permission to browse issues. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the search string and have permission to browse issues, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code. Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without the required permission return empty search results.

Important inputs: query, username, account_id, issue_key, project_key, start_at, max_results"""
        tool = self._client.get_tool('find_users_with_browse_permission')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FindUsersWithBrowsePermissionOutput.model_validate(coerce_tool_result(result))
