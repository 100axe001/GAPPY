from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsSendAsCreateToolInput, GmailUsersSettingsSendAsCreateToolOutput, GmailUsersSettingsSendAsDeleteToolInput, GmailUsersSettingsSendAsDeleteToolOutput, GmailUsersSettingsSendAsGetToolInput, GmailUsersSettingsSendAsGetToolOutput, GmailUsersSettingsSendAsListToolInput, GmailUsersSettingsSendAsListToolOutput, GmailUsersSettingsSendAsPatchToolInput, GmailUsersSettingsSendAsPatchToolOutput, GmailUsersSettingsSendAsUpdateToolInput, GmailUsersSettingsSendAsUpdateToolOutput, GmailUsersSettingsSendAsVerifyToolInput, GmailUsersSettingsSendAsVerifyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SettingsSendAsCreateInput(GmailUsersSettingsSendAsCreateToolInput):
    """Operation input for `settings_send_as_create`."""
    pass

class SettingsSendAsCreateOutput(GmailUsersSettingsSendAsCreateToolOutput):
    """Operation output for `settings_send_as_create`."""
    pass

class SettingsSendAsDeleteInput(GmailUsersSettingsSendAsDeleteToolInput):
    """Operation input for `settings_send_as_delete`."""
    pass

class SettingsSendAsDeleteOutput(GmailUsersSettingsSendAsDeleteToolOutput):
    """Operation output for `settings_send_as_delete`."""
    pass

class SettingsSendAsGetInput(GmailUsersSettingsSendAsGetToolInput):
    """Operation input for `settings_send_as_get`."""
    pass

class SettingsSendAsGetOutput(GmailUsersSettingsSendAsGetToolOutput):
    """Operation output for `settings_send_as_get`."""
    pass

class SettingsSendAsListInput(GmailUsersSettingsSendAsListToolInput):
    """Operation input for `settings_send_as_list`."""
    pass

class SettingsSendAsListOutput(GmailUsersSettingsSendAsListToolOutput):
    """Operation output for `settings_send_as_list`."""
    pass

class SettingsSendAsPatchInput(GmailUsersSettingsSendAsPatchToolInput):
    """Operation input for `settings_send_as_patch`."""
    pass

class SettingsSendAsPatchOutput(GmailUsersSettingsSendAsPatchToolOutput):
    """Operation output for `settings_send_as_patch`."""
    pass

class SettingsSendAsUpdateInput(GmailUsersSettingsSendAsUpdateToolInput):
    """Operation input for `settings_send_as_update`."""
    pass

class SettingsSendAsUpdateOutput(GmailUsersSettingsSendAsUpdateToolOutput):
    """Operation output for `settings_send_as_update`."""
    pass

class SettingsSendAsVerifyInput(GmailUsersSettingsSendAsVerifyToolInput):
    """Operation input for `settings_send_as_verify`."""
    pass

class SettingsSendAsVerifyOutput(GmailUsersSettingsSendAsVerifyToolOutput):
    """Operation output for `settings_send_as_verify`."""
    pass

class GmailSettingsSendAsResource(BaseResourceClient):
    """Operations for the `settings_send_as` resource."""

    @operation(
        name='settings_send_as_create',
        title='SettingsSendAsCreate',
        input_model=SettingsSendAsCreateInput,
        output_model=SettingsSendAsCreateOutput,
        tools_used=('gmail_users_settings_send_as_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: SettingsSendAsCreateInput) -> SettingsSendAsCreateOutput:
        """Creates a custom "from" send-as alias. If an SMTP MSA is specified, Gmail will attempt to connect to the SMTP service to validate the configuration before creating the alias. If ownership verification is required for the alias, a message will be sent to the email address and the resource's verification status will be set to `pending`; otherwise, the resource will be created with verification status set to `accepted`. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias. This method is only available to service account clients that have been delegated domain-wide authority.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_settings_send_as_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsSendAsCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_send_as_delete',
        title='SettingsSendAsDelete',
        input_model=SettingsSendAsDeleteInput,
        output_model=SettingsSendAsDeleteOutput,
        tools_used=('gmail_users_settings_send_as_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: SettingsSendAsDeleteInput) -> SettingsSendAsDeleteOutput:
        """Deletes the specified send-as alias. Revokes any verification that may have been required for using it. This method is only available to service account clients that have been delegated domain-wide authority.

Important inputs: fields, user_id, send_as_email"""
        tool = self._client.get_tool('gmail_users_settings_send_as_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsSendAsDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_send_as_get',
        title='SettingsSendAsGet',
        input_model=SettingsSendAsGetInput,
        output_model=SettingsSendAsGetOutput,
        tools_used=('gmail_users_settings_send_as_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: SettingsSendAsGetInput) -> SettingsSendAsGetOutput:
        """Gets the specified send-as alias. Fails with an HTTP 404 error if the specified address is not a member of the collection.

Important inputs: fields, user_id, send_as_email"""
        tool = self._client.get_tool('gmail_users_settings_send_as_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsSendAsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_send_as_list',
        title='SettingsSendAsList',
        input_model=SettingsSendAsListInput,
        output_model=SettingsSendAsListOutput,
        tools_used=('gmail_users_settings_send_as_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: SettingsSendAsListInput) -> SettingsSendAsListOutput:
        """Lists the send-as aliases for the specified account. The result includes the primary send-as address associated with the account as well as any custom "from" aliases.

Important inputs: fields, user_id"""
        tool = self._client.get_tool('gmail_users_settings_send_as_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsSendAsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_send_as_patch',
        title='SettingsSendAsPatch',
        input_model=SettingsSendAsPatchInput,
        output_model=SettingsSendAsPatchOutput,
        tools_used=('gmail_users_settings_send_as_patch',),
        tags=tuple(['users']),
    )
    async def patch(self, data: SettingsSendAsPatchInput) -> SettingsSendAsPatchOutput:
        """Patch the specified send-as alias.

Important inputs: fields, user_id, send_as_email, body"""
        tool = self._client.get_tool('gmail_users_settings_send_as_patch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsSendAsPatchOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_send_as_update',
        title='SettingsSendAsUpdate',
        input_model=SettingsSendAsUpdateInput,
        output_model=SettingsSendAsUpdateOutput,
        tools_used=('gmail_users_settings_send_as_update',),
        tags=tuple(['users']),
    )
    async def update(self, data: SettingsSendAsUpdateInput) -> SettingsSendAsUpdateOutput:
        """Updates a send-as alias. If a signature is provided, Gmail will sanitize the HTML before saving it with the alias. Addresses other than the primary address for the account can only be updated by service account clients that have been delegated domain-wide authority.

Important inputs: fields, user_id, send_as_email, body"""
        tool = self._client.get_tool('gmail_users_settings_send_as_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsSendAsUpdateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_send_as_verify',
        title='SettingsSendAsVerify',
        input_model=SettingsSendAsVerifyInput,
        output_model=SettingsSendAsVerifyOutput,
        tools_used=('gmail_users_settings_send_as_verify',),
        tags=tuple(['users']),
    )
    async def verify(self, data: SettingsSendAsVerifyInput) -> SettingsSendAsVerifyOutput:
        """Sends a verification email to the specified send-as alias address. The verification status must be `pending`. This method is only available to service account clients that have been delegated domain-wide authority.

Important inputs: fields, user_id, send_as_email"""
        tool = self._client.get_tool('gmail_users_settings_send_as_verify')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsSendAsVerifyOutput.model_validate(coerce_tool_result(result))
