from __future__ import annotations

from lemma_connectors.google_calendar.generated.tool_types import CalendarEventsDeleteToolInput, CalendarEventsDeleteToolOutput, CalendarEventsGetToolInput, CalendarEventsGetToolOutput, CalendarEventsImportToolInput, CalendarEventsImportToolOutput, CalendarEventsInsertToolInput, CalendarEventsInsertToolOutput, CalendarEventsInstancesToolInput, CalendarEventsInstancesToolOutput, CalendarEventsListToolInput, CalendarEventsListToolOutput, CalendarEventsMoveToolInput, CalendarEventsMoveToolOutput, CalendarEventsPatchToolInput, CalendarEventsPatchToolOutput, CalendarEventsQuickAddToolInput, CalendarEventsQuickAddToolOutput, CalendarEventsUpdateToolInput, CalendarEventsUpdateToolOutput, CalendarEventsWatchToolInput, CalendarEventsWatchToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class EventsDeleteInput(CalendarEventsDeleteToolInput):
    """Operation input for `events_delete`."""
    pass

class EventsDeleteOutput(CalendarEventsDeleteToolOutput):
    """Operation output for `events_delete`."""
    pass

class EventsGetInput(CalendarEventsGetToolInput):
    """Operation input for `events_get`."""
    pass

class EventsGetOutput(CalendarEventsGetToolOutput):
    """Operation output for `events_get`."""
    pass

class EventsImportInput(CalendarEventsImportToolInput):
    """Operation input for `events_import`."""
    pass

class EventsImportOutput(CalendarEventsImportToolOutput):
    """Operation output for `events_import`."""
    pass

class EventsInsertInput(CalendarEventsInsertToolInput):
    """Operation input for `events_insert`."""
    pass

class EventsInsertOutput(CalendarEventsInsertToolOutput):
    """Operation output for `events_insert`."""
    pass

class EventsInstancesInput(CalendarEventsInstancesToolInput):
    """Operation input for `events_instances`."""
    pass

class EventsInstancesOutput(CalendarEventsInstancesToolOutput):
    """Operation output for `events_instances`."""
    pass

class EventsListInput(CalendarEventsListToolInput):
    """Operation input for `events_list`."""
    pass

class EventsListOutput(CalendarEventsListToolOutput):
    """Operation output for `events_list`."""
    pass

class EventsMoveInput(CalendarEventsMoveToolInput):
    """Operation input for `events_move`."""
    pass

class EventsMoveOutput(CalendarEventsMoveToolOutput):
    """Operation output for `events_move`."""
    pass

class EventsPatchInput(CalendarEventsPatchToolInput):
    """Operation input for `events_patch`."""
    pass

class EventsPatchOutput(CalendarEventsPatchToolOutput):
    """Operation output for `events_patch`."""
    pass

class EventsQuickAddInput(CalendarEventsQuickAddToolInput):
    """Operation input for `events_quick_add`."""
    pass

class EventsQuickAddOutput(CalendarEventsQuickAddToolOutput):
    """Operation output for `events_quick_add`."""
    pass

class EventsUpdateInput(CalendarEventsUpdateToolInput):
    """Operation input for `events_update`."""
    pass

class EventsUpdateOutput(CalendarEventsUpdateToolOutput):
    """Operation output for `events_update`."""
    pass

class EventsWatchInput(CalendarEventsWatchToolInput):
    """Operation input for `events_watch`."""
    pass

class EventsWatchOutput(CalendarEventsWatchToolOutput):
    """Operation output for `events_watch`."""
    pass

