from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import TeamInfoToolInput, TeamInfoToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class TeamInfoInput(TeamInfoToolInput):
    """Operation input for `team_info`."""
    pass

class TeamInfoOutput(TeamInfoToolOutput):
    """Operation output for `team_info`."""
    pass

class SlackTeamResource(BaseResourceClient):
    """Operations for the `team` resource."""

    @operation(
        name='team_info',
        title='TeamInfo',
        input_model=TeamInfoInput,
        output_model=TeamInfoOutput,
        tools_used=('team_info',),
        tags=tuple(['team']),
    )
    async def info(self, data: TeamInfoInput) -> TeamInfoOutput:
        """Gets information about the current team.

Important inputs: token, team"""
        tool = self._client.get_tool('team_info')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return TeamInfoOutput.model_validate(coerce_tool_result(result))
