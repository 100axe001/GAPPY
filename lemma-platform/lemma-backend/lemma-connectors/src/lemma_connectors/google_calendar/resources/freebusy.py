from __future__ import annotations

from lemma_connectors.google_calendar.generated.tool_types import CalendarFreebusyQueryToolInput, CalendarFreebusyQueryToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class FreebusyQueryInput(CalendarFreebusyQueryToolInput):
    """Operation input for `freebusy_query`."""
    pass

class FreebusyQueryOutput(CalendarFreebusyQueryToolOutput):
    """Operation output for `freebusy_query`."""
    pass

class GoogleCalendarFreebusyResource(BaseResourceClient):
    """Operations for the `freebusy` resource."""

    @operation(
        name='freebusy_query',
        title='FreebusyQuery',
        input_model=FreebusyQueryInput,
        output_model=FreebusyQueryOutput,
        tools_used=('calendar_freebusy_query',),
        tags=tuple(['freebusy']),
    )
    async def query(self, data: FreebusyQueryInput) -> FreebusyQueryOutput:
        """Returns free/busy information for a set of calendars.

Important inputs: fields, body"""
        tool = self._client.get_tool('calendar_freebusy_query')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return FreebusyQueryOutput.model_validate(coerce_tool_result(result))
