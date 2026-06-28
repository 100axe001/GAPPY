from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import BulkGetUsersMigrationToolInput, BulkGetUsersMigrationToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class BulkGetUsersMigrationInput(BulkGetUsersMigrationToolInput):
    """Operation input for `bulk_get_users_migration`."""
    pass

class BulkGetUsersMigrationOutput(BulkGetUsersMigrationToolOutput):
    """Operation output for `bulk_get_users_migration`."""
    pass

class JiraBulkGetUsersResource(BaseResourceClient):
    """Operations for the `bulk_get_users` resource."""

    @operation(
        name='bulk_get_users_migration',
        title='BulkGetUsersMigration',
        input_model=BulkGetUsersMigrationInput,
        output_model=BulkGetUsersMigrationOutput,
        tools_used=('bulk_get_users_migration',),
        tags=tuple(['Users']),
    )
    async def migration(self, data: BulkGetUsersMigrationInput) -> BulkGetUsersMigrationOutput:
        """Returns the account IDs for the users specified in the `key` or `username` parameters. Note that multiple `key` or `username` parameters can be specified. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: start_at, max_results, username"""
        tool = self._client.get_tool('bulk_get_users_migration')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return BulkGetUsersMigrationOutput.model_validate(coerce_tool_result(result))
