from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsGetAutoForwardingToolInput, GmailUsersSettingsGetAutoForwardingToolOutput, GmailUsersSettingsGetImapToolInput, GmailUsersSettingsGetImapToolOutput, GmailUsersSettingsGetLanguageToolInput, GmailUsersSettingsGetLanguageToolOutput, GmailUsersSettingsGetPopToolInput, GmailUsersSettingsGetPopToolOutput, GmailUsersSettingsGetVacationToolInput, GmailUsersSettingsGetVacationToolOutput, GmailUsersSettingsUpdateAutoForwardingToolInput, GmailUsersSettingsUpdateAutoForwardingToolOutput, GmailUsersSettingsUpdateImapToolInput, GmailUsersSettingsUpdateImapToolOutput, GmailUsersSettingsUpdateLanguageToolInput, GmailUsersSettingsUpdateLanguageToolOutput, GmailUsersSettingsUpdatePopToolInput, GmailUsersSettingsUpdatePopToolOutput, GmailUsersSettingsUpdateVacationToolInput, GmailUsersSettingsUpdateVacationToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SettingsGetAutoForwardingInput(GmailUsersSettingsGetAutoForwardingToolInput):
    """Operation input for `settings_get_auto_forwarding`."""
    pass

class SettingsGetAutoForwardingOutput(GmailUsersSettingsGetAutoForwardingToolOutput):
    """Operation output for `settings_get_auto_forwarding`."""
    pass

class SettingsGetImapInput(GmailUsersSettingsGetImapToolInput):
    """Operation input for `settings_get_imap`."""
    pass

class SettingsGetImapOutput(GmailUsersSettingsGetImapToolOutput):
    """Operation output for `settings_get_imap`."""
    pass

class SettingsGetLanguageInput(GmailUsersSettingsGetLanguageToolInput):
    """Operation input for `settings_get_language`."""
    pass

class SettingsGetLanguageOutput(GmailUsersSettingsGetLanguageToolOutput):
    """Operation output for `settings_get_language`."""
    pass

class SettingsGetPopInput(GmailUsersSettingsGetPopToolInput):
    """Operation input for `settings_get_pop`."""
    pass

class SettingsGetPopOutput(GmailUsersSettingsGetPopToolOutput):
    """Operation output for `settings_get_pop`."""
    pass

class SettingsGetVacationInput(GmailUsersSettingsGetVacationToolInput):
    """Operation input for `settings_get_vacation`."""
    pass

class SettingsGetVacationOutput(GmailUsersSettingsGetVacationToolOutput):
    """Operation output for `settings_get_vacation`."""
    pass

class SettingsUpdateAutoForwardingInput(GmailUsersSettingsUpdateAutoForwardingToolInput):
    """Operation input for `settings_update_auto_forwarding`."""
    pass

class SettingsUpdateAutoForwardingOutput(GmailUsersSettingsUpdateAutoForwardingToolOutput):
    """Operation output for `settings_update_auto_forwarding`."""
    pass

class SettingsUpdateImapInput(GmailUsersSettingsUpdateImapToolInput):
    """Operation input for `settings_update_imap`."""
    pass

class SettingsUpdateImapOutput(GmailUsersSettingsUpdateImapToolOutput):
    """Operation output for `settings_update_imap`."""
    pass

class SettingsUpdateLanguageInput(GmailUsersSettingsUpdateLanguageToolInput):
    """Operation input for `settings_update_language`."""
    pass

class SettingsUpdateLanguageOutput(GmailUsersSettingsUpdateLanguageToolOutput):
    """Operation output for `settings_update_language`."""
    pass

class SettingsUpdatePopInput(GmailUsersSettingsUpdatePopToolInput):
    """Operation input for `settings_update_pop`."""
    pass

class SettingsUpdatePopOutput(GmailUsersSettingsUpdatePopToolOutput):
    """Operation output for `settings_update_pop`."""
    pass

class SettingsUpdateVacationInput(GmailUsersSettingsUpdateVacationToolInput):
    """Operation input for `settings_update_vacation`."""
    pass

class SettingsUpdateVacationOutput(GmailUsersSettingsUpdateVacationToolOutput):
    """Operation output for `settings_update_vacation`."""
    pass

