from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import FindUserKeysByQueryToolInput, FindUserKeysByQueryToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FindUserKeysByQueryInput(FindUserKeysByQueryToolInput):
    """Operation input for `find_user_keys_by_query`."""
    pass

class FindUserKeysByQueryOutput(FindUserKeysByQueryToolOutput):
    """Operation output for `find_user_keys_by_query`."""
    pass

class JiraFindUserKeysByResource(BaseResourceClient):
    """Operations for the `find_user_keys_by` resource."""

    @operation(
        name='find_user_keys_by_query',
        title='FindUserKeysByQuery',
        input_model=FindUserKeysByQueryInput,
        output_model=FindUserKeysByQueryOutput,
        tools_used=('find_user_keys_by_query',),
        tags=tuple(['User search']),
    )
    async def query(self, data: FindUserKeysByQueryInput) -> FindUserKeysByQueryOutput:
        """Finds users with a structured query and returns a [paginated](#pagination) list of user keys. This operation takes the users in the range defined by `startAt` and `maxResults`, up to the thousandth user, and then returns only the users from that range that match the structured query. This means the operation usually returns fewer users than specified in `maxResults`. To get all the users who match the structured query, use [Get all users](#api-rest-api-3-users-search-get) and filter the records in your code. **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg). The query statements are: * `is assignee of PROJ` Returns the users that are assignees of at least one issue in project *PROJ*. * `is assignee of (PROJ-1, PROJ-2)` Returns users that are assignees on the issues *PROJ-1* or *PROJ-2*. * `is reporter of (PROJ-1, PROJ-2)` Returns users that are reporters on the issues *PROJ-1* or *PROJ-2*. * `is watcher of (PROJ-1, PROJ-2)` Returns users that are watchers on the issues *PROJ-1* or *PROJ-2*. * `is voter of (PROJ-1, PROJ-2)` Returns users that are voters on the issues *PROJ-1* or *PROJ-2*. * `is commenter of (PROJ-1, PROJ-2)` Returns users that have posted a comment on the issues *PROJ-1* or *PROJ-2*. * `is transitioner of (PROJ-1, PROJ-2)` Returns users that have performed a transition on issues *PROJ-1* or *PROJ-2*. * `[propertyKey].entity.property.path is "property value"` Returns users with the entity property value. The list of issues can be extended as needed, as in *(PROJ-1, PROJ-2, ... PROJ-n)*. Statements can be combined using the `AND` and `OR` operators to form more complex queries. For example: `is assignee of PROJ AND [propertyKey].entity.property.path is "property value"`.

Important inputs: query, start_at, max_results"""
        tool = self._client.get_tool('find_user_keys_by_query')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FindUserKeysByQueryOutput.model_validate(coerce_tool_result(result))
