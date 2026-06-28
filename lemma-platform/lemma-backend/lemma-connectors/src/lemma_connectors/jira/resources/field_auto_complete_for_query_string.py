from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetFieldAutoCompleteForQueryStringToolInput, GetFieldAutoCompleteForQueryStringToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetFieldAutoCompleteForQueryStringInput(GetFieldAutoCompleteForQueryStringToolInput):
    """Operation input for `get_field_auto_complete_for_query_string`."""
    pass

class GetFieldAutoCompleteForQueryStringOutput(GetFieldAutoCompleteForQueryStringToolOutput):
    """Operation output for `get_field_auto_complete_for_query_string`."""
    pass

class JiraFieldAutoCompleteForQueryStringResource(BaseResourceClient):
    """Operations for the `field_auto_complete_for_query_string` resource."""

    @operation(
        name='get_field_auto_complete_for_query_string',
        title='GetFieldAutoCompleteForQueryString',
        input_model=GetFieldAutoCompleteForQueryStringInput,
        output_model=GetFieldAutoCompleteForQueryStringOutput,
        tools_used=('get_field_auto_complete_for_query_string',),
        tags=tuple(['JQL']),
    )
    async def get(self, data: GetFieldAutoCompleteForQueryStringInput) -> GetFieldAutoCompleteForQueryStringOutput:
        """Returns the JQL search auto complete suggestions for a field. Suggestions can be obtained by providing: * `fieldName` to get a list of all values for the field. * `fieldName` and `fieldValue` to get a list of values containing the text in `fieldValue`. * `fieldName` and `predicateName` to get a list of all predicate values for the field. * `fieldName`, `predicateName`, and `predicateValue` to get a list of predicate values containing the text in `predicateValue`. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: field_name, field_value, predicate_name, predicate_value"""
        tool = self._client.get_tool('get_field_auto_complete_for_query_string')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetFieldAutoCompleteForQueryStringOutput.model_validate(coerce_tool_result(result))