class GmailSettingsResource(BaseResourceClient):
    """Operations for the `settings` resource."""

    @operation(
        name='settings_get_auto_forwarding',
        title='SettingsGetAutoForwarding',
        input_model=SettingsGetAutoForwardingInput,
        output_model=SettingsGetAutoForwardingOutput,
        tools_used=('gmail_users_settings_get_auto_forwarding',),
        tags=tuple(['users']),
    )
    async def get_auto_forwarding(self, data: SettingsGetAutoForwardingInput) -> SettingsGetAutoForwardingOutput:
        """Gets the auto-forwarding setting for the specified account.

Important inputs: fields, user_id"""
        tool = self._client.get_tool('gmail_users_settings_get_auto_forwarding')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsGetAutoForwardingOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_get_imap',
        title='SettingsGetImap',
        input_model=SettingsGetImapInput,
        output_model=SettingsGetImapOutput,
        tools_used=('gmail_users_settings_get_imap',),
        tags=tuple(['users']),
    )
    async def get_imap(self, data: SettingsGetImapInput) -> SettingsGetImapOutput:
        """Gets IMAP settings.

Important inputs: fields, user_id"""
        tool = self._client.get_tool('gmail_users_settings_get_imap')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsGetImapOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_get_language',
        title='SettingsGetLanguage',
        input_model=SettingsGetLanguageInput,
        output_model=SettingsGetLanguageOutput,
        tools_used=('gmail_users_settings_get_language',),
        tags=tuple(['users']),
    )
    async def get_language(self, data: SettingsGetLanguageInput) -> SettingsGetLanguageOutput:
        """Gets language settings.

Important inputs: fields, user_id"""
        tool = self._client.get_tool('gmail_users_settings_get_language')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsGetLanguageOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_get_pop',
        title='SettingsGetPop',
        input_model=SettingsGetPopInput,
        output_model=SettingsGetPopOutput,
        tools_used=('gmail_users_settings_get_pop',),
        tags=tuple(['users']),
    )
    async def get_pop(self, data: SettingsGetPopInput) -> SettingsGetPopOutput:
        """Gets POP settings.

Important inputs: fields, user_id"""
        tool = self._client.get_tool('gmail_users_settings_get_pop')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsGetPopOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_get_vacation',
        title='SettingsGetVacation',
        input_model=SettingsGetVacationInput,
        output_model=SettingsGetVacationOutput,
        tools_used=('gmail_users_settings_get_vacation',),
        tags=tuple(['users']),
    )
    async def get_vacation(self, data: SettingsGetVacationInput) -> SettingsGetVacationOutput:
        """Gets vacation responder settings.

Important inputs: fields, user_id"""
        tool = self._client.get_tool('gmail_users_settings_get_vacation')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsGetVacationOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_update_auto_forwarding',
        title='SettingsUpdateAutoForwarding',
        input_model=SettingsUpdateAutoForwardingInput,
        output_model=SettingsUpdateAutoForwardingOutput,
        tools_used=('gmail_users_settings_update_auto_forwarding',),
        tags=tuple(['users']),
    )
    async def update_auto_forwarding(self, data: SettingsUpdateAutoForwardingInput) -> SettingsUpdateAutoForwardingOutput:
        """Updates the auto-forwarding setting for the specified account. A verified forwarding address must be specified when auto-forwarding is enabled. This method is only available to service account clients that have been delegated domain-wide authority.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_settings_update_auto_forwarding')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsUpdateAutoForwardingOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_update_imap',
        title='SettingsUpdateImap',
        input_model=SettingsUpdateImapInput,
        output_model=SettingsUpdateImapOutput,
        tools_used=('gmail_users_settings_update_imap',),
        tags=tuple(['users']),
    )
    async def update_imap(self, data: SettingsUpdateImapInput) -> SettingsUpdateImapOutput:
        """Updates IMAP settings.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_settings_update_imap')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsUpdateImapOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_update_language',
        title='SettingsUpdateLanguage',
        input_model=SettingsUpdateLanguageInput,
        output_model=SettingsUpdateLanguageOutput,
        tools_used=('gmail_users_settings_update_language',),
        tags=tuple(['users']),
    )
    async def update_language(self, data: SettingsUpdateLanguageInput) -> SettingsUpdateLanguageOutput:
        """Updates language settings. If successful, the return object contains the `displayLanguage` that was saved for the user, which may differ from the value passed into the request. This is because the requested `displayLanguage` may not be directly supported by Gmail but have a close variant that is, and so the variant may be chosen and saved instead.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_settings_update_language')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsUpdateLanguageOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_update_pop',
        title='SettingsUpdatePop',
        input_model=SettingsUpdatePopInput,
        output_model=SettingsUpdatePopOutput,
        tools_used=('gmail_users_settings_update_pop',),
        tags=tuple(['users']),
    )
    async def update_pop(self, data: SettingsUpdatePopInput) -> SettingsUpdatePopOutput:
        """Updates POP settings.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_settings_update_pop')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsUpdatePopOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_update_vacation',
        title='SettingsUpdateVacation',
        input_model=SettingsUpdateVacationInput,
        output_model=SettingsUpdateVacationOutput,
        tools_used=('gmail_users_settings_update_vacation',),
        tags=tuple(['users']),
    )
    async def update_vacation(self, data: SettingsUpdateVacationInput) -> SettingsUpdateVacationOutput:
        """Updates vacation responder settings.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_settings_update_vacation')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsUpdateVacationOutput.model_validate(coerce_tool_result(result))
