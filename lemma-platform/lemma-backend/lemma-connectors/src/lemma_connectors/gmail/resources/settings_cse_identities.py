from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsCseIdentitiesCreateToolInput, GmailUsersSettingsCseIdentitiesCreateToolOutput, GmailUsersSettingsCseIdentitiesDeleteToolInput, GmailUsersSettingsCseIdentitiesDeleteToolOutput, GmailUsersSettingsCseIdentitiesGetToolInput, GmailUsersSettingsCseIdentitiesGetToolOutput, GmailUsersSettingsCseIdentitiesListToolInput, GmailUsersSettingsCseIdentitiesListToolOutput, GmailUsersSettingsCseIdentitiesPatchToolInput, GmailUsersSettingsCseIdentitiesPatchToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SettingsCseIdentitiesCreateInput(GmailUsersSettingsCseIdentitiesCreateToolInput):
    """Operation input for `settings_cse_identities_create`."""
    pass

class SettingsCseIdentitiesCreateOutput(GmailUsersSettingsCseIdentitiesCreateToolOutput):
    """Operation output for `settings_cse_identities_create`."""
    pass

class SettingsCseIdentitiesDeleteInput(GmailUsersSettingsCseIdentitiesDeleteToolInput):
    """Operation input for `settings_cse_identities_delete`."""
    pass

class SettingsCseIdentitiesDeleteOutput(GmailUsersSettingsCseIdentitiesDeleteToolOutput):
    """Operation output for `settings_cse_identities_delete`."""
    pass

class SettingsCseIdentitiesGetInput(GmailUsersSettingsCseIdentitiesGetToolInput):
    """Operation input for `settings_cse_identities_get`."""
    pass

class SettingsCseIdentitiesGetOutput(GmailUsersSettingsCseIdentitiesGetToolOutput):
    """Operation output for `settings_cse_identities_get`."""
    pass

class SettingsCseIdentitiesListInput(GmailUsersSettingsCseIdentitiesListToolInput):
    """Operation input for `settings_cse_identities_list`."""
    pass

class SettingsCseIdentitiesListOutput(GmailUsersSettingsCseIdentitiesListToolOutput):
    """Operation output for `settings_cse_identities_list`."""
    pass

class SettingsCseIdentitiesPatchInput(GmailUsersSettingsCseIdentitiesPatchToolInput):
    """Operation input for `settings_cse_identities_patch`."""
    pass

class SettingsCseIdentitiesPatchOutput(GmailUsersSettingsCseIdentitiesPatchToolOutput):
    """Operation output for `settings_cse_identities_patch`."""
    pass

class GmailSettingsCseIdentitiesResource(BaseResourceClient):
    """Operations for the `settings_cse_identities` resource."""

    @operation(
        name='settings_cse_identities_create',
        title='SettingsCseIdentitiesCreate',
        input_model=SettingsCseIdentitiesCreateInput,
        output_model=SettingsCseIdentitiesCreateOutput,
        tools_used=('gmail_users_settings_cse_identities_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: SettingsCseIdentitiesCreateInput) -> SettingsCseIdentitiesCreateOutput:
        """Creates and configures a client-side encryption identity that's authorized to send mail from the user account. Google publishes the S/MIME certificate to a shared domain-wide directory so that people within a Google Workspace organization can encrypt and send mail to the identity.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_settings_cse_identities_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsCseIdentitiesCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_cse_identities_delete',
        title='SettingsCseIdentitiesDelete',
        input_model=SettingsCseIdentitiesDeleteInput,
        output_model=SettingsCseIdentitiesDeleteOutput,
        tools_used=('gmail_users_settings_cse_identities_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: SettingsCseIdentitiesDeleteInput) -> SettingsCseIdentitiesDeleteOutput:
        """Deletes a client-side encryption identity. The authenticated user can no longer use the identity to send encrypted messages. You cannot restore the identity after you delete it. Instead, use the CreateCseIdentity method to create another identity with the same configuration.

Important inputs: fields, user_id, cse_email_address"""
        tool = self._client.get_tool('gmail_users_settings_cse_identities_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsCseIdentitiesDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_cse_identities_get',
        title='SettingsCseIdentitiesGet',
        input_model=SettingsCseIdentitiesGetInput,
        output_model=SettingsCseIdentitiesGetOutput,
        tools_used=('gmail_users_settings_cse_identities_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: SettingsCseIdentitiesGetInput) -> SettingsCseIdentitiesGetOutput:
        """Retrieves a client-side encryption identity configuration.

Important inputs: fields, user_id, cse_email_address"""
        tool = self._client.get_tool('gmail_users_settings_cse_identities_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsCseIdentitiesGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_cse_identities_list',
        title='SettingsCseIdentitiesList',
        input_model=SettingsCseIdentitiesListInput,
        output_model=SettingsCseIdentitiesListOutput,
        tools_used=('gmail_users_settings_cse_identities_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: SettingsCseIdentitiesListInput) -> SettingsCseIdentitiesListOutput:
        """Lists the client-side encrypted identities for an authenticated user.

Important inputs: fields, user_id, page_size, page_token"""
        tool = self._client.get_tool('gmail_users_settings_cse_identities_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsCseIdentitiesListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_cse_identities_patch',
        title='SettingsCseIdentitiesPatch',
        input_model=SettingsCseIdentitiesPatchInput,
        output_model=SettingsCseIdentitiesPatchOutput,
        tools_used=('gmail_users_settings_cse_identities_patch',),
        tags=tuple(['users']),
    )
    async def patch(self, data: SettingsCseIdentitiesPatchInput) -> SettingsCseIdentitiesPatchOutput:
        """Associates a different key pair with an existing client-side encryption identity. The updated key pair must validate against Google's [S/MIME certificate profiles](https://support.google.com/a/answer/7300887).

Important inputs: fields, user_id, email_address, body"""
        tool = self._client.get_tool('gmail_users_settings_cse_identities_patch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsCseIdentitiesPatchOutput.model_validate(coerce_tool_result(result))
