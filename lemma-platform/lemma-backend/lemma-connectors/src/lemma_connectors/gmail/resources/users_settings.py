from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsGetAutoForwardingToolInput, GmailUsersSettingsGetAutoForwardingToolOutput, GmailUsersSettingsGetImapToolInput, GmailUsersSettingsGetImapToolOutput, GmailUsersSettingsGetLanguageToolInput, GmailUsersSettingsGetLanguageToolOutput, GmailUsersSettingsGetPopToolInput, GmailUsersSettingsGetPopToolOutput, GmailUsersSettingsGetVacationToolInput, GmailUsersSettingsGetVacationToolOutput, GmailUsersSettingsUpdateAutoForwardingToolInput, GmailUsersSettingsUpdateAutoForwardingToolOutput, GmailUsersSettingsUpdateImapToolInput, GmailUsersSettingsUpdateImapToolOutput, GmailUsersSettingsUpdateLanguageToolInput, GmailUsersSettingsUpdateLanguageToolOutput, GmailUsersSettingsUpdatePopToolInput, GmailUsersSettingsUpdatePopToolOutput, GmailUsersSettingsUpdateVacationToolInput, GmailUsersSettingsUpdateVacationToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsersSettingsGetAutoForwardingInput(GmailUsersSettingsGetAutoForwardingToolInput):
    """Operation input for `users_settings_get_auto_forwarding`."""
    pass

class UsersSettingsGetAutoForwardingOutput(GmailUsersSettingsGetAutoForwardingToolOutput):
    """Operation output for `users_settings_get_auto_forwarding`."""
    pass

class UsersSettingsGetImapInput(GmailUsersSettingsGetImapToolInput):
    """Operation input for `users_settings_get_imap`."""
    pass

class UsersSettingsGetImapOutput(GmailUsersSettingsGetImapToolOutput):
    """Operation output for `users_settings_get_imap`."""
    pass

class UsersSettingsGetLanguageInput(GmailUsersSettingsGetLanguageToolInput):
    """Operation input for `users_settings_get_language`."""
    pass

class UsersSettingsGetLanguageOutput(GmailUsersSettingsGetLanguageToolOutput):
    """Operation output for `users_settings_get_language`."""
    pass

class UsersSettingsGetPopInput(GmailUsersSettingsGetPopToolInput):
    """Operation input for `users_settings_get_pop`."""
    pass

class UsersSettingsGetPopOutput(GmailUsersSettingsGetPopToolOutput):
    """Operation output for `users_settings_get_pop`."""
    pass

class UsersSettingsGetVacationInput(GmailUsersSettingsGetVacationToolInput):
    """Operation input for `users_settings_get_vacation`."""
    pass

class UsersSettingsGetVacationOutput(GmailUsersSettingsGetVacationToolOutput):
    """Operation output for `users_settings_get_vacation`."""
    pass

class UsersSettingsUpdateAutoForwardingInput(GmailUsersSettingsUpdateAutoForwardingToolInput):
    """Operation input for `users_settings_update_auto_forwarding`."""
    pass

class UsersSettingsUpdateAutoForwardingOutput(GmailUsersSettingsUpdateAutoForwardingToolOutput):
    """Operation output for `users_settings_update_auto_forwarding`."""
    pass

class UsersSettingsUpdateImapInput(GmailUsersSettingsUpdateImapToolInput):
    """Operation input for `users_settings_update_imap`."""
    pass

class UsersSettingsUpdateImapOutput(GmailUsersSettingsUpdateImapToolOutput):
    """Operation output for `users_settings_update_imap`."""
    pass

class UsersSettingsUpdateLanguageInput(GmailUsersSettingsUpdateLanguageToolInput):
    """Operation input for `users_settings_update_language`."""
    pass

class UsersSettingsUpdateLanguageOutput(GmailUsersSettingsUpdateLanguageToolOutput):
    """Operation output for `users_settings_update_language`."""
    pass

class UsersSettingsUpdatePopInput(GmailUsersSettingsUpdatePopToolInput):
    """Operation input for `users_settings_update_pop`."""
    pass

class UsersSettingsUpdatePopOutput(GmailUsersSettingsUpdatePopToolOutput):
    """Operation output for `users_settings_update_pop`."""
    pass

class UsersSettingsUpdateVacationInput(GmailUsersSettingsUpdateVacationToolInput):
    """Operation input for `users_settings_update_vacation`."""
    pass

class UsersSettingsUpdateVacationOutput(GmailUsersSettingsUpdateVacationToolOutput):
    """Operation output for `users_settings_update_vacation`."""
    pass