class GoogleCalendarEventsResource(BaseResourceClient):
    """Operations for the `events` resource."""

    @operation(
        name='events_delete',
        title='EventsDelete',
        input_model=EventsDeleteInput,
        output_model=EventsDeleteOutput,
        tools_used=('calendar_events_delete',),
        tags=tuple(['events']),
    )
    async def delete(self, data: EventsDeleteInput) -> EventsDeleteOutput:
        """Deletes an event.

Important inputs: fields, calendar_id, event_id, send_notifications, send_updates"""
        tool = self._client.get_tool('calendar_events_delete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return EventsDeleteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='events_get',
        title='EventsGet',
        input_model=EventsGetInput,
        output_model=EventsGetOutput,
        tools_used=('calendar_events_get',),
        tags=tuple(['events']),
    )
    async def get(self, data: EventsGetInput) -> EventsGetOutput:
        """Returns an event based on its Google Calendar ID. To retrieve an event using its iCalendar ID, call the events.list method using the iCalUID parameter.

Important inputs: fields, calendar_id, event_id, always_include_email, max_attendees, time_zone"""
        tool = self._client.get_tool('calendar_events_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return EventsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='events_import',
        title='EventsImport',
        input_model=EventsImportInput,
        output_model=EventsImportOutput,
        tools_used=('calendar_events_import',),
        tags=tuple(['events']),
    )
    async def import_(self, data: EventsImportInput) -> EventsImportOutput:
        """Imports an event. This operation is used to add a private copy of an existing event to a calendar.

Important inputs: fields, calendar_id, conference_data_version, supports_attachments, body"""
        tool = self._client.get_tool('calendar_events_import')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return EventsImportOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='events_insert',
        title='EventsInsert',
        input_model=EventsInsertInput,
        output_model=EventsInsertOutput,
        tools_used=('calendar_events_insert',),
        tags=tuple(['events']),
    )
    async def insert(self, data: EventsInsertInput) -> EventsInsertOutput:
        """Creates an event.

Important inputs: fields, calendar_id, conference_data_version, max_attendees, send_notifications, send_updates, supports_attachments, body"""
        tool = self._client.get_tool('calendar_events_insert')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return EventsInsertOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='events_instances',
        title='EventsInstances',
        input_model=EventsInstancesInput,
        output_model=EventsInstancesOutput,
        tools_used=('calendar_events_instances',),
        tags=tuple(['events']),
    )
    async def instances(self, data: EventsInstancesInput) -> EventsInstancesOutput:
        """Returns instances of the specified recurring event.

Important inputs: fields, calendar_id, event_id, always_include_email, max_attendees, max_results, original_start, page_token, show_deleted, time_max, time_min, time_zone"""
        tool = self._client.get_tool('calendar_events_instances')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return EventsInstancesOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='events_list',
        title='EventsList',
        input_model=EventsListInput,
        output_model=EventsListOutput,
        tools_used=('calendar_events_list',),
        tags=tuple(['events']),
    )
    async def list(self, data: EventsListInput) -> EventsListOutput:
        """Returns events on the specified calendar.

Important inputs: fields, calendar_id, always_include_email, event_types, i_cal_uid, max_attendees, max_results, order_by, page_token, private_extended_property, q, shared_extended_property, show_deleted, show_hidden_invitations, single_events, sync_token, time_max, time_min, time_zone, updated_min"""
        tool = self._client.get_tool('calendar_events_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return EventsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='events_move',
        title='EventsMove',
        input_model=EventsMoveInput,
        output_model=EventsMoveOutput,
        tools_used=('calendar_events_move',),
        tags=tuple(['events']),
    )
    async def move(self, data: EventsMoveInput) -> EventsMoveOutput:
        """Moves an event to another calendar, i.e. changes an event's organizer.

Important inputs: fields, calendar_id, event_id, destination, send_notifications, send_updates"""
        tool = self._client.get_tool('calendar_events_move')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return EventsMoveOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='events_patch',
        title='EventsPatch',
        input_model=EventsPatchInput,
        output_model=EventsPatchOutput,
        tools_used=('calendar_events_patch',),
        tags=tuple(['events']),
    )
    async def patch(self, data: EventsPatchInput) -> EventsPatchOutput:
        """Updates an event. This method supports patch semantics.

Important inputs: fields, calendar_id, event_id, always_include_email, conference_data_version, max_attendees, send_notifications, send_updates, supports_attachments, body"""
        tool = self._client.get_tool('calendar_events_patch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return EventsPatchOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='events_quick_add',
        title='EventsQuickAdd',
        input_model=EventsQuickAddInput,
        output_model=EventsQuickAddOutput,
        tools_used=('calendar_events_quick_add',),
        tags=tuple(['events']),
    )
    async def quick_add(self, data: EventsQuickAddInput) -> EventsQuickAddOutput:
        """Creates an event based on a simple text string.

Important inputs: fields, calendar_id, text, send_notifications, send_updates"""
        tool = self._client.get_tool('calendar_events_quick_add')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return EventsQuickAddOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='events_update',
        title='EventsUpdate',
        input_model=EventsUpdateInput,
        output_model=EventsUpdateOutput,
        tools_used=('calendar_events_update',),
        tags=tuple(['events']),
    )
    async def update(self, data: EventsUpdateInput) -> EventsUpdateOutput:
        """Updates an event.

Important inputs: fields, calendar_id, event_id, always_include_email, conference_data_version, max_attendees, send_notifications, send_updates, supports_attachments, body"""
        tool = self._client.get_tool('calendar_events_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return EventsUpdateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='events_watch',
        title='EventsWatch',
        input_model=EventsWatchInput,
        output_model=EventsWatchOutput,
        tools_used=('calendar_events_watch',),
        tags=tuple(['events']),
    )
    async def watch(self, data: EventsWatchInput) -> EventsWatchOutput:
        """Watch for changes to Events resources.

Important inputs: fields, calendar_id, always_include_email, event_types, i_cal_uid, max_attendees, max_results, order_by, page_token, private_extended_property, q, shared_extended_property, show_deleted, show_hidden_invitations, single_events, sync_token, time_max, time_min, time_zone, updated_min, body"""
        tool = self._client.get_tool('calendar_events_watch')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return EventsWatchOutput.model_validate(coerce_tool_result(result))
