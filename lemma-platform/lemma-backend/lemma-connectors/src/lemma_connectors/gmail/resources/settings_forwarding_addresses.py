from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsForwardingAddressesCreateToolInput, GmailUsersSettingsForwardingAddressesCreateToolOutput, GmailUsersSettingsForwardingAddressesDeleteToolInput, GmailUsersSettingsForwardingAddressesDeleteToolOutput, GmailUsersSettingsForwardingAddressesGetToolInput, GmailUsersSettingsForwardingAddressesGetToolOutput, GmailUsersSettingsForwardingAddressesListToolInput, GmailUsersSettingsForwardingAddressesListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SettingsForwardingAddressesCreateInput(GmailUsersSettingsForwardingAddressesCreateToolInput):
    """Operation input for `settings_forwarding_addresses_create`."""
    pass

class SettingsForwardingAddressesCreateOutput(GmailUsersSettingsForwardingAddressesCreateToolOutput):
    """Operation output for `settings_forwarding_addresses_create`."""
    pass

class SettingsForwardingAddressesDeleteInput(GmailUsersSettingsForwardingAddressesDeleteToolInput):
    """Operation input for `settings_forwarding_addresses_delete`."""
    pass

class SettingsForwardingAddressesDeleteOutput(GmailUsersSettingsForwardingAddressesDeleteToolOutput):
    """Operation output for `settings_forwarding_addresses_delete`."""
    pass

class SettingsForwardingAddressesGetInput(GmailUsersSettingsForwardingAddressesGetToolInput):
    """Operation input for `settings_forwarding_addresses_get`."""
    pass

class SettingsForwardingAddressesGetOutput(GmailUsersSettingsForwardingAddressesGetToolOutput):
    """Operation output for `settings_forwarding_addresses_get`."""
    pass

class SettingsForwardingAddressesListInput(GmailUsersSettingsForwardingAddressesListToolInput):
    """Operation input for `settings_forwarding_addresses_list`."""
    pass

class SettingsForwardingAddressesListOutput(GmailUsersSettingsForwardingAddressesListToolOutput):
    """Operation output for `settings_forwarding_addresses_list`."""
    pass

class GmailSettingsForwardingAddressesResource(BaseResourceClient):
    """Operations for the `settings_forwarding_addresses` resource."""

    @operation(
        name='settings_forwarding_addresses_create',
        title='SettingsForwardingAddressesCreate',
        input_model=SettingsForwardingAddressesCreateInput,
        output_model=SettingsForwardingAddressesCreateOutput,
        tools_used=('gmail_users_settings_forwarding_addresses_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: SettingsForwardingAddressesCreateInput) -> SettingsForwardingAddressesCreateOutput:
        """Creates a forwarding address. If ownership verification is required, a message will be sent to the recipient and the resource's verification status will be set to `pending`; otherwise, the resource will be created with verification status set to `accepted`. This method is only available to service account clients that have been delegated domain-wide authority.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_settings_forwarding_addresses_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsForwardingAddressesCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_forwarding_addresses_delete',
        title='SettingsForwardingAddressesDelete',
        input_model=SettingsForwardingAddressesDeleteInput,
        output_model=SettingsForwardingAddressesDeleteOutput,
        tools_used=('gmail_users_settings_forwarding_addresses_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: SettingsForwardingAddressesDeleteInput) -> SettingsForwardingAddressesDeleteOutput:
        """Deletes the specified forwarding address and revokes any verification that may have been required. This method is only available to service account clients that have been delegated domain-wide authority.

Important inputs: fields, user_id, forwarding_email"""
        tool = self._client.get_tool('gmail_users_settings_forwarding_addresses_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsForwardingAddressesDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_forwarding_addresses_get',
        title='SettingsForwardingAddressesGet',
        input_model=SettingsForwardingAddressesGetInput,
        output_model=SettingsForwardingAddressesGetOutput,
        tools_used=('gmail_users_settings_forwarding_addresses_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: SettingsForwardingAddressesGetInput) -> SettingsForwardingAddressesGetOutput:
        """Gets the specified forwarding address.

Important inputs: fields, user_id, forwarding_email"""
        tool = self._client.get_tool('gmail_users_settings_forwarding_addresses_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsForwardingAddressesGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_forwarding_addresses_list',
        title='SettingsForwardingAddressesList',
        input_model=SettingsForwardingAddressesListInput,
        output_model=SettingsForwardingAddressesListOutput,
        tools_used=('gmail_users_settings_forwarding_addresses_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: SettingsForwardingAddressesListInput) -> SettingsForwardingAddressesListOutput:
        """Lists the forwarding addresses for the specified account.

Important inputs: fields, user_id"""
        tool = self._client.get_tool('gmail_users_settings_forwarding_addresses_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsForwardingAddressesListOutput.model_validate(coerce_tool_result(result))
