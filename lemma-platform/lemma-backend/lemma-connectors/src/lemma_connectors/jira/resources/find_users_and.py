from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import FindUsersAndGroupsToolInput, FindUsersAndGroupsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FindUsersAndGroupsInput(FindUsersAndGroupsToolInput):
    """Operation input for `find_users_and_groups`."""
    pass

class FindUsersAndGroupsOutput(FindUsersAndGroupsToolOutput):
    """Operation output for `find_users_and_groups`."""
    pass

class JiraFindUsersAndResource(BaseResourceClient):
    """Operations for the `find_users_and` resource."""

    @operation(
        name='find_users_and_groups',
        title='FindUsersAndGroups',
        input_model=FindUsersAndGroupsInput,
        output_model=FindUsersAndGroupsOutput,
        tools_used=('find_users_and_groups',),
        tags=tuple(['Group and user picker']),
    )
    async def groups(self, data: FindUsersAndGroupsInput) -> FindUsersAndGroupsOutput:
        """Returns a list of users and groups matching a string. The string is used: * for users, to find a case-insensitive match with display name and e-mail address. Note that if a user has hidden their email address in their user profile, partial matches of the email address will not find the user. An exact match is required. * for groups, to find a case-sensitive match with group name. For example, if the string *tin* is used, records with the display name *Tina*, email address *sarah@tinplatetraining.com*, and the group *accounting* would be returned. Optionally, the search can be refined to: * the projects and issue types associated with a custom field, such as a user picker. The search can then be further refined to return only users and groups that have permission to view specific: * projects. * issue types. If multiple projects or issue types are specified, they must be a subset of those enabled for the custom field or no results are returned. For example, if a field is enabled for projects A, B, and C then the search could be limited to projects B and C. However, if the search is limited to projects B and D, nothing is returned. * not return Connect app users and groups. * return groups that have a case-insensitive match with the query. The primary use case for this resource is to populate a picker field suggestion list with users or groups. To this end, the returned object includes an `html` field for each list. This field highlights the matched query term in the item name with the HTML strong tag. Also, each list is wrapped in a response object that contains a header for use in a picker, specifically *Showing X of Y matching groups*. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/yodKLg).

Important inputs: query, max_results, show_avatar, field_id, project_id, issue_type_id, avatar_size, case_insensitive, exclude_connect_addons"""
        tool = self._client.get_tool('find_users_and_groups')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FindUsersAndGroupsOutput.model_validate(coerce_tool_result(result))
