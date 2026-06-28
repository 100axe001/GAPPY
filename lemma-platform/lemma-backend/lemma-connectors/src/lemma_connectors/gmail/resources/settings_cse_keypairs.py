from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsCseKeypairsCreateToolInput, GmailUsersSettingsCseKeypairsCreateToolOutput, GmailUsersSettingsCseKeypairsDisableToolInput, GmailUsersSettingsCseKeypairsDisableToolOutput, GmailUsersSettingsCseKeypairsEnableToolInput, GmailUsersSettingsCseKeypairsEnableToolOutput, GmailUsersSettingsCseKeypairsGetToolInput, GmailUsersSettingsCseKeypairsGetToolOutput, GmailUsersSettingsCseKeypairsListToolInput, GmailUsersSettingsCseKeypairsListToolOutput, GmailUsersSettingsCseKeypairsObliterateToolInput, GmailUsersSettingsCseKeypairsObliterateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SettingsCseKeypairsCreateInput(GmailUsersSettingsCseKeypairsCreateToolInput):
    """Operation input for `settings_cse_keypairs_create`."""
    pass

class SettingsCseKeypairsCreateOutput(GmailUsersSettingsCseKeypairsCreateToolOutput):
    """Operation output for `settings_cse_keypairs_create`."""
    pass

class SettingsCseKeypairsDisableInput(GmailUsersSettingsCseKeypairsDisableToolInput):
    """Operation input for `settings_cse_keypairs_disable`."""
    pass

class SettingsCseKeypairsDisableOutput(GmailUsersSettingsCseKeypairsDisableToolOutput):
    """Operation output for `settings_cse_keypairs_disable`."""
    pass

class SettingsCseKeypairsEnableInput(GmailUsersSettingsCseKeypairsEnableToolInput):
    """Operation input for `settings_cse_keypairs_enable`."""
    pass

class SettingsCseKeypairsEnableOutput(GmailUsersSettingsCseKeypairsEnableToolOutput):
    """Operation output for `settings_cse_keypairs_enable`."""
    pass

class SettingsCseKeypairsGetInput(GmailUsersSettingsCseKeypairsGetToolInput):
    """Operation input for `settings_cse_keypairs_get`."""
    pass

class SettingsCseKeypairsGetOutput(GmailUsersSettingsCseKeypairsGetToolOutput):
    """Operation output for `settings_cse_keypairs_get`."""
    pass

class SettingsCseKeypairsListInput(GmailUsersSettingsCseKeypairsListToolInput):
    """Operation input for `settings_cse_keypairs_list`."""
    pass

class SettingsCseKeypairsListOutput(GmailUsersSettingsCseKeypairsListToolOutput):
    """Operation output for `settings_cse_keypairs_list`."""
    pass

class SettingsCseKeypairsObliterateInput(GmailUsersSettingsCseKeypairsObliterateToolInput):
    """Operation input for `settings_cse_keypairs_obliterate`."""
    pass

class SettingsCseKeypairsObliterateOutput(GmailUsersSettingsCseKeypairsObliterateToolOutput):
    """Operation output for `settings_cse_keypairs_obliterate`."""
    pass

class GmailSettingsCseKeypairsResource(BaseResourceClient):
    """Operations for the `settings_cse_keypairs` resource."""

    @operation(
        name='settings_cse_keypairs_create',
        title='SettingsCseKeypairsCreate',
        input_model=SettingsCseKeypairsCreateInput,
        output_model=SettingsCseKeypairsCreateOutput,
        tools_used=('gmail_users_settings_cse_keypairs_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: SettingsCseKeypairsCreateInput) -> SettingsCseKeypairsCreateOutput:
        """Creates and uploads a client-side encryption S/MIME public key certificate chain and private key metadata for the authenticated user.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_settings_cse_keypairs_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsCseKeypairsCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_cse_keypairs_disable',
        title='SettingsCseKeypairsDisable',
        input_model=SettingsCseKeypairsDisableInput,
        output_model=SettingsCseKeypairsDisableOutput,
        tools_used=('gmail_users_settings_cse_keypairs_disable',),
        tags=tuple(['users']),
    )
    async def disable(self, data: SettingsCseKeypairsDisableInput) -> SettingsCseKeypairsDisableOutput:
        """Turns off a client-side encryption key pair. The authenticated user can no longer use the key pair to decrypt incoming CSE message texts or sign outgoing CSE mail. To regain access, use the EnableCseKeyPair to turn on the key pair. After 30 days, you can permanently delete the key pair by using the ObliterateCseKeyPair method.

Important inputs: fields, user_id, key_pair_id, body"""
        tool = self._client.get_tool('gmail_users_settings_cse_keypairs_disable')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsCseKeypairsDisableOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_cse_keypairs_enable',
        title='SettingsCseKeypairsEnable',
        input_model=SettingsCseKeypairsEnableInput,
        output_model=SettingsCseKeypairsEnableOutput,
        tools_used=('gmail_users_settings_cse_keypairs_enable',),
        tags=tuple(['users']),
    )
    async def enable(self, data: SettingsCseKeypairsEnableInput) -> SettingsCseKeypairsEnableOutput:
        """Turns on a client-side encryption key pair that was turned off. The key pair becomes active again for any associated client-side encryption identities.

Important inputs: fields, user_id, key_pair_id, body"""
        tool = self._client.get_tool('gmail_users_settings_cse_keypairs_enable')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsCseKeypairsEnableOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_cse_keypairs_get',
        title='SettingsCseKeypairsGet',
        input_model=SettingsCseKeypairsGetInput,
        output_model=SettingsCseKeypairsGetOutput,
        tools_used=('gmail_users_settings_cse_keypairs_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: SettingsCseKeypairsGetInput) -> SettingsCseKeypairsGetOutput:
        """Retrieves an existing client-side encryption key pair.

Important inputs: fields, user_id, key_pair_id"""
        tool = self._client.get_tool('gmail_users_settings_cse_keypairs_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsCseKeypairsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_cse_keypairs_list',
        title='SettingsCseKeypairsList',
        input_model=SettingsCseKeypairsListInput,
        output_model=SettingsCseKeypairsListOutput,
        tools_used=('gmail_users_settings_cse_keypairs_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: SettingsCseKeypairsListInput) -> SettingsCseKeypairsListOutput:
        """Lists client-side encryption key pairs for an authenticated user.

Important inputs: fields, user_id, page_size, page_token"""
        tool = self._client.get_tool('gmail_users_settings_cse_keypairs_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsCseKeypairsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_cse_keypairs_obliterate',
        title='SettingsCseKeypairsObliterate',
        input_model=SettingsCseKeypairsObliterateInput,
        output_model=SettingsCseKeypairsObliterateOutput,
        tools_used=('gmail_users_settings_cse_keypairs_obliterate',),
        tags=tuple(['users']),
    )
    async def obliterate(self, data: SettingsCseKeypairsObliterateInput) -> SettingsCseKeypairsObliterateOutput:
        """Deletes a client-side encryption key pair permanently and immediately. You can only permanently delete key pairs that have been turned off for more than 30 days. To turn off a key pair, use the DisableCseKeyPair method. Gmail can't restore or decrypt any messages that were encrypted by an obliterated key. Authenticated users and Google Workspace administrators lose access to reading the encrypted messages.

Important inputs: fields, user_id, key_pair_id, body"""
        tool = self._client.get_tool('gmail_users_settings_cse_keypairs_obliterate')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsCseKeypairsObliterateOutput.model_validate(coerce_tool_result(result))
