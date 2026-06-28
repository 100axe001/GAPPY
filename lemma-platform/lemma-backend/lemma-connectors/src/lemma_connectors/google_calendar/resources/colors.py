from __future__ import annotations

from lemma_connectors.google_calendar.generated.tool_types import CalendarColorsGetToolInput, CalendarColorsGetToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ColorsGetInput(CalendarColorsGetToolInput):
    """Operation input for `colors_get`."""
    pass

class ColorsGetOutput(CalendarColorsGetToolOutput):
    """Operation output for `colors_get`."""
    pass

class GoogleCalendarColorsResource(BaseResourceClient):
    """Operations for the `colors` resource."""

    @operation(
        name='colors_get',
        title='ColorsGet',
        input_model=ColorsGetInput,
        output_model=ColorsGetOutput,
        tools_used=('calendar_colors_get',),
        tags=tuple(['colors']),
    )
    async def get(self, data: ColorsGetInput) -> ColorsGetOutput:
        """Returns the color definitions for calendars and events.

Important inputs: fields"""
        tool = self._client.get_tool('calendar_colors_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ColorsGetOutput.model_validate(coerce_tool_result(result))
