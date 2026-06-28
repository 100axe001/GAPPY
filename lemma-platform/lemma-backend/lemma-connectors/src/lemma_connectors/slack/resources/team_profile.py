from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import TeamProfileGetToolInput, TeamProfileGetToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class TeamProfileGetInput(TeamProfileGetToolInput):
    """Operation input for `team_profile_get`."""
    pass

class TeamProfileGetOutput(TeamProfileGetToolOutput):
    """Operation output for `team_profile_get`."""
    pass

class SlackTeamProfileResource(BaseResourceClient):
    """Operations for the `team_profile` resource."""

    @operation(
        name='team_profile_get',
        title='TeamProfileGet',
        input_model=TeamProfileGetInput,
        output_model=TeamProfileGetOutput,
        tools_used=('team_profile_get',),
        tags=tuple(['team.profile', 'team']),
    )
    async def get(self, data: TeamProfileGetInput) -> TeamProfileGetOutput:
        """Retrieve a team's profile.

Important inputs: token, visibility"""
        tool = self._client.get_tool('team_profile_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return TeamProfileGetOutput.model_validate(coerce_tool_result(result))
