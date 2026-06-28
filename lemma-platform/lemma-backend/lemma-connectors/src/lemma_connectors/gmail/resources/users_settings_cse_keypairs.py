from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsCseKeypairsCreateToolInput, GmailUsersSettingsCseKeypairsCreateToolOutput, GmailUsersSettingsCseKeypairsDisableToolInput, GmailUsersSettingsCseKeypairsDisableToolOutput, GmailUsersSettingsCseKeypairsEnableToolInput, GmailUsersSettingsCseKeypairsEnableToolOutput, GmailUsersSettingsCseKeypairsGetToolInput, GmailUsersSettingsCseKeypairsGetToolOutput, GmailUsersSettingsCseKeypairsListToolInput, GmailUsersSettingsCseKeypairsListToolOutput, GmailUsersSettingsCseKeypairsObliterateToolInput, GmailUsersSettingsCseKeypairsObliterateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersSettingsCseKeypairsCreateInput(GmailUsersSettingsCseKeypairsCreateToolInput):
    """Operation input for `users_settings_cse_keypairs_create`."""
    pass

class UsersSettingsCseKeypairsCreateOutput(GmailUsersSettingsCseKeypairsCreateToolOutput):
    """Operation output for `users_settings_cse_keypairs_create`."""
    pass

class UsersSettingsCseKeypairsDisableInput(GmailUsersSettingsCseKeypairsDisableToolInput):
    """Operation input for `users_settings_cse_keypairs_disable`."""
    pass

class UsersSettingsCseKeypairsDisableOutput(GmailUsersSettingsCseKeypairsDisableToolOutput):
    """Operation output for `users_settings_cse_keypairs_disable`."""
    pass

class UsersSettingsCseKeypairsEnableInput(GmailUsersSettingsCseKeypairsEnableToolInput):
    """Operation input for `users_settings_cse_keypairs_enable`."""
    pass

class UsersSettingsCseKeypairsEnableOutput(GmailUsersSettingsCseKeypairsEnableToolOutput):
    """Operation output for `users_settings_cse_keypairs_enable`."""
    pass

class UsersSettingsCseKeypairsGetInput(GmailUsersSettingsCseKeypairsGetToolInput):
    """Operation input for `users_settings_cse_keypairs_get`."""
    pass

class UsersSettingsCseKeypairsGetOutput(GmailUsersSettingsCseKeypairsGetToolOutput):
    """Operation output for `users_settings_cse_keypairs_get`."""
    pass

class UsersSettingsCseKeypairsListInput(GmailUsersSettingsCseKeypairsListToolInput):
    """Operation input for `users_settings_cse_keypairs_list`."""
    pass

class UsersSettingsCseKeypairsListOutput(GmailUsersSettingsCseKeypairsListToolOutput):
    """Operation output for `users_settings_cse_keypairs_list`."""
    pass

class UsersSettingsCseKeypairsObliterateInput(GmailUsersSettingsCseKeypairsObliterateToolInput):
    """Operation input for `users_settings_cse_keypairs_obliterate`."""
    pass

class UsersSettingsCseKeypairsObliterateOutput(GmailUsersSettingsCseKeypairsObliterateToolOutput):
    """Operation output for `users_settings_cse_keypairs_obliterate`."""
    pass

