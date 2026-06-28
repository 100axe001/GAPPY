from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsSendAsSmimeInfoDeleteToolInput, GmailUsersSettingsSendAsSmimeInfoDeleteToolOutput, GmailUsersSettingsSendAsSmimeInfoGetToolInput, GmailUsersSettingsSendAsSmimeInfoGetToolOutput, GmailUsersSettingsSendAsSmimeInfoInsertToolInput, GmailUsersSettingsSendAsSmimeInfoInsertToolOutput, GmailUsersSettingsSendAsSmimeInfoListToolInput, GmailUsersSettingsSendAsSmimeInfoListToolOutput, GmailUsersSettingsSendAsSmimeInfoSetDefaultToolInput, GmailUsersSettingsSendAsSmimeInfoSetDefaultToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersSettingsSendAsSmimeInfoDeleteInput(GmailUsersSettingsSendAsSmimeInfoDeleteToolInput):
    """Operation input for `users_settings_send_as_smime_info_delete`."""
    pass

class UsersSettingsSendAsSmimeInfoDeleteOutput(GmailUsersSettingsSendAsSmimeInfoDeleteToolOutput):
    """Operation output for `users_settings_send_as_smime_info_delete`."""
    pass

class UsersSettingsSendAsSmimeInfoGetInput(GmailUsersSettingsSendAsSmimeInfoGetToolInput):
    """Operation input for `users_settings_send_as_smime_info_get`."""
    pass

class UsersSettingsSendAsSmimeInfoGetOutput(GmailUsersSettingsSendAsSmimeInfoGetToolOutput):
    """Operation output for `users_settings_send_as_smime_info_get`."""
    pass

class UsersSettingsSendAsSmimeInfoInsertInput(GmailUsersSettingsSendAsSmimeInfoInsertToolInput):
    """Operation input for `users_settings_send_as_smime_info_insert`."""
    pass

class UsersSettingsSendAsSmimeInfoInsertOutput(GmailUsersSettingsSendAsSmimeInfoInsertToolOutput):
    """Operation output for `users_settings_send_as_smime_info_insert`."""
    pass

class UsersSettingsSendAsSmimeInfoListInput(GmailUsersSettingsSendAsSmimeInfoListToolInput):
    """Operation input for `users_settings_send_as_smime_info_list`."""
    pass

class UsersSettingsSendAsSmimeInfoListOutput(GmailUsersSettingsSendAsSmimeInfoListToolOutput):
    """Operation output for `users_settings_send_as_smime_info_list`."""
    pass

class UsersSettingsSendAsSmimeInfoSetDefaultInput(GmailUsersSettingsSendAsSmimeInfoSetDefaultToolInput):
    """Operation input for `users_settings_send_as_smime_info_set_default`."""
    pass

class UsersSettingsSendAsSmimeInfoSetDefaultOutput(GmailUsersSettingsSendAsSmimeInfoSetDefaultToolOutput):
    """Operation output for `users_settings_send_as_smime_info_set_default`."""
    pass

class GmailUsersSettingsSendAsSmimeInfoResource(BaseResourceClient):
    """Operations grouped around the `users_settings_send_as_smime_info` resource."""

    @operation(
        name='users_settings_send_as_smime_info_delete',
        title='UsersSettingsSendAsSmimeInfoDelete',
        input_model=UsersSettingsSendAsSmimeInfoDeleteInput,
        output_model=UsersSettingsSendAsSmimeInfoDeleteOutput,
        tools_used=('gmail_users_settings_send_as_smime_info_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: UsersSettingsSendAsSmimeInfoDeleteInput) -> UsersSettingsSendAsSmimeInfoDeleteOutput:
        """Deletes the specified S/MIME config for the specified send-as alias.

Use this when you want to deletes the specified S/MIME config for the specified send-as alias.
Key inputs: fields, user_id, send_as_email, id."""
        tool = self._client.get_tool('gmail_users_settings_send_as_smime_info_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsSendAsSmimeInfoDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_send_as_smime_info_get',
        title='UsersSettingsSendAsSmimeInfoGet',
        input_model=UsersSettingsSendAsSmimeInfoGetInput,
        output_model=UsersSettingsSendAsSmimeInfoGetOutput,
        tools_used=('gmail_users_settings_send_as_smime_info_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: UsersSettingsSendAsSmimeInfoGetInput) -> UsersSettingsSendAsSmimeInfoGetOutput:
        """Gets the specified S/MIME config for the specified send-as alias.

Use this when you want to gets the specified S/MIME config for the specified send-as alias.
Key inputs: fields, user_id, send_as_email, id."""
        tool = self._client.get_tool('gmail_users_settings_send_as_smime_info_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsSendAsSmimeInfoGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_send_as_smime_info_insert',
        title='UsersSettingsSendAsSmimeInfoInsert',
        input_model=UsersSettingsSendAsSmimeInfoInsertInput,
        output_model=UsersSettingsSendAsSmimeInfoInsertOutput,
        tools_used=('gmail_users_settings_send_as_smime_info_insert',),
        tags=tuple(['users']),
    )
    async def insert(self, data: UsersSettingsSendAsSmimeInfoInsertInput) -> UsersSettingsSendAsSmimeInfoInsertOutput:
        """Insert (upload) the given S/MIME config for the specified send-as alias. Note that pkcs12 format is required for the key.

Use this when you want to insert (upload) the given S/MIME config for the specified send-as alias. Note that pkcs12 format is required for the key.
Key inputs: fields, user_id, send_as_email, body."""
        tool = self._client.get_tool('gmail_users_settings_send_as_smime_info_insert')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsSendAsSmimeInfoInsertOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_send_as_smime_info_list',
        title='UsersSettingsSendAsSmimeInfoList',
        input_model=UsersSettingsSendAsSmimeInfoListInput,
        output_model=UsersSettingsSendAsSmimeInfoListOutput,
        tools_used=('gmail_users_settings_send_as_smime_info_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: UsersSettingsSendAsSmimeInfoListInput) -> UsersSettingsSendAsSmimeInfoListOutput:
        """Lists S/MIME configs for the specified send-as alias.

Use this when you want to lists S/MIME configs for the specified send-as alias.
Key inputs: fields, user_id, send_as_email."""
        tool = self._client.get_tool('gmail_users_settings_send_as_smime_info_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsSendAsSmimeInfoListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_send_as_smime_info_set_default',
        title='UsersSettingsSendAsSmimeInfoSetDefault',
        input_model=UsersSettingsSendAsSmimeInfoSetDefaultInput,
        output_model=UsersSettingsSendAsSmimeInfoSetDefaultOutput,
        tools_used=('gmail_users_settings_send_as_smime_info_set_default',),
        tags=tuple(['users']),
    )
    async def set_default(self, data: UsersSettingsSendAsSmimeInfoSetDefaultInput) -> UsersSettingsSendAsSmimeInfoSetDefaultOutput:
        """Sets the default S/MIME config for the specified send-as alias.

Use this when you want to sets the default S/MIME config for the specified send-as alias.
Key inputs: fields, user_id, send_as_email, id."""
        tool = self._client.get_tool('gmail_users_settings_send_as_smime_info_set_default')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsSendAsSmimeInfoSetDefaultOutput.model_validate(coerce_tool_result(result))
