from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import UsersConversationsToolInput, UsersConversationsToolOutput, UsersIdentityToolInput, UsersIdentityToolOutput, UsersInfoToolInput, UsersInfoToolOutput, UsersListToolInput, UsersListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersConversationsInput(UsersConversationsToolInput):
    """Operation input for `users_conversations`."""
    pass

class UsersConversationsOutput(UsersConversationsToolOutput):
    """Operation output for `users_conversations`."""
    pass

class UsersIdentityInput(UsersIdentityToolInput):
    """Operation input for `users_identity`."""
    pass

class UsersIdentityOutput(UsersIdentityToolOutput):
    """Operation output for `users_identity`."""
    pass

class UsersInfoInput(UsersInfoToolInput):
    """Operation input for `users_info`."""
    pass

class UsersInfoOutput(UsersInfoToolOutput):
    """Operation output for `users_info`."""
    pass

class UsersListInput(UsersListToolInput):
    """Operation input for `users_list`."""
    pass

class UsersListOutput(UsersListToolOutput):
    """Operation output for `users_list`."""
    pass

class SlackUsersResource(BaseResourceClient):
    """Operations for the `users` resource."""

    @operation(
        name='users_conversations',
        title='UsersConversations',
        input_model=UsersConversationsInput,
        output_model=UsersConversationsOutput,
        tools_used=('users_conversations',),
        tags=tuple(['users']),
    )
    async def conversations(self, data: UsersConversationsInput) -> UsersConversationsOutput:
        """List conversations the calling user may access.

Important inputs: token, user, types, exclude_archived, limit, cursor"""
        tool = self._client.get_tool('users_conversations')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersConversationsOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_identity',
        title='UsersIdentity',
        input_model=UsersIdentityInput,
        output_model=UsersIdentityOutput,
        tools_used=('users_identity',),
        tags=tuple(['users']),
    )
    async def identity(self, data: UsersIdentityInput) -> UsersIdentityOutput:
        """Get a user's identity.

Important inputs: token"""
        tool = self._client.get_tool('users_identity')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersIdentityOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_info',
        title='UsersInfo',
        input_model=UsersInfoInput,
        output_model=UsersInfoOutput,
        tools_used=('users_info',),
        tags=tuple(['users']),
    )
    async def info(self, data: UsersInfoInput) -> UsersInfoOutput:
        """Gets information about a user.

Important inputs: token, include_locale, user"""
        tool = self._client.get_tool('users_info')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersInfoOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_list',
        title='UsersList',
        input_model=UsersListInput,
        output_model=UsersListOutput,
        tools_used=('users_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: UsersListInput) -> UsersListOutput:
        """Lists all users in a Slack team.

Important inputs: token, limit, cursor, include_locale"""
        tool = self._client.get_tool('users_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersListOutput.model_validate(coerce_tool_result(result))
