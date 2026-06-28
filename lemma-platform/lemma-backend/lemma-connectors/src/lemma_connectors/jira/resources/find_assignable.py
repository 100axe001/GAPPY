from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import FindAssignableUsersToolInput, FindAssignableUsersToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FindAssignableUsersInput(FindAssignableUsersToolInput):
    """Operation input for `find_assignable_users`."""
    pass

class FindAssignableUsersOutput(FindAssignableUsersToolOutput):
    """Operation output for `find_assignable_users`."""
    pass

class JiraFindAssignableResource(BaseResourceClient):
    """Operations for the `find_assignable` resource."""

    @operation(
        name='find_assignable_users',
        title='FindAssignableUsers',
        input_model=FindAssignableUsersInput,
        output_model=FindAssignableUsersOutput,
        tools_used=('find_assignable_users',),
        tags=tuple(['User search']),
    )
    async def users(self, data: FindAssignableUsersInput) -> FindAssignableUsersOutput:
        """Returns a list of users that can be assigned to an issue. Use this operation to find the list of users who can be assigned to: * a new issue, by providing the `projectKeyOrId`. * an updated issue, by providing the `issueKey`. * to an issue during a transition (workflow action), by providing the `issueKey` and the transition id in `actionDescriptorId`. You can obtain the IDs of an issue's valid transitions using the `transitions` option in the `expand` parameter of [ Get issue](#api-rest-api-3-issue-issueIdOrKey-get). In all these cases, you can pass an account ID to determine if a user can be assigned to an issue. The user is returned in the response if they can be assigned to the issue or issue transition. This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that can be assigned the issue. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who can be assigned the issue, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code. Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: query, session_id, username, account_id, project, issue_key, start_at, max_results, action_descriptor_id, recommend"""
        tool = self._client.get_tool('find_assignable_users')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FindAssignableUsersOutput.model_validate(coerce_tool_result(result))
