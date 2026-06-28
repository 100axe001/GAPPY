from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import UsersDeletePhotoToolInput, UsersDeletePhotoToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersDeletePhotoInput(UsersDeletePhotoToolInput):
    """Operation input for `users_delete_photo`."""
    pass

class UsersDeletePhotoOutput(UsersDeletePhotoToolOutput):
    """Operation output for `users_delete_photo`."""
    pass

class SlackUsersDeleteResource(BaseResourceClient):
    """Operations for the `users_delete` resource."""

    @operation(
        name='users_delete_photo',
        title='UsersDeletePhoto',
        input_model=UsersDeletePhotoInput,
        output_model=UsersDeletePhotoOutput,
        tools_used=('users_delete_photo',),
        tags=tuple(['users']),
    )
    async def photo(self, data: UsersDeletePhotoInput) -> UsersDeletePhotoOutput:
        """Delete the user profile photo.

Important inputs: body"""
        tool = self._client.get_tool('users_delete_photo')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersDeletePhotoOutput.model_validate(coerce_tool_result(result))
