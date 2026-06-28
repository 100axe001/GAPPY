from __future__ import annotations

from lemma_connectors.google_calendar.generated.tool_types import CalendarSettingsGetToolInput, CalendarSettingsGetToolOutput, CalendarSettingsListToolInput, CalendarSettingsListToolOutput, CalendarSettingsWatchToolInput, CalendarSettingsWatchToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SettingsGetInput(CalendarSettingsGetToolInput):
    """Operation input for `settings_get`."""
    pass

class SettingsGetOutput(CalendarSettingsGetToolOutput):
    """Operation output for `settings_get`."""
    pass

class SettingsListInput(CalendarSettingsListToolInput):
    """Operation input for `settings_list`."""
    pass

class SettingsListOutput(CalendarSettingsListToolOutput):
    """Operation output for `settings_list`."""
    pass

class SettingsWatchInput(CalendarSettingsWatchToolInput):
    """Operation input for `settings_watch`."""
    pass

class SettingsWatchOutput(CalendarSettingsWatchToolOutput):
    """Operation output for `settings_watch`."""
    pass

class GoogleCalendarSettingsResource(BaseResourceClient):
    """Operations for the `settings` resource."""

    @operation(
        name='settings_get',
        title='SettingsGet',
        input_model=SettingsGetInput,
        output_model=SettingsGetOutput,
        tools_used=('calendar_settings_get',),
        tags=tuple(['settings']),
    )
    async def get(self, data: SettingsGetInput) -> SettingsGetOutput:
        """Returns a single user setting.

Important inputs: fields, setting"""
        tool = self._client.get_tool('calendar_settings_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_list',
        title='SettingsList',
        input_model=SettingsListInput,
        output_model=SettingsListOutput,
        tools_used=('calendar_settings_list',),
        tags=tuple(['settings']),
    )
    async def list(self, data: SettingsListInput) -> SettingsListOutput:
        """Returns all user settings for the authenticated user.

Important inputs: fields, max_results, page_token, sync_token"""
        tool = self._client.get_tool('calendar_settings_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='settings_watch',
        title='SettingsWatch',
        input_model=SettingsWatchInput,
        output_model=SettingsWatchOutput,
        tools_used=('calendar_settings_watch',),
        tags=tuple(['settings']),
    )
    async def watch(self, data: SettingsWatchInput) -> SettingsWatchOutput:
        """Watch for changes to Settings resources.

Important inputs: fields, max_results, page_token, sync_token, body"""
        tool = self._client.get_tool('calendar_settings_watch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SettingsWatchOutput.model_validate(coerce_tool_result(result))
