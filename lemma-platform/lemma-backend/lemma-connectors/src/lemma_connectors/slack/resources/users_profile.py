from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import UsersProfileGetToolInput, UsersProfileGetToolOutput, UsersProfileSetToolInput, UsersProfileSetToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersProfileGetInput(UsersProfileGetToolInput):
    """Operation input for `users_profile_get`."""
    pass

class UsersProfileGetOutput(UsersProfileGetToolOutput):
    """Operation output for `users_profile_get`."""
    pass

class UsersProfileSetInput(UsersProfileSetToolInput):
    """Operation input for `users_profile_set`."""
    pass

class UsersProfileSetOutput(UsersProfileSetToolOutput):
    """Operation output for `users_profile_set`."""
    pass

class SlackUsersProfileResource(BaseResourceClient):
    """Operations for the `users_profile` resource."""

    @operation(
        name='users_profile_get',
        title='UsersProfileGet',
        input_model=UsersProfileGetInput,
        output_model=UsersProfileGetOutput,
        tools_used=('users_profile_get',),
        tags=tuple(['users.profile', 'users']),
    )
    async def get(self, data: UsersProfileGetInput) -> UsersProfileGetOutput:
        """Retrieves a user's profile information.

Important inputs: token, include_labels, user"""
        tool = self._client.get_tool('users_profile_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersProfileGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_profile_set',
        title='UsersProfileSet',
        input_model=UsersProfileSetInput,
        output_model=UsersProfileSetOutput,
        tools_used=('users_profile_set',),
        tags=tuple(['users.profile', 'users']),
    )
    async def set(self, data: UsersProfileSetInput) -> UsersProfileSetOutput:
        """Set the profile information for a user.

Important inputs: token, body"""
        tool = self._client.get_tool('users_profile_set')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersProfileSetOutput.model_validate(coerce_tool_result(result))
