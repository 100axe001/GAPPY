from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersGetProfileToolInput, GmailUsersGetProfileToolOutput, GmailUsersStopToolInput, GmailUsersStopToolOutput, GmailUsersWatchToolInput, GmailUsersWatchToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProfileInput(GmailUsersGetProfileToolInput):
    """Operation input for `get_profile`."""
    pass

class GetProfileOutput(GmailUsersGetProfileToolOutput):
    """Operation output for `get_profile`."""
    pass

class StopInput(GmailUsersStopToolInput):
    """Operation input for `stop`."""
    pass

class StopOutput(GmailUsersStopToolOutput):
    """Operation output for `stop`."""
    pass

class WatchInput(GmailUsersWatchToolInput):
    """Operation input for `watch`."""
    pass

class WatchOutput(GmailUsersWatchToolOutput):
    """Operation output for `watch`."""
    pass

class GmailRootResource(BaseResourceClient):
    """Operations for the `root` resource."""

    @operation(
        name='get_profile',
        title='GetProfile',
        input_model=GetProfileInput,
        output_model=GetProfileOutput,
        tools_used=('gmail_users_get_profile',),
        tags=tuple(['users']),
    )
    async def get_profile(self, data: GetProfileInput) -> GetProfileOutput:
        """Gets the current user's Gmail profile.

Important inputs: fields, user_id"""
        tool = self._client.get_tool('gmail_users_get_profile')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProfileOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='stop',
        title='Stop',
        input_model=StopInput,
        output_model=StopOutput,
        tools_used=('gmail_users_stop',),
        tags=tuple(['users']),
    )
    async def stop(self, data: StopInput) -> StopOutput:
        """Stop receiving push notifications for the given user mailbox.

Important inputs: fields, user_id"""
        tool = self._client.get_tool('gmail_users_stop')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return StopOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='watch',
        title='Watch',
        input_model=WatchInput,
        output_model=WatchOutput,
        tools_used=('gmail_users_watch',),
        tags=tuple(['users']),
    )
    async def watch(self, data: WatchInput) -> WatchOutput:
        """Set up or update a push notification watch on the given user mailbox.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_watch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return WatchOutput.model_validate(coerce_tool_result(result))
