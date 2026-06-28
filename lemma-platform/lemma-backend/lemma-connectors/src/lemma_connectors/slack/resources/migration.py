from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import MigrationExchangeToolInput, MigrationExchangeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class MigrationExchangeInput(MigrationExchangeToolInput):
    """Operation input for `migration_exchange`."""
    pass

class MigrationExchangeOutput(MigrationExchangeToolOutput):
    """Operation output for `migration_exchange`."""
    pass

class SlackMigrationResource(BaseResourceClient):
    """Operations for the `migration` resource."""

    @operation(
        name='migration_exchange',
        title='MigrationExchange',
        input_model=MigrationExchangeInput,
        output_model=MigrationExchangeOutput,
        tools_used=('migration_exchange',),
        tags=tuple(['migration']),
    )
    async def exchange(self, data: MigrationExchangeInput) -> MigrationExchangeOutput:
        """For Enterprise Grid workspaces, map local user IDs to global user IDs.

Important inputs: token, users, team_id, to_old"""
        tool = self._client.get_tool('migration_exchange')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MigrationExchangeOutput.model_validate(coerce_tool_result(result))
