from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import UsersSetActiveToolInput, UsersSetActiveToolOutput, UsersSetPhotoToolInput, UsersSetPhotoToolOutput, UsersSetPresenceToolInput, UsersSetPresenceToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersSetActiveInput(UsersSetActiveToolInput):
    """Operation input for `users_set_active`."""
    pass

class UsersSetActiveOutput(UsersSetActiveToolOutput):
    """Operation output for `users_set_active`."""
    pass

class UsersSetPhotoInput(UsersSetPhotoToolInput):
    """Operation input for `users_set_photo`."""
    pass

class UsersSetPhotoOutput(UsersSetPhotoToolOutput):
    """Operation output for `users_set_photo`."""
    pass

class UsersSetPresenceInput(UsersSetPresenceToolInput):
    """Operation input for `users_set_presence`."""
    pass

class UsersSetPresenceOutput(UsersSetPresenceToolOutput):
    """Operation output for `users_set_presence`."""
    pass

class SlackUsersSetResource(BaseResourceClient):
    """Operations for the `users_set` resource."""

    @operation(
        name='users_set_active',
        title='UsersSetActive',
        input_model=UsersSetActiveInput,
        output_model=UsersSetActiveOutput,
        tools_used=('users_set_active',),
        tags=tuple(['users']),
    )
    async def active(self, data: UsersSetActiveInput) -> UsersSetActiveOutput:
        """Marked a user as active. Deprecated and non-functional.

Important inputs: token"""
        tool = self._client.get_tool('users_set_active')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSetActiveOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_set_photo',
        title='UsersSetPhoto',
        input_model=UsersSetPhotoInput,
        output_model=UsersSetPhotoOutput,
        tools_used=('users_set_photo',),
        tags=tuple(['users']),
    )
    async def photo(self, data: UsersSetPhotoInput) -> UsersSetPhotoOutput:
        """Set the user profile photo.

Important inputs: body"""
        tool = self._client.get_tool('users_set_photo')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSetPhotoOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_set_presence',
        title='UsersSetPresence',
        input_model=UsersSetPresenceInput,
        output_model=UsersSetPresenceOutput,
        tools_used=('users_set_presence',),
        tags=tuple(['users']),
    )
    async def presence(self, data: UsersSetPresenceInput) -> UsersSetPresenceOutput:
        """Manually sets user presence.

Important inputs: token, body"""
        tool = self._client.get_tool('users_set_presence')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSetPresenceOutput.model_validate(coerce_tool_result(result))
