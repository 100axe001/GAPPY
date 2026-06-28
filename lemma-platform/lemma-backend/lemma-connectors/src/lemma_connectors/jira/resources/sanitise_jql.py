from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import SanitiseJqlQueriesToolInput, SanitiseJqlQueriesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SanitiseJqlQueriesInput(SanitiseJqlQueriesToolInput):
    """Operation input for `sanitise_jql_queries`."""
    pass

class SanitiseJqlQueriesOutput(SanitiseJqlQueriesToolOutput):
    """Operation output for `sanitise_jql_queries`."""
    pass

class JiraSanitiseJqlResource(BaseResourceClient):
    """Operations for the `sanitise_jql` resource."""

    @operation(
        name='sanitise_jql_queries',
        title='SanitiseJqlQueries',
        input_model=SanitiseJqlQueriesInput,
        output_model=SanitiseJqlQueriesOutput,
        tools_used=('sanitise_jql_queries',),
        tags=tuple(['JQL']),
    )
    async def queries(self, data: SanitiseJqlQueriesInput) -> SanitiseJqlQueriesOutput:
        """Sanitizes one or more JQL queries by converting readable details into IDs where a user doesn't have permission to view the entity. For example, if the query contains the clause *project = 'Secret project'*, and a user does not have browse permission for the project "Secret project", the sanitized query replaces the clause with *project = 12345"* (where 12345 is the ID of the project). If a user has the required permission, the clause is not sanitized. If the account ID is null, sanitizing is performed for an anonymous user. Note that sanitization doesn't make the queries GDPR-compliant, because it doesn't remove user identifiers (username or user key). If you need to make queries GDPR-compliant, use [Convert user identifiers to account IDs in JQL queries](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-jql/#api-rest-api-3-jql-sanitize-post). Before sanitization each JQL query is parsed. The queries are returned in the same order that they were passed. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('sanitise_jql_queries')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SanitiseJqlQueriesOutput.model_validate(coerce_tool_result(result))
