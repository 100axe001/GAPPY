from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersGetProfileToolInput, GmailUsersGetProfileToolOutput, GmailUsersStopToolInput, GmailUsersStopToolOutput, GmailUsersWatchToolInput, GmailUsersWatchToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersGetProfileInput(GmailUsersGetProfileToolInput):
    """Operation input for `users_get_profile`."""
    pass

class UsersGetProfileOutput(GmailUsersGetProfileToolOutput):
    """Operation output for `users_get_profile`."""
    pass

class UsersStopInput(GmailUsersStopToolInput):
    """Operation input for `users_stop`."""
    pass

class UsersStopOutput(GmailUsersStopToolOutput):
    """Operation output for `users_stop`."""
    pass

class UsersWatchInput(GmailUsersWatchToolInput):
    """Operation input for `users_watch`."""
    pass

class UsersWatchOutput(GmailUsersWatchToolOutput):
    """Operation output for `users_watch`."""
    pass

class GmailUsersResource(BaseResourceClient):
    """Operations grouped around the `users` resource."""

    @operation(
        name='users_get_profile',
        title='UsersGetProfile',
        input_model=UsersGetProfileInput,
        output_model=UsersGetProfileOutput,
        tools_used=('gmail_users_get_profile',),
        tags=tuple(['users']),
    )
    async def get_profile(self, data: UsersGetProfileInput) -> UsersGetProfileOutput:
        """Gets the current user's Gmail profile.

Use this when you want to gets the current user's Gmail profile.
Key inputs: fields, user_id."""
        tool = self._client.get_tool('gmail_users_get_profile')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersGetProfileOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_stop',
        title='UsersStop',
        input_model=UsersStopInput,
        output_model=UsersStopOutput,
        tools_used=('gmail_users_stop',),
        tags=tuple(['users']),
    )
    async def stop(self, data: UsersStopInput) -> UsersStopOutput:
        """Stop receiving push notifications for the given user mailbox.

Use this when you want to stop receiving push notifications for the given user mailbox.
Key inputs: fields, user_id."""
        tool = self._client.get_tool('gmail_users_stop')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersStopOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_watch',
        title='UsersWatch',
        input_model=UsersWatchInput,
        output_model=UsersWatchOutput,
        tools_used=('gmail_users_watch',),
        tags=tuple(['users']),
    )
    async def watch(self, data: UsersWatchInput) -> UsersWatchOutput:
        """Set up or update a push notification watch on the given user mailbox.

Use this when you want to set up or update a push notification watch on the given user mailbox.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_watch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersWatchOutput.model_validate(coerce_tool_result(result))
