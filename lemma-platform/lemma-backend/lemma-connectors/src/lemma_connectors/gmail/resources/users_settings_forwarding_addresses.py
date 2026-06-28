from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsForwardingAddressesCreateToolInput, GmailUsersSettingsForwardingAddressesCreateToolOutput, GmailUsersSettingsForwardingAddressesDeleteToolInput, GmailUsersSettingsForwardingAddressesDeleteToolOutput, GmailUsersSettingsForwardingAddressesGetToolInput, GmailUsersSettingsForwardingAddressesGetToolOutput, GmailUsersSettingsForwardingAddressesListToolInput, GmailUsersSettingsForwardingAddressesListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersSettingsForwardingAddressesCreateInput(GmailUsersSettingsForwardingAddressesCreateToolInput):
    """Operation input for `users_settings_forwarding_addresses_create`."""
    pass

class UsersSettingsForwardingAddressesCreateOutput(GmailUsersSettingsForwardingAddressesCreateToolOutput):
    """Operation output for `users_settings_forwarding_addresses_create`."""
    pass

class UsersSettingsForwardingAddressesDeleteInput(GmailUsersSettingsForwardingAddressesDeleteToolInput):
    """Operation input for `users_settings_forwarding_addresses_delete`."""
    pass

class UsersSettingsForwardingAddressesDeleteOutput(GmailUsersSettingsForwardingAddressesDeleteToolOutput):
    """Operation output for `users_settings_forwarding_addresses_delete`."""
    pass

class UsersSettingsForwardingAddressesGetInput(GmailUsersSettingsForwardingAddressesGetToolInput):
    """Operation input for `users_settings_forwarding_addresses_get`."""
    pass

class UsersSettingsForwardingAddressesGetOutput(GmailUsersSettingsForwardingAddressesGetToolOutput):
    """Operation output for `users_settings_forwarding_addresses_get`."""
    pass

class UsersSettingsForwardingAddressesListInput(GmailUsersSettingsForwardingAddressesListToolInput):
    """Operation input for `users_settings_forwarding_addresses_list`."""
    pass

class UsersSettingsForwardingAddressesListOutput(GmailUsersSettingsForwardingAddressesListToolOutput):
    """Operation output for `users_settings_forwarding_addresses_list`."""
    pass

class GmailUsersSettingsForwardingAddressesResource(BaseResourceClient):
    """Operations grouped around the `users_settings_forwarding_addresses` resource."""

    @operation(
        name='users_settings_forwarding_addresses_create',
        title='UsersSettingsForwardingAddressesCreate',
        input_model=UsersSettingsForwardingAddressesCreateInput,
        output_model=UsersSettingsForwardingAddressesCreateOutput,
        tools_used=('gmail_users_settings_forwarding_addresses_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: UsersSettingsForwardingAddressesCreateInput) -> UsersSettingsForwardingAddressesCreateOutput:
        """Creates a forwarding address. If ownership verification is required, a message will be sent to the recipient and the resource's verification status will be set to `pending`; otherwise, the resource will be created with verification status set to `accepted`. This method is only available to service account clients that have been delegated domain-wide authority.

Use this when you want to creates a forwarding address. If ownership verification is required, a message will be sent to the recipient and the resource's verification status will be set to `pending`; otherwise, the resource will be created with verification status set to `accepted`. This method is only available to service account clients that have been delegated domain-wide authority.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_settings_forwarding_addresses_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsForwardingAddressesCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_forwarding_addresses_delete',
        title='UsersSettingsForwardingAddressesDelete',
        input_model=UsersSettingsForwardingAddressesDeleteInput,
        output_model=UsersSettingsForwardingAddressesDeleteOutput,
        tools_used=('gmail_users_settings_forwarding_addresses_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: UsersSettingsForwardingAddressesDeleteInput) -> UsersSettingsForwardingAddressesDeleteOutput:
        """Deletes the specified forwarding address and revokes any verification that may have been required. This method is only available to service account clients that have been delegated domain-wide authority.

Use this when you want to deletes the specified forwarding address and revokes any verification that may have been required. This method is only available to service account clients that have been delegated domain-wide authority.
Key inputs: fields, user_id, forwarding_email."""
        tool = self._client.get_tool('gmail_users_settings_forwarding_addresses_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsForwardingAddressesDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_forwarding_addresses_get',
        title='UsersSettingsForwardingAddressesGet',
        input_model=UsersSettingsForwardingAddressesGetInput,
        output_model=UsersSettingsForwardingAddressesGetOutput,
        tools_used=('gmail_users_settings_forwarding_addresses_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: UsersSettingsForwardingAddressesGetInput) -> UsersSettingsForwardingAddressesGetOutput:
        """Gets the specified forwarding address.

Use this when you want to gets the specified forwarding address.
Key inputs: fields, user_id, forwarding_email."""
        tool = self._client.get_tool('gmail_users_settings_forwarding_addresses_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsForwardingAddressesGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_forwarding_addresses_list',
        title='UsersSettingsForwardingAddressesList',
        input_model=UsersSettingsForwardingAddressesListInput,
        output_model=UsersSettingsForwardingAddressesListOutput,
        tools_used=('gmail_users_settings_forwarding_addresses_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: UsersSettingsForwardingAddressesListInput) -> UsersSettingsForwardingAddressesListOutput:
        """Lists the forwarding addresses for the specified account.

Use this when you want to lists the forwarding addresses for the specified account.
Key inputs: fields, user_id."""
        tool = self._client.get_tool('gmail_users_settings_forwarding_addresses_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsForwardingAddressesListOutput.model_validate(coerce_tool_result(result))
