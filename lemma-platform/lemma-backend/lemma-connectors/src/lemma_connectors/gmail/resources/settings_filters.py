from __future__ import annotations

from lemma_connectors.gmail.generated.tool_types import GmailUsersSettingsFiltersCreateToolInput, GmailUsersSettingsFiltersCreateToolOutput, GmailUsersSettingsFiltersDeleteToolInput, GmailUsersSettingsFiltersDeleteToolOutput, GmailUsersSettingsFiltersGetToolInput, GmailUsersSettingsFiltersGetToolOutput, GmailUsersSettingsFiltersListToolInput, GmailUsersSettingsFiltersListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SettingsFiltersCreateInput(GmailUsersSettingsFiltersCreateToolInput):
    """Operation input for `settings_filters_create`."""
    pass

class SettingsFiltersCreateOutput(GmailUsersSettingsFiltersCreateToolOutput):
    """Operation output for `settings_filters_create`."""
    pass

class SettingsFiltersDeleteInput(GmailUsersSettingsFiltersDeleteToolInput):
    """Operation input for `settings_filters_delete`."""
    pass

class SettingsFiltersDeleteOutput(GmailUsersSettingsFiltersDeleteToolOutput):
    """Operation output for `settings_filters_delete`."""
    pass

class SettingsFiltersGetInput(GmailUsersSettingsFiltersGetToolInput):
    """Operation input for `settings_filters_get`."""
    pass

class SettingsFiltersGetOutput(GmailUsersSettingsFiltersGetToolOutput):
    """Operation output for `settings_filters_get`."""
    pass

class SettingsFiltersListInput(GmailUsersSettingsFiltersListToolInput):
    """Operation input for `settings_filters_list`."""
    pass

class SettingsFiltersListOutput(GmailUsersSettingsFiltersListToolOutput):
    """Operation output for `settings_filters_list`."""
    pass

class GmailSettingsFiltersResource(BaseResourceClient):
    """Operations for the `settings_filters` resource."""

    @operation(
        name='settings_filters_create',
        title='SettingsFiltersCreate',
        input_model=SettingsFiltersCreateInput,
        output_model=SettingsFiltersCreateOutput,
        tools_used=('gmail_users_settings_filters_create',),
        tags=tuple(['users']),
    )
    async def create(self, data: SettingsFiltersCreateInput) -> SettingsFiltersCreateOutput:
        """Creates a filter. Note: you can only create a maximum of 1,000 filters.

Important inputs: fields, user_id, body"""
        tool = self._client.get_tool('gmail_users_settings_filters_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsFiltersCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_filters_delete',
        title='SettingsFiltersDelete',
        input_model=SettingsFiltersDeleteInput,
        output_model=SettingsFiltersDeleteOutput,
        tools_used=('gmail_users_settings_filters_delete',),
        tags=tuple(['users']),
    )
    async def delete(self, data: SettingsFiltersDeleteInput) -> SettingsFiltersDeleteOutput:
        """Immediately and permanently deletes the specified filter.

Important inputs: fields, user_id, id"""
        tool = self._client.get_tool('gmail_users_settings_filters_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsFiltersDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_filters_get',
        title='SettingsFiltersGet',
        input_model=SettingsFiltersGetInput,
        output_model=SettingsFiltersGetOutput,
        tools_used=('gmail_users_settings_filters_get',),
        tags=tuple(['users']),
    )
    async def get(self, data: SettingsFiltersGetInput) -> SettingsFiltersGetOutput:
        """Gets a filter.

Important inputs: fields, user_id, id"""
        tool = self._client.get_tool('gmail_users_settings_filters_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsFiltersGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_filters_list',
        title='SettingsFiltersList',
        input_model=SettingsFiltersListInput,
        output_model=SettingsFiltersListOutput,
        tools_used=('gmail_users_settings_filters_list',),
        tags=tuple(['users']),
    )
    async def list(self, data: SettingsFiltersListInput) -> SettingsFiltersListOutput:
        """Lists the message filters of a Gmail user.

Important inputs: fields, user_id"""
        tool = self._client.get_tool('gmail_users_settings_filters_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsFiltersListOutput.model_validate(coerce_tool_result(result))
