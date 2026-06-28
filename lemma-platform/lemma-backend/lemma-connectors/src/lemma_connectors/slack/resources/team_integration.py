from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import TeamIntegrationLogsToolInput, TeamIntegrationLogsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class TeamIntegrationLogsInput(TeamIntegrationLogsToolInput):
    """Operation input for `team_integration_logs`."""
    pass

class TeamIntegrationLogsOutput(TeamIntegrationLogsToolOutput):
    """Operation output for `team_integration_logs`."""
    pass

class SlackTeamIntegrationResource(BaseResourceClient):
    """Operations for the `team_integration` resource."""

    @operation(
        name='team_integration_logs',
        title='TeamIntegrationLogs',
        input_model=TeamIntegrationLogsInput,
        output_model=TeamIntegrationLogsOutput,
        tools_used=('team_integration_logs',),
        tags=tuple(['team']),
    )
    async def logs(self, data: TeamIntegrationLogsInput) -> TeamIntegrationLogsOutput:
        """Gets the integration logs for the current team.

Important inputs: token, app_id, change_type, count, page, service_id, user"""
        tool = self._client.get_tool('team_integration_logs')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return TeamIntegrationLogsOutput.model_validate(coerce_tool_result(result))
