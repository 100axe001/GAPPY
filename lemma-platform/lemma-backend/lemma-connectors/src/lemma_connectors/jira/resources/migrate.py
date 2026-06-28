from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import MigrateQueriesToolInput, MigrateQueriesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class MigrateQueriesInput(MigrateQueriesToolInput):
    """Operation input for `migrate_queries`."""
    pass

class MigrateQueriesOutput(MigrateQueriesToolOutput):
    """Operation output for `migrate_queries`."""
    pass

class JiraMigrateResource(BaseResourceClient):
    """Operations for the `migrate` resource."""

    @operation(
        name='migrate_queries',
        title='MigrateQueries',
        input_model=MigrateQueriesInput,
        output_model=MigrateQueriesOutput,
        tools_used=('migrate_queries',),
        tags=tuple(['JQL']),
    )
    async def queries(self, data: MigrateQueriesInput) -> MigrateQueriesOutput:
        """Converts one or more JQL queries with user identifiers (username or user key) to equivalent JQL queries with account IDs. You may wish to use this operation if your system stores JQL queries and you want to make them GDPR-compliant. For more information about GDPR-related changes, see the [migration guide](https://developer.atlassian.com/cloud/jira/platform/deprecation-notice-user-privacy-api-migration-guide/). **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: body"""
        tool = self._client.get_tool('migrate_queries')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MigrateQueriesOutput.model_validate(coerce_tool_result(result))
