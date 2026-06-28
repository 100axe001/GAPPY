from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAutoCompletePostToolInput, GetAutoCompletePostToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAutoCompletePostInput(GetAutoCompletePostToolInput):
    """Operation input for `get_auto_complete_post`."""
    pass

class GetAutoCompletePostOutput(GetAutoCompletePostToolOutput):
    """Operation output for `get_auto_complete_post`."""
    pass

class JiraAutoCompletePostResource(BaseResourceClient):
    """Operations for the `auto_complete_post` resource."""

    @operation(
        name='get_auto_complete_post',
        title='GetAutoCompletePost',
        input_model=GetAutoCompletePostInput,
        output_model=GetAutoCompletePostOutput,
        tools_used=('get_auto_complete_post',),
        tags=tuple(['JQL']),
    )
    async def get(self, data: GetAutoCompletePostInput) -> GetAutoCompletePostOutput:
        """Returns reference data for JQL searches. This is a downloadable version of the documentation provided in [Advanced searching - fields reference](https://confluence.atlassian.com/x/gwORLQ) and [Advanced searching - functions reference](https://confluence.atlassian.com/x/hgORLQ), along with a list of JQL-reserved words. Use this information to assist with the programmatic creation of JQL queries or the validation of queries built in a custom query builder. This operation can filter the custom fields returned by project. Invalid project IDs in `projectIds` are ignored. System fields are always returned. It can also return the collapsed field for custom fields. Collapsed fields enable searches to be performed across all fields with the same name and of the same field type. For example, the collapsed field `Component - Component[Dropdown]` enables dropdown fields `Component - cf[10061]` and `Component - cf[10062]` to be searched simultaneously. **[Permissions](#permissions) required:** None.

Important inputs: body"""
        tool = self._client.get_tool('get_auto_complete_post')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAutoCompletePostOutput.model_validate(coerce_tool_result(result))
