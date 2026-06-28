from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import UsersGetPresenceToolInput, UsersGetPresenceToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersGetPresenceInput(UsersGetPresenceToolInput):
    """Operation input for `users_get_presence`."""
    pass

class UsersGetPresenceOutput(UsersGetPresenceToolOutput):
    """Operation output for `users_get_presence`."""
    pass

class SlackUsersGetResource(BaseResourceClient):
    """Operations for the `users_get` resource."""

    @operation(
        name='users_get_presence',
        title='UsersGetPresence',
        input_model=UsersGetPresenceInput,
        output_model=UsersGetPresenceOutput,
        tools_used=('users_get_presence',),
        tags=tuple(['users']),
    )
    async def presence(self, data: UsersGetPresenceInput) -> UsersGetPresenceOutput:
        """Gets user presence information.

Important inputs: token, user"""
        tool = self._client.get_tool('users_get_presence')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersGetPresenceOutput.model_validate(coerce_tool_result(result))
