from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import DndSetSnoozeToolInput, DndSetSnoozeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DndSetSnoozeInput(DndSetSnoozeToolInput):
    """Operation input for `dnd_set_snooze`."""
    pass

class DndSetSnoozeOutput(DndSetSnoozeToolOutput):
    """Operation output for `dnd_set_snooze`."""
    pass

class SlackDndSetResource(BaseResourceClient):
    """Operations for the `dnd_set` resource."""

    @operation(
        name='dnd_set_snooze',
        title='DndSetSnooze',
        input_model=DndSetSnoozeInput,
        output_model=DndSetSnoozeOutput,
        tools_used=('dnd_set_snooze',),
        tags=tuple(['dnd']),
    )
    async def snooze(self, data: DndSetSnoozeInput) -> DndSetSnoozeOutput:
        """Turns on Do Not Disturb mode for the current user, or changes its duration.

Important inputs: body"""
        tool = self._client.get_tool('dnd_set_snooze')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DndSetSnoozeOutput.model_validate(coerce_tool_result(result))
