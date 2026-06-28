from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAutoCompleteToolInput, GetAutoCompleteToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAutoCompleteInput(GetAutoCompleteToolInput):
    """Operation input for `get_auto_complete`."""
    pass

class GetAutoCompleteOutput(GetAutoCompleteToolOutput):
    """Operation output for `get_auto_complete`."""
    pass

class JiraAutoCompleteResource(BaseResourceClient):
    """Operations for the `auto_complete` resource."""

    @operation(
        name='get_auto_complete',
        title='GetAutoComplete',
        input_model=GetAutoCompleteInput,
        output_model=GetAutoCompleteOutput,
        tools_used=('get_auto_complete',),
        tags=tuple(['JQL']),
    )
    async def get(self, data: GetAutoCompleteInput) -> GetAutoCompleteOutput:
        """Returns reference data for JQL searches. This is a downloadable version of the documentation provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL queries or the validation of queries built in a custom query builder. To filter visible field details by project or collapse non-unique fields by field type then [Get field reference data (POST)](#api-rest-api-3-jql-autocompletedata-post) can be used. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_auto_complete')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAutoCompleteOutput.model_validate(coerce_tool_result(result))
