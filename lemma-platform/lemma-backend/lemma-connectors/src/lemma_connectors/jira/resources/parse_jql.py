from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import ParseJqlQueriesToolInput, ParseJqlQueriesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ParseJqlQueriesInput(ParseJqlQueriesToolInput):
    """Operation input for `parse_jql_queries`."""
    pass

class ParseJqlQueriesOutput(ParseJqlQueriesToolOutput):
    """Operation output for `parse_jql_queries`."""
    pass

class JiraParseJqlResource(BaseResourceClient):
    """Operations for the `parse_jql` resource."""

    @operation(
        name='parse_jql_queries',
        title='ParseJqlQueries',
        input_model=ParseJqlQueriesInput,
        output_model=ParseJqlQueriesOutput,
        tools_used=('parse_jql_queries',),
        tags=tuple(['JQL']),
    )
    async def queries(self, data: ParseJqlQueriesInput) -> ParseJqlQueriesOutput:
        """Parses and validates JQL queries. Validation is performed in context of the current user. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: validation, body"""
        tool = self._client.get_tool('parse_jql_queries')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ParseJqlQueriesOutput.model_validate(coerce_tool_result(result))
