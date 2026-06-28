from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import BulkGetGroupsToolInput, BulkGetGroupsToolOutput, BulkGetUsersToolInput, BulkGetUsersToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class BulkGetGroupsInput(BulkGetGroupsToolInput):
    """Operation input for `bulk_get_groups`."""
    pass

class BulkGetGroupsOutput(BulkGetGroupsToolOutput):
    """Operation output for `bulk_get_groups`."""
    pass

class BulkGetUsersInput(BulkGetUsersToolInput):
    """Operation input for `bulk_get_users`."""
    pass

class BulkGetUsersOutput(BulkGetUsersToolOutput):
    """Operation output for `bulk_get_users`."""
    pass

class JiraBulkGetResource(BaseResourceClient):
    """Operations for the `bulk_get` resource."""

    @operation(
        name='bulk_get_groups',
        title='BulkGetGroups',
        input_model=BulkGetGroupsInput,
        output_model=BulkGetGroupsOutput,
        tools_used=('bulk_get_groups',),
        tags=tuple(['Groups']),
    )
    async def groups(self, data: BulkGetGroupsInput) -> BulkGetGroupsOutput:
        """Returns a [paginated](#pagination) list of groups. **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, group_id, group_name, access_type, application_key"""
        tool = self._client.get_tool('bulk_get_groups')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return BulkGetGroupsOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='bulk_get_users',
        title='BulkGetUsers',
        input_model=BulkGetUsersInput,
        output_model=BulkGetUsersOutput,
        tools_used=('bulk_get_users',),
        tags=tuple(['Users']),
    )
    async def users(self, data: BulkGetUsersInput) -> BulkGetUsersOutput:
        """Returns a [paginated](#pagination) list of the users specified by one or more account IDs. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: start_at, max_results, username, account_id"""
        tool = self._client.get_tool('bulk_get_users')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return BulkGetUsersOutput.model_validate(coerce_tool_result(result))
