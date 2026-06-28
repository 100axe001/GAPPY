from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import TeamBillableInfoToolInput, TeamBillableInfoToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class TeamBillableInfoInput(TeamBillableInfoToolInput):
    """Operation input for `team_billable_info`."""
    pass

class TeamBillableInfoOutput(TeamBillableInfoToolOutput):
    """Operation output for `team_billable_info`."""
    pass

class SlackTeamBillableResource(BaseResourceClient):
    """Operations for the `team_billable` resource."""

    @operation(
        name='team_billable_info',
        title='TeamBillableInfo',
        input_model=TeamBillableInfoInput,
        output_model=TeamBillableInfoOutput,
        tools_used=('team_billable_info',),
        tags=tuple(['team']),
    )
    async def info(self, data: TeamBillableInfoInput) -> TeamBillableInfoOutput:
        """Gets billable users information for the current team.

Important inputs: token, user"""
        tool = self._client.get_tool('team_billable_info')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return TeamBillableInfoOutput.model_validate(coerce_tool_result(result))