class GmailUsersSettingsCseKeypairsResource(BaseResourceClient):
    """Operations grouped around the `users_settings_cse_keypairs` resource."""

    @operation(
        name='users_settings_cse_keypairs_create',
        title='UsersSettingsCseKeypairsCreate',
        input_model=UsersSettingsCseKeypairsCreateInput,
        output_model=UsersSettingsCseKeypairsCreateOutput,
        tools_used=('gmail_users_settings_cse_keypairs_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: UsersSettingsCseKeypairsCreateInput) -> UsersSettingsCseKeypairsCreateOutput:
        """Creates and uploads a client-side encryption S/MIME public key certificate chain and private key metadata for the authenticated user.

Use this when you want to creates and uploads a client-side encryption S/MIME public key certificate chain and private key metadata for the authenticated user.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_settings_cse_keypairs_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsCseKeypairsCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_cse_keypairs_disable',
        title='UsersSettingsCseKeypairsDisable',
        input_model=UsersSettingsCseKeypairsDisableInput,
        output_model=UsersSettingsCseKeypairsDisableOutput,
        tools_used=('gmail_users_settings_cse_keypairs_disable',),
        tags=tuple(['users']),
    )
    async def disable(self, data: UsersSettingsCseKeypairsDisableInput) -> UsersSettingsCseKeypairsDisableOutput:
        """Turns off a client-side encryption key pair. The authenticated user can no longer use the key pair to decrypt incoming CSE message texts or sign outgoing CSE mail. To regain access, use the EnableCseKeyPair to turn on the key pair. After 30 days, you can permanently delete the key pair by using the ObliterateCseKeyPair method.

Use this when you want to turns off a client-side encryption key pair. The authenticated user can no longer use the key pair to decrypt incoming CSE message texts or sign outgoing CSE mail. To regain access, use the EnableCseKeyPair to turn on the key pair. After 30 days, you can permanently delete the key pair by using the ObliterateCseKeyPair method.
Key inputs: fields, user_id, key_pair_id, body."""
        tool = self._client.get_tool('gmail_users_settings_cse_keypairs_disable')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsCseKeypairsDisableOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_cse_keypairs_enable',
        title='UsersSettingsCseKeypairsEnable',
        input_model=UsersSettingsCseKeypairsEnableInput,
        output_model=UsersSettingsCseKeypairsEnableOutput,
        tools_used=('gmail_users_settings_cse_keypairs_enable',),
        tags=tuple(['users']),
    )
    async def enable(self, data: UsersSettingsCseKeypairsEnableInput) -> UsersSettingsCseKeypairsEnableOutput:
        """Turns on a client-side encryption key pair that was turned off. The key pair becomes active again for any associated client-side encryption identities.

Use this when you want to turns on a client-side encryption key pair that was turned off. The key pair becomes active again for any associated client-side encryption identities.
Key inputs: fields, user_id, key_pair_id, body."""
        tool = self._client.get_tool('gmail_users_settings_cse_keypairs_enable')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsCseKeypairsEnableOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_cse_keypairs_get',
        title='UsersSettingsCseKeypairsGet',
        input_model=UsersSettingsCseKeypairsGetInput,
        output_model=UsersSettingsCseKeypairsGetOutput,
        tools_used=('gmail_users_settings_cse_keypairs_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: UsersSettingsCseKeypairsGetInput) -> UsersSettingsCseKeypairsGetOutput:
        """Retrieves an existing client-side encryption key pair.

Use this when you want to retrieves an existing client-side encryption key pair.
Key inputs: fields, user_id, key_pair_id."""
        tool = self._client.get_tool('gmail_users_settings_cse_keypairs_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsCseKeypairsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_cse_keypairs_list',
        title='UsersSettingsCseKeypairsList',
        input_model=UsersSettingsCseKeypairsListInput,
        output_model=UsersSettingsCseKeypairsListOutput,
        tools_used=('gmail_users_settings_cse_keypairs_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: UsersSettingsCseKeypairsListInput) -> UsersSettingsCseKeypairsListOutput:
        """Lists client-side encryption key pairs for an authenticated user.

Use this when you want to lists client-side encryption key pairs for an authenticated user.
Key inputs: fields, user_id, page_size, page_token."""
        tool = self._client.get_tool('gmail_users_settings_cse_keypairs_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsCseKeypairsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_cse_keypairs_obliterate',
        title='UsersSettingsCseKeypairsObliterate',
        input_model=UsersSettingsCseKeypairsObliterateInput,
        output_model=UsersSettingsCseKeypairsObliterateOutput,
        tools_used=('gmail_users_settings_cse_keypairs_obliterate',),
        tags=tuple(['users']),
    )
    async def obliterate(self, data: UsersSettingsCseKeypairsObliterateInput) -> UsersSettingsCseKeypairsObliterateOutput:
        """Deletes a client-side encryption key pair permanently and immediately. You can only permanently delete key pairs that have been turned off for more than 30 days. To turn off a key pair, use the DisableCseKeyPair method. Gmail can't restore or decrypt any messages that were encrypted by an obliterated key. Authenticated users and Google Workspace administrators lose access to reading the encrypted messages.

Use this when you want to deletes a client-side encryption key pair permanently and immediately. You can only permanently delete key pairs that have been turned off for more than 30 days. To turn off a key pair, use the DisableCseKeyPair method. Gmail can't restore or decrypt any messages that were encrypted by an obliterated key. Authenticated users and Google Workspace administrators lose access to reading the encrypted messages.
Key inputs: fields, user_id, key_pair_id, body."""
        tool = self._client.get_tool('gmail_users_settings_cse_keypairs_obliterate')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsCseKeypairsObliterateOutput.model_validate(coerce_tool_result(result))
