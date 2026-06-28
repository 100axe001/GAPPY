from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsSendAsCreateToolInput, GmailUsersSettingsSendAsCreateToolOutput, GmailUsersSettingsSendAsDeleteToolInput, GmailUsersSettingsSendAsDeleteToolOutput, GmailUsersSettingsSendAsGetToolInput, GmailUsersSettingsSendAsGetToolOutput, GmailUsersSettingsSendAsListToolInput, GmailUsersSettingsSendAsListToolOutput, GmailUsersSettingsSendAsPatchToolInput, GmailUsersSettingsSendAsPatchToolOutput, GmailUsersSettingsSendAsUpdateToolInput, GmailUsersSettingsSendAsUpdateToolOutput, GmailUsersSettingsSendAsVerifyToolInput, GmailUsersSettingsSendAsVerifyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersSettingsSendAsCreateInput(GmailUsersSettingsSendAsCreateToolInput):
    """Operation input for `users_settings_send_as_create`."""
    pass

class UsersSettingsSendAsCreateOutput(GmailUsersSettingsSendAsCreateToolOutput):
    """Operation output for `users_settings_send_as_create`."""
    pass

class UsersSettingsSendAsDeleteInput(GmailUsersSettingsSendAsDeleteToolInput):
    """Operation input for `users_settings_send_as_delete`."""
    pass

class UsersSettingsSendAsDeleteOutput(GmailUsersSettingsSendAsDeleteToolOutput):
    """Operation output for `users_settings_send_as_delete`."""
    pass

class UsersSettingsSendAsGetInput(GmailUsersSettingsSendAsGetToolInput):
    """Operation input for `users_settings_send_as_get`."""
    pass

class UsersSettingsSendAsGetOutput(GmailUsersSettingsSendAsGetToolOutput):
    """Operation output for `users_settings_send_as_get`."""
    pass

class UsersSettingsSendAsListInput(GmailUsersSettingsSendAsListToolInput):
    """Operation input for `users_settings_send_as_list`."""
    pass

class UsersSettingsSendAsListOutput(GmailUsersSettingsSendAsListToolOutput):
    """Operation output for `users_settings_send_as_list`."""
    pass

class UsersSettingsSendAsPatchInput(GmailUsersSettingsSendAsPatchToolInput):
    """Operation input for `users_settings_send_as_patch`."""
    pass

class UsersSettingsSendAsPatchOutput(GmailUsersSettingsSendAsPatchToolOutput):
    """Operation output for `users_settings_send_as_patch`."""
    pass

class UsersSettingsSendAsUpdateInput(GmailUsersSettingsSendAsUpdateToolInput):
    """Operation input for `users_settings_send_as_update`."""
    pass

class UsersSettingsSendAsUpdateOutput(GmailUsersSettingsSendAsUpdateToolOutput):
    """Operation output for `users_settings_send_as_update`."""
    pass

class UsersSettingsSendAsVerifyInput(GmailUsersSettingsSendAsVerifyToolInput):
    """Operation input for `users_settings_send_as_verify`."""
    pass

class UsersSettingsSendAsVerifyOutput(GmailUsersSettingsSendAsVerifyToolOutput):
    """Operation output for `users_settings_send_as_verify`."""
    pass

