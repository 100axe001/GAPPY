from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import UsersLookupByEmailToolInput, UsersLookupByEmailToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersLookupByEmailInput(UsersLookupByEmailToolInput):
    """Operation input for `users_lookup_by_email`."""
    pass

class UsersLookupByEmailOutput(UsersLookupByEmailToolOutput):
    """Operation output for `users_lookup_by_email`."""
    pass

class SlackUsersLookupByResource(BaseResourceClient):
    """Operations for the `users_lookup_by` resource."""

    @operation(
        name='users_lookup_by_email',
        title='UsersLookupByEmail',
        input_model=UsersLookupByEmailInput,
        output_model=UsersLookupByEmailOutput,
        tools_used=('users_lookup_by_email',),
        tags=tuple(['users']),
    )
    async def email(self, data: UsersLookupByEmailInput) -> UsersLookupByEmailOutput:
        """Find a user with an email address.

Important inputs: token, email"""
        tool = self._client.get_tool('users_lookup_by_email')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersLookupByEmailOutput.model_validate(coerce_tool_result(result))
