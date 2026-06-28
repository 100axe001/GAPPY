from __future__ import annotations

from lemma_connectors.google_calendar.generated.tool_types import CalendarCalendarListDeleteToolInput, CalendarCalendarListDeleteToolOutput, CalendarCalendarListGetToolInput, CalendarCalendarListGetToolOutput, CalendarCalendarListInsertToolInput, CalendarCalendarListInsertToolOutput, CalendarCalendarListListToolInput, CalendarCalendarListListToolOutput, CalendarCalendarListPatchToolInput, CalendarCalendarListPatchToolOutput, CalendarCalendarListUpdateToolInput, CalendarCalendarListUpdateToolOutput, CalendarCalendarListWatchToolInput, CalendarCalendarListWatchToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CalendarListDeleteInput(CalendarCalendarListDeleteToolInput):
    """Operation input for `calendar_list_delete`."""
    pass

class CalendarListDeleteOutput(CalendarCalendarListDeleteToolOutput):
    """Operation output for `calendar_list_delete`."""
    pass

class CalendarListGetInput(CalendarCalendarListGetToolInput):
    """Operation input for `calendar_list_get`."""
    pass

class CalendarListGetOutput(CalendarCalendarListGetToolOutput):
    """Operation output for `calendar_list_get`."""
    pass

class CalendarListInsertInput(CalendarCalendarListInsertToolInput):
    """Operation input for `calendar_list_insert`."""
    pass

class CalendarListInsertOutput(CalendarCalendarListInsertToolOutput):
    """Operation output for `calendar_list_insert`."""
    pass

class CalendarListListInput(CalendarCalendarListListToolInput):
    """Operation input for `calendar_list_list`."""
    pass

class CalendarListListOutput(CalendarCalendarListListToolOutput):
    """Operation output for `calendar_list_list`."""
    pass

class CalendarListPatchInput(CalendarCalendarListPatchToolInput):
    """Operation input for `calendar_list_patch`."""
    pass

class CalendarListPatchOutput(CalendarCalendarListPatchToolOutput):
    """Operation output for `calendar_list_patch`."""
    pass

class CalendarListUpdateInput(CalendarCalendarListUpdateToolInput):
    """Operation input for `calendar_list_update`."""
    pass

class CalendarListUpdateOutput(CalendarCalendarListUpdateToolOutput):
    """Operation output for `calendar_list_update`."""
    pass

class CalendarListWatchInput(CalendarCalendarListWatchToolInput):
    """Operation input for `calendar_list_watch`."""
    pass

class CalendarListWatchOutput(CalendarCalendarListWatchToolOutput):
    """Operation output for `calendar_list_watch`."""
    pass

class GoogleCalendarCalendarListResource(BaseResourceClient):
    """Operations for the `calendar_list` resource."""

    @operation(
        name='calendar_list_delete',
        title='CalendarListDelete',
        input_model=CalendarListDeleteInput,
        output_model=CalendarListDeleteOutput,
        tools_used=('calendar_calendar_list_delete',),
        tags=tuple(['calendarList']),
    )
    async def delete(self, data: CalendarListDeleteInput) -> CalendarListDeleteOutput:
        """Removes a calendar from the user's calendar list.

Important inputs: fields, calendar_id"""
        tool = self._client.get_tool('calendar_calendar_list_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CalendarListDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='calendar_list_get',
        title='CalendarListGet',
        input_model=CalendarListGetInput,
        output_model=CalendarListGetOutput,
        tools_used=('calendar_calendar_list_get',),
        tags=tuple(['calendarList']),
    )
    async def get(self, data: CalendarListGetInput) -> CalendarListGetOutput:
        """Returns a calendar from the user's calendar list.

Important inputs: fields, calendar_id"""
        tool = self._client.get_tool('calendar_calendar_list_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CalendarListGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='calendar_list_insert',
        title='CalendarListInsert',
        input_model=CalendarListInsertInput,
        output_model=CalendarListInsertOutput,
        tools_used=('calendar_calendar_list_insert',),
        tags=tuple(['calendarList']),
    )
    async def insert(self, data: CalendarListInsertInput) -> CalendarListInsertOutput:
        """Inserts an existing calendar into the user's calendar list.

Important inputs: fields, color_rgb_format, body"""
        tool = self._client.get_tool('calendar_calendar_list_insert')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CalendarListInsertOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='calendar_list_list',
        title='CalendarListList',
        input_model=CalendarListListInput,
        output_model=CalendarListListOutput,
        tools_used=('calendar_calendar_list_list',),
        tags=tuple(['calendarList']),
    )
    async def list(self, data: CalendarListListInput) -> CalendarListListOutput:
        """Returns the calendars on the user's calendar list.

Important inputs: fields, max_results, min_access_role, page_token, show_deleted, show_hidden, sync_token"""
        tool = self._client.get_tool('calendar_calendar_list_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CalendarListListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='calendar_list_patch',
        title='CalendarListPatch',
        input_model=CalendarListPatchInput,
        output_model=CalendarListPatchOutput,
        tools_used=('calendar_calendar_list_patch',),
        tags=tuple(['calendarList']),
    )
    async def patch(self, data: CalendarListPatchInput) -> CalendarListPatchOutput:
        """Updates an existing calendar on the user's calendar list. This method supports patch semantics.

Important inputs: fields, calendar_id, color_rgb_format, body"""
        tool = self._client.get_tool('calendar_calendar_list_patch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CalendarListPatchOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='calendar_list_update',
        title='CalendarListUpdate',
        input_model=CalendarListUpdateInput,
        output_model=CalendarListUpdateOutput,
        tools_used=('calendar_calendar_list_update',),
        tags=tuple(['calendarList']),
    )
    async def update(self, data: CalendarListUpdateInput) -> CalendarListUpdateOutput:
        """Updates an existing calendar on the user's calendar list.

Important inputs: fields, calendar_id, color_rgb_format, body"""
        tool = self._client.get_tool('calendar_calendar_list_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CalendarListUpdateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='calendar_list_watch',
        title='CalendarListWatch',
        input_model=CalendarListWatchInput,
        output_model=CalendarListWatchOutput,
        tools_used=('calendar_calendar_list_watch',),
        tags=tuple(['calendarList']),
    )
    async def watch(self, data: CalendarListWatchInput) -> CalendarListWatchOutput:
        """Watch for changes to CalendarList resources.

Important inputs: fields, max_results, min_access_role, page_token, show_deleted, show_hidden, sync_token, body"""
        tool = self._client.get_tool('calendar_calendar_list_watch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CalendarListWatchOutput.model_validate(coerce_tool_result(result))