class GmailUsersSettingsResource(BaseResourceClient):
    """Operations grouped around the `users_settings` resource."""

    @operation(
        name='users_settings_get_auto_forwarding',
        title='UsersSettingsGetAutoForwarding',
        input_model=UsersSettingsGetAutoForwardingInput,
        output_model=UsersSettingsGetAutoForwardingOutput,
        tools_used=('gmail_users_settings_get_auto_forwarding',),
        tags=tuple(['users']),
    )
    async def get_auto_forwarding(self, data: UsersSettingsGetAutoForwardingInput) -> UsersSettingsGetAutoForwardingOutput:
        """Gets the auto-forwarding setting for the specified account.

Use this when you want to gets the auto-forwarding setting for the specified account.
Key inputs: fields, user_id."""
        tool = self._client.get_tool('gmail_users_settings_get_auto_forwarding')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsGetAutoForwardingOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_get_imap',
        title='UsersSettingsGetImap',
        input_model=UsersSettingsGetImapInput,
        output_model=UsersSettingsGetImapOutput,
        tools_used=('gmail_users_settings_get_imap',),
        tags=tuple(['users']),
    )
    async def get_imap(self, data: UsersSettingsGetImapInput) -> UsersSettingsGetImapOutput:
        """Gets IMAP settings.

Use this when you want to gets IMAP settings.
Key inputs: fields, user_id."""
        tool = self._client.get_tool('gmail_users_settings_get_imap')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsGetImapOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_get_language',
        title='UsersSettingsGetLanguage',
        input_model=UsersSettingsGetLanguageInput,
        output_model=UsersSettingsGetLanguageOutput,
        tools_used=('gmail_users_settings_get_language',),
        tags=tuple(['users']),
    )
    async def get_language(self, data: UsersSettingsGetLanguageInput) -> UsersSettingsGetLanguageOutput:
        """Gets language settings.

Use this when you want to gets language settings.
Key inputs: fields, user_id."""
        tool = self._client.get_tool('gmail_users_settings_get_language')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsGetLanguageOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_get_pop',
        title='UsersSettingsGetPop',
        input_model=UsersSettingsGetPopInput,
        output_model=UsersSettingsGetPopOutput,
        tools_used=('gmail_users_settings_get_pop',),
        tags=tuple(['users']),
    )
    async def get_pop(self, data: UsersSettingsGetPopInput) -> UsersSettingsGetPopOutput:
        """Gets POP settings.

Use this when you want to gets POP settings.
Key inputs: fields, user_id."""
        tool = self._client.get_tool('gmail_users_settings_get_pop')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsGetPopOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_get_vacation',
        title='UsersSettingsGetVacation',
        input_model=UsersSettingsGetVacationInput,
        output_model=UsersSettingsGetVacationOutput,
        tools_used=('gmail_users_settings_get_vacation',),
        tags=tuple(['users']),
    )
    async def get_vacation(self, data: UsersSettingsGetVacationInput) -> UsersSettingsGetVacationOutput:
        """Gets vacation responder settings.

Use this when you want to gets vacation responder settings.
Key inputs: fields, user_id."""
        tool = self._client.get_tool('gmail_users_settings_get_vacation')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsGetVacationOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_update_auto_forwarding',
        title='UsersSettingsUpdateAutoForwarding',
        input_model=UsersSettingsUpdateAutoForwardingInput,
        output_model=UsersSettingsUpdateAutoForwardingOutput,
        tools_used=('gmail_users_settings_update_auto_forwarding',),
        tags=tuple(['users']),
    )
    async def update_auto_forwarding(self, data: UsersSettingsUpdateAutoForwardingInput) -> UsersSettingsUpdateAutoForwardingOutput:
        """Updates the auto-forwarding setting for the specified account. A verified forwarding address must be specified when auto-forwarding is enabled. This method is only available to service account clients that have been delegated domain-wide authority.

Use this when you want to updates the auto-forwarding setting for the specified account. A verified forwarding address must be specified when auto-forwarding is enabled. This method is only available to service account clients that have been delegated domain-wide authority.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_settings_update_auto_forwarding')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsUpdateAutoForwardingOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_update_imap',
        title='UsersSettingsUpdateImap',
        input_model=UsersSettingsUpdateImapInput,
        output_model=UsersSettingsUpdateImapOutput,
        tools_used=('gmail_users_settings_update_imap',),
        tags=tuple(['users']),
    )
    async def update_imap(self, data: UsersSettingsUpdateImapInput) -> UsersSettingsUpdateImapOutput:
        """Updates IMAP settings.

Use this when you want to updates IMAP settings.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_settings_update_imap')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsUpdateImapOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_update_language',
        title='UsersSettingsUpdateLanguage',
        input_model=UsersSettingsUpdateLanguageInput,
        output_model=UsersSettingsUpdateLanguageOutput,
        tools_used=('gmail_users_settings_update_language',),
        tags=tuple(['users']),
    )
    async def update_language(self, data: UsersSettingsUpdateLanguageInput) -> UsersSettingsUpdateLanguageOutput:
        """Updates language settings. If successful, the return object contains the `displayLanguage` that was saved for the user, which may differ from the value passed into the request. This is because the requested `displayLanguage` may not be directly supported by Gmail but have a close variant that is, and so the variant may be chosen and saved instead.

Use this when you want to updates language settings. If successful, the return object contains the `displayLanguage` that was saved for the user, which may differ from the value passed into the request. This is because the requested `displayLanguage` may not be directly supported by Gmail but have a close variant that is, and so the variant may be chosen and saved instead.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_settings_update_language')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsUpdateLanguageOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_update_pop',
        title='UsersSettingsUpdatePop',
        input_model=UsersSettingsUpdatePopInput,
        output_model=UsersSettingsUpdatePopOutput,
        tools_used=('gmail_users_settings_update_pop',),
        tags=tuple(['users']),
    )
    async def update_pop(self, data: UsersSettingsUpdatePopInput) -> UsersSettingsUpdatePopOutput:
        """Updates POP settings.

Use this when you want to updates POP settings.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_settings_update_pop')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsUpdatePopOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='users_settings_update_vacation',
        title='UsersSettingsUpdateVacation',
        input_model=UsersSettingsUpdateVacationInput,
        output_model=UsersSettingsUpdateVacationOutput,
        tools_used=('gmail_users_settings_update_vacation',),
        tags=tuple(['users']),
    )
    async def update_vacation(self, data: UsersSettingsUpdateVacationInput) -> UsersSettingsUpdateVacationOutput:
        """Updates vacation responder settings.

Use this when you want to updates vacation responder settings.
Key inputs: fields, user_id, body."""
        tool = self._client.get_tool('gmail_users_settings_update_vacation')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsersSettingsUpdateVacationOutput.model_validate(coerce_tool_result(result))
