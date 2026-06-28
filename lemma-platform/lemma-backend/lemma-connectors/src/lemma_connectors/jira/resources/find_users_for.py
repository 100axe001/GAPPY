from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import FindUsersForPickerToolInput, FindUsersForPickerToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FindUsersForPickerInput(FindUsersForPickerToolInput):
    """Operation input for `find_users_for_picker`."""
    pass

class FindUsersForPickerOutput(FindUsersForPickerToolOutput):
    """Operation output for `find_users_for_picker`."""
    pass

class JiraFindUsersForResource(BaseResourceClient):
    """Operations for the `find_users_for` resource."""

    @operation(
        name='find_users_for_picker',
        title='FindUsersForPicker',
        input_model=FindUsersForPickerInput,
        output_model=FindUsersForPickerOutput,
        tools_used=('find_users_for_picker',),
        tags=tuple(['User search']),
    )
    async def picker(self, data: FindUsersForPickerInput) -> FindUsersForPickerOutput:
        """Returns a list of users whose attributes match the query term. The returned object includes the `html` field where the matched query term is highlighted with the HTML strong tag. A list of account IDs can be provided to exclude users from the results. This operation takes the users in the range defined by `maxResults`, up to the thousandth user, and then returns only the users from that range that match the query term. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the query term, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code. Privacy controls are applied to the response based on the users' preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). Anonymous calls and calls by users without the required permission return search results for an exact name match only.

Important inputs: query, max_results, show_avatar, exclude, exclude_account_ids, avatar_size, exclude_connect_users"""
        tool = self._client.get_tool('find_users_for_picker')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FindUsersForPickerOutput.model_validate(coerce_tool_result(result))
