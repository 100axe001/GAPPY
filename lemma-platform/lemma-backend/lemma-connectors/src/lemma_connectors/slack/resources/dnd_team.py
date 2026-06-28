from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import DndTeamInfoToolInput, DndTeamInfoToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DndTeamInfoInput(DndTeamInfoToolInput):
    """Operation input for `dnd_team_info`."""
    pass

class DndTeamInfoOutput(DndTeamInfoToolOutput):
    """Operation output for `dnd_team_info`."""
    pass

class SlackDndTeamResource(BaseResourceClient):
    """Operations for the `dnd_team` resource."""

    @operation(
        name='dnd_team_info',
        title='DndTeamInfo',
        input_model=DndTeamInfoInput,
        output_model=DndTeamInfoOutput,
        tools_used=('dnd_team_info',),
        tags=tuple(['dnd']),
    )
    async def info(self, data: DndTeamInfoInput) -> DndTeamInfoOutput:
        """Retrieves the Do Not Disturb status for up to 50 users on a team.

Important inputs: token, users"""
        tool = self._client.get_tool('dnd_team_info')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DndTeamInfoOutput.model_validate(coerce_tool_result(result))
