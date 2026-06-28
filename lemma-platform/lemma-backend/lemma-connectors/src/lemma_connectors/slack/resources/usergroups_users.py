from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import UsergroupsUsersListToolInput, UsergroupsUsersListToolOutput, UsergroupsUsersUpdateToolInput, UsergroupsUsersUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsergroupsUsersListInput(UsergroupsUsersListToolInput):
    """Operation input for `usergroups_users_list`."""
    pass

class UsergroupsUsersListOutput(UsergroupsUsersListToolOutput):
    """Operation output for `usergroups_users_list`."""
    pass

class UsergroupsUsersUpdateInput(UsergroupsUsersUpdateToolInput):
    """Operation input for `usergroups_users_update`."""
    pass

class UsergroupsUsersUpdateOutput(UsergroupsUsersUpdateToolOutput):
    """Operation output for `usergroups_users_update`."""
    pass

class SlackUsergroupsUsersResource(BaseResourceClient):
    """Operations for the `usergroups_users` resource."""

    @operation(
        name='usergroups_users_list',
        title='UsergroupsUsersList',
        input_model=UsergroupsUsersListInput,
        output_model=UsergroupsUsersListOutput,
        tools_used=('usergroups_users_list',),
        tags=tuple(['usergroups.users', 'usergroups']),
    )
    async def list(self, data: UsergroupsUsersListInput) -> UsergroupsUsersListOutput:
        """List all users in a User Group.

Important inputs: token, include_disabled, usergroup"""
        tool = self._client.get_tool('usergroups_users_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsergroupsUsersListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='usergroups_users_update',
        title='UsergroupsUsersUpdate',
        input_model=UsergroupsUsersUpdateInput,
        output_model=UsergroupsUsersUpdateOutput,
        tools_used=('usergroups_users_update',),
        tags=tuple(['usergroups.users', 'usergroups']),
    )
    async def update(self, data: UsergroupsUsersUpdateInput) -> UsergroupsUsersUpdateOutput:
        """Update the list of users for a User Group.

Important inputs: token, body"""
        tool = self._client.get_tool('usergroups_users_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsergroupsUsersUpdateOutput.model_validate(coerce_tool_result(result))
