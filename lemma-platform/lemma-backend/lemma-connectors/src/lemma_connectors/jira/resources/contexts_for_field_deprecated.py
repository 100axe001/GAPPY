from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetContextsForFieldDeprecatedToolInput, GetContextsForFieldDeprecatedToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetContextsForFieldDeprecatedInput(GetContextsForFieldDeprecatedToolInput):
    """Operation input for `get_contexts_for_field_deprecated`."""
    pass

class GetContextsForFieldDeprecatedOutput(GetContextsForFieldDeprecatedToolOutput):
    """Operation output for `get_contexts_for_field_deprecated`."""
    pass

class JiraContextsForFieldDeprecatedResource(BaseResourceClient):
    """Operations for the `contexts_for_field_deprecated` resource."""

    @operation(
        name='get_contexts_for_field_deprecated',
        title='GetContextsForFieldDeprecated',
        input_model=GetContextsForFieldDeprecatedInput,
        output_model=GetContextsForFieldDeprecatedOutput,
        tools_used=('get_contexts_for_field_deprecated',),
        tags=tuple(['Issue fields']),
    )
    async def get(self, data: GetContextsForFieldDeprecatedInput) -> GetContextsForFieldDeprecatedOutput:
        """Returns a [paginated](#pagination) list of the contexts a field is used in. Deprecated, use [ Get custom field contexts](#api-rest-api-3-field-fieldId-context-get). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, start_at, max_results"""
        tool = self._client.get_tool('get_contexts_for_field_deprecated')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetContextsForFieldDeprecatedOutput.model_validate(coerce_tool_result(result))