class GmailUsersSettingsSendAsResource(BaseResourceClient):
    """Operations grouped around the `users_settings_send_as` resource."""

    @operation(
        name='users_settings_send_as_create',
        title='UsersSettingsSendAsCreate',
        input_model=UsersSettingsSendAsCreateInput,
        output_model=UsersSettingsSendAsCreateOutput,
        tools_used=('gmail_users_settings_send_as_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: UsersSettingsSendAsCreateInput) -> UsersSettingsSendAsCreateOutput:
        """Creates a custom "from" send-as alias. If an SMTP MSA is specified, Gmail will attempt to connect to the SMTP service to validate the configuration before creating the alias. If ownership verification is required for the alias, a message will be sent to the email address and the resource's verification status will be set to `pending`; otherwise, the resource will be created with verification status set to `accepted`. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias. This method is only available to service account clients that have been delegated domain-wide authority.

Use this when you want to creates a custom "from" send-as alias. If an SMTP MSA is specified, Gmail will attempt to connect to the SMTP service to validate the configuration before creating the alias. If ownership verification is required for the alias, a message will be sent to the email address and the resource's verification status will be set to `pending`; otherwise, the resource will be created with verification status set to `accepted`. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias. This method is only available to service account clients that have been delegated domain-wide authority.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_settings_send_as_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsSendAsCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_send_as_delete',
        title='UsersSettingsSendAsDelete',
        input_model=UsersSettingsSendAsDeleteInput,
        output_model=UsersSettingsSendAsDeleteOutput,
        tools_used=('gmail_users_settings_send_as_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: UsersSettingsSendAsDeleteInput) -> UsersSettingsSendAsDeleteOutput:
        """Deletes the specified send-as alias. Revokes any verification that may have been required for using it. This method is only available to service account clients that have been delegated domain-wide authority.

Use this when you want to deletes the specified send-as alias. Revokes any verification that may have been required for using it. This method is only available to service account clients that have been delegated domain-wide authority.
Key inputs: fields, user_id, send_as_email."""
        tool = self._client.get_tool('gmail_users_settings_send_as_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsSendAsDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_send_as_get',
        title='UsersSettingsSendAsGet',
        input_model=UsersSettingsSendAsGetInput,
        output_model=UsersSettingsSendAsGetOutput,
        tools_used=('gmail_users_settings_send_as_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: UsersSettingsSendAsGetInput) -> UsersSettingsSendAsGetOutput:
        """Gets the specified send-as alias. Fails with an HTTP 404 error if the specified address is not a member of the collection.

Use this when you want to gets the specified send-as alias. Fails with an HTTP 404 error if the specified address is not a member of the collection.
Key inputs: fields, user_id, send_as_email."""
        tool = self._client.get_tool('gmail_users_settings_send_as_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsSendAsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_send_as_list',
        title='UsersSettingsSendAsList',
        input_model=UsersSettingsSendAsListInput,
        output_model=UsersSettingsSendAsListOutput,
        tools_used=('gmail_users_settings_send_as_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: UsersSettingsSendAsListInput) -> UsersSettingsSendAsListOutput:
        """Lists the send-as aliases for the specified account. The result includes the primary send-as address associated with the account as well as any custom "from" aliases.

Use this when you want to lists the send-as aliases for the specified account. The result includes the primary send-as address associated with the account as well as any custom "from" aliases.
Key inputs: fields, user_id."""
        tool = self._client.get_tool('gmail_users_settings_send_as_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsSendAsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_send_as_patch',
        title='UsersSettingsSendAsPatch',
        input_model=UsersSettingsSendAsPatchInput,
        output_model=UsersSettingsSendAsPatchOutput,
        tools_used=('gmail_users_settings_send_as_patch',),
        tags=tuple(['users']),
    )
    async def patch(self, data: UsersSettingsSendAsPatchInput) -> UsersSettingsSendAsPatchOutput:
        """Patch the specified send-as alias.

Use this when you want to patch the specified send-as alias.
Key inputs: fields, user_id, send_as_email, body."""
        tool = self._client.get_tool('gmail_users_settings_send_as_patch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsSendAsPatchOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_send_as_update',
        title='UsersSettingsSendAsUpdate',
        input_model=UsersSettingsSendAsUpdateInput,
        output_model=UsersSettingsSendAsUpdateOutput,
        tools_used=('gmail_users_settings_send_as_update',),
        tags=tuple(['users']),
    )
    async def update(self, data: UsersSettingsSendAsUpdateInput) -> UsersSettingsSendAsUpdateOutput:
        """Updates a send-as alias. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias. Addresses other than the primary address for the account can only be updated by service account clients that have been delegated domain-wide authority.

Use this when you want to updates a send-as alias. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias. Addresses other than the primary address for the account can only be updated by service account clients that have been delegated domain-wide authority.
Key inputs: fields, user_id, send_as_email, body."""
        tool = self._client.get_tool('gmail_users_settings_send_as_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsSendAsUpdateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_send_as_verify',
        title='UsersSettingsSendAsVerify',
        input_model=UsersSettingsSendAsVerifyInput,
        output_model=UsersSettingsSendAsVerifyOutput,
        tools_used=('gmail_users_settings_send_as_verify',),
        tags=tuple(['users']),
    )
    async def verify(self, data: UsersSettingsSendAsVerifyInput) -> UsersSettingsSendAsVerifyOutput:
        """Sends a verification email to the specified send-as alias address. The verification status must be `pending`. This method is only available to service account clients that have been delegated domain-wide authority.

Use this when you want to sends a verification email to the specified send-as alias address. The verification status must be `pending`. This method is only available to service account clients that have been delegated domain-wide authority.
Key inputs: fields, user_id, send_as_email."""
        tool = self._client.get_tool('gmail_users_settings_send_as_verify')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsSendAsVerifyOutput.model_validate(coerce_tool_result(result))
