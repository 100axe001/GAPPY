from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import FindUsersWithAllPermissionsToolInput, FindUsersWithAllPermissionsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FindUsersWithAllPermissionsInput(FindUsersWithAllPermissionsToolInput):
    """Operation input for `find_users_with_all_permissions`."""
    pass

class FindUsersWithAllPermissionsOutput(FindUsersWithAllPermissionsToolOutput):
    """Operation output for `find_users_with_all_permissions`."""
    pass

class JiraFindUsersWithAllResource(BaseResourceClient):
    """Operations for the `find_users_with_all` resource."""

    @operation(
        name='find_users_with_all_permissions',
        title='FindUsersWithAllPermissions',
        input_model=FindUsersWithAllPermissionsInput,
        output_model=FindUsersWithAllPermissionsOutput,
        tools_used=('find_users_with_all_permissions',),
        tags=tuple(['User search']),
    )
    async def permissions(self, data: FindUsersWithAllPermissionsInput) -> FindUsersWithAllPermissionsOutput:
        """Returns a list of users who fulfill these criteria: * their user attributes match a search string. * they have a set of permissions for a project or issue. If no search string is provided, a list of all users with the permissions is returned. This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the search string and have permission for the project or issue. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the search string and have permission for the project or issue, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code. Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg), to get users for any project. * *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project, to get users for that project.

Important inputs: query, username, account_id, permissions, issue_key, project_key, start_at, max_results"""
        tool = self._client.get_tool('find_users_with_all_permissions')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FindUsersWithAllPermissionsOutput.model_validate(coerce_tool_result(result))
