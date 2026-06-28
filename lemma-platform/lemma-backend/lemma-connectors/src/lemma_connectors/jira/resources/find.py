from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import FindGroupsToolInput, FindGroupsToolOutput, FindUsersToolInput, FindUsersToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FindGroupsInput(FindGroupsToolInput):
    """Operation input for `find_groups`."""
    pass

class FindGroupsOutput(FindGroupsToolOutput):
    """Operation output for `find_groups`."""
    pass

class FindUsersInput(FindUsersToolInput):
    """Operation input for `find_users`."""
    pass

class FindUsersOutput(FindUsersToolOutput):
    """Operation output for `find_users`."""
    pass

class JiraFindResource(BaseResourceClient):
    """Operations for the `find` resource."""

    @operation(
        name='find_groups',
        title='FindGroups',
        input_model=FindGroupsInput,
        output_model=FindGroupsOutput,
        tools_used=('find_groups',),
        tags=tuple(['Groups']),
    )
    async def groups(self, data: FindGroupsInput) -> FindGroupsOutput:
        """Returns a list of groups whose names contain a query string. A list of group names can be provided to exclude groups from the results. The primary use case for this resource is to populate a group picker suggestions list. To this end, the returned object includes the `html` field where the matched query term is highlighted in the group name with the HTML strong tag. Also, the groups list is wrapped in a response object that contains a header for use in the picker, specifically *Showing X of Y matching groups*. The list returns with the groups sorted. If no groups match the list criteria, an empty list is returned. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg). Anonymous calls and calls by users without the required permission return an empty list. *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Without this permission, calls where query is not an exact match to an existing group will return an empty list.

Important inputs: account_id, query, exclude, exclude_id, max_results, case_insensitive, user_name"""
        tool = self._client.get_tool('find_groups')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FindGroupsOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='find_users',
        title='FindUsers',
        input_model=FindUsersInput,
        output_model=FindUsersOutput,
        tools_used=('find_users',),
        tags=tuple(['User search']),
    )
    async def users(self, data: FindUsersInput) -> FindUsersOutput:
        """Returns a list of users that match the search string and property. This operation first applies a filter to match the search string and property, and then takes the filtered users in the range defined by `startAt` and `maxResults`, up to the thousandth user. To get all the users who match the search string and property, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code. This operation can be accessed anonymously. Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details. **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls or calls by users without the required permission return empty search results.

Important inputs: query, username, account_id, start_at, max_results, property"""
        tool = self._client.get_tool('find_users')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FindUsersOutput.model_validate(coerce_tool_result(result))
