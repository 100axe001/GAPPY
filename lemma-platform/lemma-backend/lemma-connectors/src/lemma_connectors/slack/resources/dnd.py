from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import DndInfoToolInput, DndInfoToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DndInfoInput(DndInfoToolInput):
    """Operation input for `dnd_info`."""
    pass

class DndInfoOutput(DndInfoToolOutput):
    """Operation output for `dnd_info`."""
    pass

class SlackDndResource(BaseResourceClient):
    """Operations for the `dnd` resource."""

    @operation(
        name='dnd_info',
        title='DndInfo',
        input_model=DndInfoInput,
        output_model=DndInfoOutput,
        tools_used=('dnd_info',),
        tags=tuple(['dnd']),
    )
    async def info(self, data: DndInfoInput) -> DndInfoOutput:
        """Retrieves a user's current Do Not Disturb status.

Important inputs: token, user"""
        tool = self._client.get_tool('dnd_info')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DndInfoOutput.model_validate(coerce_tool_result(result))
