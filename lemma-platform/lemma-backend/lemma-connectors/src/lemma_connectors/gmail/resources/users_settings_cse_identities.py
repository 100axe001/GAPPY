from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsCseIdentitiesCreateToolInput, GmailUsersSettingsCseIdentitiesCreateToolOutput, GmailUsersSettingsCseIdentitiesDeleteToolInput, GmailUsersSettingsCseIdentitiesDeleteToolOutput, GmailUsersSettingsCseIdentitiesGetToolInput, GmailUsersSettingsCseIdentitiesGetToolOutput, GmailUsersSettingsCseIdentitiesListToolInput, GmailUsersSettingsCseIdentitiesListToolOutput, GmailUsersSettingsCseIdentitiesPatchToolInput, GmailUsersSettingsCseIdentitiesPatchToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersSettingsCseIdentitiesCreateInput(GmailUsersSettingsCseIdentitiesCreateToolInput):
    """Operation input for `users_settings_cse_identities_create`."""
    pass

class UsersSettingsCseIdentitiesCreateOutput(GmailUsersSettingsCseIdentitiesCreateToolOutput):
    """Operation output for `users_settings_cse_identities_create`."""
    pass

class UsersSettingsCseIdentitiesDeleteInput(GmailUsersSettingsCseIdentitiesDeleteToolInput):
    """Operation input for `users_settings_cse_identities_delete`."""
    pass

class UsersSettingsCseIdentitiesDeleteOutput(GmailUsersSettingsCseIdentitiesDeleteToolOutput):
    """Operation output for `users_settings_cse_identities_delete`."""
    pass

class UsersSettingsCseIdentitiesGetInput(GmailUsersSettingsCseIdentitiesGetToolInput):
    """Operation input for `users_settings_cse_identities_get`."""
    pass

class UsersSettingsCseIdentitiesGetOutput(GmailUsersSettingsCseIdentitiesGetToolOutput):
    """Operation output for `users_settings_cse_identities_get`."""
    pass

class UsersSettingsCseIdentitiesListInput(GmailUsersSettingsCseIdentitiesListToolInput):
    """Operation input for `users_settings_cse_identities_list`."""
    pass

class UsersSettingsCseIdentitiesListOutput(GmailUsersSettingsCseIdentitiesListToolOutput):
    """Operation output for `users_settings_cse_identities_list`."""
    pass

class UsersSettingsCseIdentitiesPatchInput(GmailUsersSettingsCseIdentitiesPatchToolInput):
    """Operation input for `users_settings_cse_identities_patch`."""
    pass

class UsersSettingsCseIdentitiesPatchOutput(GmailUsersSettingsCseIdentitiesPatchToolOutput):
    """Operation output for `users_settings_cse_identities_patch`."""
    pass

class GmailUsersSettingsCseIdentitiesResource(BaseResourceClient):
    """Operations grouped around the `users_settings_cse_identities` resource."""

    @operation(
        name='users_settings_cse_identities_create',
        title='UsersSettingsCseIdentitiesCreate',
        input_model=UsersSettingsCseIdentitiesCreateInput,
        output_model=UsersSettingsCseIdentitiesCreateOutput,
        tools_used=('gmail_users_settings_cse_identities_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: UsersSettingsCseIdentitiesCreateInput) -> UsersSettingsCseIdentitiesCreateOutput:
        """Creates and configures a client-side encryption identity that's authorized to send mail from the user account. Google publishes the S/MIME certificate to a shared domain-wide directory so that people within a Google Workspace organization can encrypt and send mail to the identity.

Use this when you want to creates and configures a client-side encryption identity that's authorized to send mail from the user account. Google publishes the S/MIME certificate to a shared domain-wide directory so that people within a Google Workspace organization can encrypt and send mail to the identity.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_settings_cse_identities_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsCseIdentitiesCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_cse_identities_delete',
        title='UsersSettingsCseIdentitiesDelete',
        input_model=UsersSettingsCseIdentitiesDeleteInput,
        output_model=UsersSettingsCseIdentitiesDeleteOutput,
        tools_used=('gmail_users_settings_cse_identities_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: UsersSettingsCseIdentitiesDeleteInput) -> UsersSettingsCseIdentitiesDeleteOutput:
        """Deletes a client-side encryption identity. The authenticated user can no longer use the identity to send encrypted messages. You cannot restore the identity after you delete it. Instead, use the CreateCseIdentity method to create another identity with the same configuration.

Use this when you want to deletes a client-side encryption identity. The authenticated user can no longer use the identity to send encrypted messages. You cannot restore the identity after you delete it. Instead, use the CreateCseIdentity method to create another identity with the same configuration.
Key inputs: fields, user_id, cse_email_address."""
        tool = self._client.get_tool('gmail_users_settings_cse_identities_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsCseIdentitiesDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_cse_identities_get',
        title='UsersSettingsCseIdentitiesGet',
        input_model=UsersSettingsCseIdentitiesGetInput,
        output_model=UsersSettingsCseIdentitiesGetOutput,
        tools_used=('gmail_users_settings_cse_identities_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: UsersSettingsCseIdentitiesGetInput) -> UsersSettingsCseIdentitiesGetOutput:
        """Retrieves a client-side encryption identity configuration.

Use this when you want to retrieves a client-side encryption identity configuration.
Key inputs: fields, user_id, cse_email_address."""
        tool = self._client.get_tool('gmail_users_settings_cse_identities_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsCseIdentitiesGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_cse_identities_list',
        title='UsersSettingsCseIdentitiesList',
        input_model=UsersSettingsCseIdentitiesListInput,
        output_model=UsersSettingsCseIdentitiesListOutput,
        tools_used=('gmail_users_settings_cse_identities_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: UsersSettingsCseIdentitiesListInput) -> UsersSettingsCseIdentitiesListOutput:
        """Lists the client-side encrypted identities for an authenticated user.

Use this when you want to lists the client-side encrypted identities for an authenticated user.
Key inputs: fields, user_id, page_size, page_token."""
        tool = self._client.get_tool('gmail_users_settings_cse_identities_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsCseIdentitiesListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_cse_identities_patch',
        title='UsersSettingsCseIdentitiesPatch',
        input_model=UsersSettingsCseIdentitiesPatchInput,
        output_model=UsersSettingsCseIdentitiesPatchOutput,
        tools_used=('gmail_users_settings_cse_identities_patch',),
        tags=tuple(['users']),
    )
    async def patch(self, data: UsersSettingsCseIdentitiesPatchInput) -> UsersSettingsCseIdentitiesPatchOutput:
        """Associates a different key pair with an existing client-side encryption identity. The updated key pair must validate against Google's [S/MIME certificate profiles](https://support.google.com/a/answer/7300887).

Use this when you want to associates a different key pair with an existing client-side encryption identity. The updated key pair must validate against Google's [S/MIME certificate profiles](https://support.google.com/a/answer/7300887).
Key inputs: fields, user_id, email_address, body."""
        tool = self._client.get_tool('gmail_users_settings_cse_identities_patch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsCseIdentitiesPatchOutput.model_validate(coerce_tool_result(result))
