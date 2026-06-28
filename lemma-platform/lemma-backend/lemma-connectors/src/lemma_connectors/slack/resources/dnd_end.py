from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import DndEndDndToolInput, DndEndDndToolOutput, DndEndSnoozeToolInput, DndEndSnoozeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DndEndDndInput(DndEndDndToolInput):
    """Operation input for `dnd_end_dnd`."""
    pass

class DndEndDndOutput(DndEndDndToolOutput):
    """Operation output for `dnd_end_dnd`."""
    pass

class DndEndSnoozeInput(DndEndSnoozeToolInput):
    """Operation input for `dnd_end_snooze`."""
    pass

class DndEndSnoozeOutput(DndEndSnoozeToolOutput):
    """Operation output for `dnd_end_snooze`."""
    pass

class SlackDndEndResource(BaseResourceClient):
    """Operations for the `dnd_end` resource."""

    @operation(
        name='dnd_end_dnd',
        title='DndEndDnd',
        input_model=DndEndDndInput,
        output_model=DndEndDndOutput,
        tools_used=('dnd_end_dnd',),
        tags=tuple(['dnd']),
    )
    async def dnd(self, data: DndEndDndInput) -> DndEndDndOutput:
        """Ends the current user's Do Not Disturb session immediately.

Important inputs: token"""
        tool = self._client.get_tool('dnd_end_dnd')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DndEndDndOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='dnd_end_snooze',
        title='DndEndSnooze',
        input_model=DndEndSnoozeInput,
        output_model=DndEndSnoozeOutput,
        tools_used=('dnd_end_snooze',),
        tags=tuple(['dnd']),
    )
    async def snooze(self, data: DndEndSnoozeInput) -> DndEndSnoozeOutput:
        """Ends the current user's snooze mode immediately.

Important inputs: token"""
        tool = self._client.get_tool('dnd_end_snooze')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DndEndSnoozeOutput.model_validate(coerce_tool_result(result))
