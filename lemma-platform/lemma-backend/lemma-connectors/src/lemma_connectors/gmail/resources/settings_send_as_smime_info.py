from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsSendAsSmimeInfoDeleteToolInput, GmailUsersSettingsSendAsSmimeInfoDeleteToolOutput, GmailUsersSettingsSendAsSmimeInfoGetToolInput, GmailUsersSettingsSendAsSmimeInfoGetToolOutput, GmailUsersSettingsSendAsSmimeInfoInsertToolInput, GmailUsersSettingsSendAsSmimeInfoInsertToolOutput, GmailUsersSettingsSendAsSmimeInfoListToolInput, GmailUsersSettingsSendAsSmimeInfoListToolOutput, GmailUsersSettingsSendAsSmimeInfoSetDefaultToolInput, GmailUsersSettingsSendAsSmimeInfoSetDefaultToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SettingsSendAsSmimeInfoDeleteInput(GmailUsersSettingsSendAsSmimeInfoDeleteToolInput):
    """Operation input for `settings_send_as_smime_info_delete`."""
    pass

class SettingsSendAsSmimeInfoDeleteOutput(GmailUsersSettingsSendAsSmimeInfoDeleteToolOutput):
    """Operation output for `settings_send_as_smime_info_delete`."""
    pass

class SettingsSendAsSmimeInfoGetInput(GmailUsersSettingsSendAsSmimeInfoGetToolInput):
    """Operation input for `settings_send_as_smime_info_get`."""
    pass

class SettingsSendAsSmimeInfoGetOutput(GmailUsersSettingsSendAsSmimeInfoGetToolOutput):
    """Operation output for `settings_send_as_smime_info_get`."""
    pass

class SettingsSendAsSmimeInfoInsertInput(GmailUsersSettingsSendAsSmimeInfoInsertToolInput):
    """Operation input for `settings_send_as_smime_info_insert`."""
    pass

class SettingsSendAsSmimeInfoInsertOutput(GmailUsersSettingsSendAsSmimeInfoInsertToolOutput):
    """Operation output for `settings_send_as_smime_info_insert`."""
    pass

class SettingsSendAsSmimeInfoListInput(GmailUsersSettingsSendAsSmimeInfoListToolInput):
    """Operation input for `settings_send_as_smime_info_list`."""
    pass

class SettingsSendAsSmimeInfoListOutput(GmailUsersSettingsSendAsSmimeInfoListToolOutput):
    """Operation output for `settings_send_as_smime_info_list`."""
    pass

class SettingsSendAsSmimeInfoSetDefaultInput(GmailUsersSettingsSendAsSmimeInfoSetDefaultToolInput):
    """Operation input for `settings_send_as_smime_info_set_default`."""
    pass

class SettingsSendAsSmimeInfoSetDefaultOutput(GmailUsersSettingsSendAsSmimeInfoSetDefaultToolOutput):
    """Operation output for `settings_send_as_smime_info_set_default`."""
    pass

class GmailSettingsSendAsSmimeInfoResource(BaseResourceClient):
    """Operations for the `settings_send_as_smime_info` resource."""

    @operation(
        name='settings_send_as_smime_info_delete',
        title='SettingsSendAsSmimeInfoDelete',
        input_model=SettingsSendAsSmimeInfoDeleteInput,
        output_model=SettingsSendAsSmimeInfoDeleteOutput,
        tools_used=('gmail_users_settings_send_as_smime_info_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: SettingsSendAsSmimeInfoDeleteInput) -> SettingsSendAsSmimeInfoDeleteOutput:
        """Deletes the specified S/MIME config for the specified send-as alias.

Important inputs: fields, user_id, send_as_email, id"""
        tool = self._client.get_tool('gmail_users_settings_send_as_smime_info_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsSendAsSmimeInfoDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_send_as_smime_info_get',
        title='SettingsSendAsSmimeInfoGet',
        input_model=SettingsSendAsSmimeInfoGetInput,
        output_model=SettingsSendAsSmimeInfoGetOutput,
        tools_used=('gmail_users_settings_send_as_smime_info_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: SettingsSendAsSmimeInfoGetInput) -> SettingsSendAsSmimeInfoGetOutput:
        """Gets the specified S/MIME config for the specified send-as alias.

Important inputs: fields, user_id, send_as_email, id"""
        tool = self._client.get_tool('gmail_users_settings_send_as_smime_info_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsSendAsSmimeInfoGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_send_as_smime_info_insert',
        title='SettingsSendAsSmimeInfoInsert',
        input_model=SettingsSendAsSmimeInfoInsertInput,
        output_model=SettingsSendAsSmimeInfoInsertOutput,
        tools_used=('gmail_users_settings_send_as_smime_info_insert',),
        tags=tuple(['users']),
    )
    async def insert(self, data: SettingsSendAsSmimeInfoInsertInput) -> SettingsSendAsSmimeInfoInsertOutput:
        """Insert (upload) the given S/MIME config for the specified send-as alias. Note that pkcs12 format is required for the key.

Important inputs: fields, user_id, send_as_email, body"""
        tool = self._client.get_tool('gmail_users_settings_send_as_smime_info_insert')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsSendAsSmimeInfoInsertOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_send_as_smime_info_list',
        title='SettingsSendAsSmimeInfoList',
        input_model=SettingsSendAsSmimeInfoListInput,
        output_model=SettingsSendAsSmimeInfoListOutput,
        tools_used=('gmail_users_settings_send_as_smime_info_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: SettingsSendAsSmimeInfoListInput) -> SettingsSendAsSmimeInfoListOutput:
        """Lists S/MIME configs for the specified send-as alias.

Important inputs: fields, user_id, send_as_email"""
        tool = self._client.get_tool('gmail_users_settings_send_as_smime_info_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsSendAsSmimeInfoListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_send_as_smime_info_set_default',
        title='SettingsSendAsSmimeInfoSetDefault',
        input_model=SettingsSendAsSmimeInfoSetDefaultInput,
        output_model=SettingsSendAsSmimeInfoSetDefaultOutput,
        tools_used=('gmail_users_settings_send_as_smime_info_set_default',),
        tags=tuple(['users']),
    )
    async def set_default(self, data: SettingsSendAsSmimeInfoSetDefaultInput) -> SettingsSendAsSmimeInfoSetDefaultOutput:
        """Sets the default S/MIME config for the specified send-as alias.

Important inputs: fields, user_id, send_as_email, id"""
        tool = self._client.get_tool('gmail_users_settings_send_as_smime_info_set_default')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsSendAsSmimeInfoSetDefaultOutput.model_validate(coerce_tool_result(result))
