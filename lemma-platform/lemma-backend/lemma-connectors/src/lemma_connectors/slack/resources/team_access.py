from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import TeamAccessLogsToolInput, TeamAccessLogsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class TeamAccessLogsInput(TeamAccessLogsToolInput):
    """Operation input for `team_access_logs`."""
    pass

class TeamAccessLogsOutput(TeamAccessLogsToolOutput):
    """Operation output for `team_access_logs`."""
    pass

class SlackTeamAccessResource(BaseResourceClient):
    """Operations for the `team_access` resource."""

    @operation(
        name='team_access_logs',
        title='TeamAccessLogs',
        input_model=TeamAccessLogsInput,
        output_model=TeamAccessLogsOutput,
        tools_used=('team_access_logs',),
        tags=tuple(['team']),
    )
    async def logs(self, data: TeamAccessLogsInput) -> TeamAccessLogsOutput:
        """Gets the access logs for the current team.

Important inputs: token, before, count, page"""
        tool = self._client.get_tool('team_access_logs')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return TeamAccessLogsOutput.model_validate(coerce_tool_result(result))
