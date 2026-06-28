from __future__ import annotations

from lemma_connectors.google_calendar.generated.tool_types import CalendarCalendarsClearToolInput, CalendarCalendarsClearToolOutput, CalendarCalendarsDeleteToolInput, CalendarCalendarsDeleteToolOutput, CalendarCalendarsGetToolInput, CalendarCalendarsGetToolOutput, CalendarCalendarsInsertToolInput, CalendarCalendarsInsertToolOutput, CalendarCalendarsPatchToolInput, CalendarCalendarsPatchToolOutput, CalendarCalendarsUpdateToolInput, CalendarCalendarsUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CalendarsClearInput(CalendarCalendarsClearToolInput):
    """Operation input for `calendars_clear`."""
    pass

class CalendarsClearOutput(CalendarCalendarsClearToolOutput):
    """Operation output for `calendars_clear`."""
    pass

class CalendarsDeleteInput(CalendarCalendarsDeleteToolInput):
    """Operation input for `calendars_delete`."""
    pass

class CalendarsDeleteOutput(CalendarCalendarsDeleteToolOutput):
    """Operation output for `calendars_delete`."""
    pass

class CalendarsGetInput(CalendarCalendarsGetToolInput):
    """Operation input for `calendars_get`."""
    pass

class CalendarsGetOutput(CalendarCalendarsGetToolOutput):
    """Operation output for `calendars_get`."""
    pass

class CalendarsInsertInput(CalendarCalendarsInsertToolInput):
    """Operation input for `calendars_insert`."""
    pass

class CalendarsInsertOutput(CalendarCalendarsInsertToolOutput):
    """Operation output for `calendars_insert`."""
    pass

class CalendarsPatchInput(CalendarCalendarsPatchToolInput):
    """Operation input for `calendars_patch`."""
    pass

class CalendarsPatchOutput(CalendarCalendarsPatchToolOutput):
    """Operation output for `calendars_patch`."""
    pass

class CalendarsUpdateInput(CalendarCalendarsUpdateToolInput):
    """Operation input for `calendars_update`."""
    pass

class CalendarsUpdateOutput(CalendarCalendarsUpdateToolOutput):
    """Operation output for `calendars_update`."""
    pass

class GoogleCalendarCalendarsResource(BaseResourceClient):
    """Operations for the `calendars` resource."""

    @operation(
        name='calendars_clear',
        title='CalendarsClear',
        input_model=CalendarsClearInput,
        output_model=CalendarsClearOutput,
        tools_used=('calendar_calendars_clear',),
        tags=tuple(['calendars']),
    )
    async def clear(self, data: CalendarsClearInput) -> CalendarsClearOutput:
        """Clears a primary calendar. This operation deletes all events associated with the primary calendar of an account.

Important inputs: fields, calendar_id"""
        tool = self._client.get_tool('calendar_calendars_clear')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CalendarsClearOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='calendars_delete',
        title='CalendarsDelete',
        input_model=CalendarsDeleteInput,
        output_model=CalendarsDeleteOutput,
        tools_used=('calendar_calendars_delete',),
        tags=tuple(['calendars']),
    )
    async def delete(self, data: CalendarsDeleteInput) -> CalendarsDeleteOutput:
        """Deletes a secondary calendar. Use calendars.clear for clearing all events on primary calendars.

Important inputs: fields, calendar_id"""
        tool = self._client.get_tool('calendar_calendars_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CalendarsDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='calendars_get',
        title='CalendarsGet',
        input_model=CalendarsGetInput,
        output_model=CalendarsGetOutput,
        tools_used=('calendar_calendars_get',),
        tags=tuple(['calendars']),
    )
    async def get(self, data: CalendarsGetInput) -> CalendarsGetOutput:
        """Returns metadata for a calendar.

Important inputs: fields, calendar_id"""
        tool = self._client.get_tool('calendar_calendars_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CalendarsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='calendars_insert',
        title='CalendarsInsert',
        input_model=CalendarsInsertInput,
        output_model=CalendarsInsertOutput,
        tools_used=('calendar_calendars_insert',),
        tags=tuple(['calendars']),
    )
    async def insert(self, data: CalendarsInsertInput) -> CalendarsInsertOutput:
        """Creates a secondary calendar.

Important inputs: fields, body"""
        tool = self._client.get_tool('calendar_calendars_insert')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CalendarsInsertOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='calendars_patch',
        title='CalendarsPatch',
        input_model=CalendarsPatchInput,
        output_model=CalendarsPatchOutput,
        tools_used=('calendar_calendars_patch',),
        tags=tuple(['calendars']),
    )
    async def patch(self, data: CalendarsPatchInput) -> CalendarsPatchOutput:
        """Updates metadata for a calendar. This method supports patch semantics.

Important inputs: fields, calendar_id, body"""
        tool = self._client.get_tool('calendar_calendars_patch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CalendarsPatchOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='calendars_update',
        title='CalendarsUpdate',
        input_model=CalendarsUpdateInput,
        output_model=CalendarsUpdateOutput,
        tools_used=('calendar_calendars_update',),
        tags=tuple(['calendars']),
    )
    async def update(self, data: CalendarsUpdateInput) -> CalendarsUpdateOutput:
        """Updates metadata for a calendar.

Important inputs: fields, calendar_id, body"""
        tool = self._client.get_tool('calendar_calendars_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CalendarsUpdateOutput.model_validate(coerce_tool_result(result))
