from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetContextsForFieldToolInput, GetContextsForFieldToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetContextsForFieldInput(GetContextsForFieldToolInput):
    """Operation input for `get_contexts_for_field`."""
    pass

class GetContextsForFieldOutput(GetContextsForFieldToolOutput):
    """Operation output for `get_contexts_for_field`."""
    pass

class JiraContextsForFieldResource(BaseResourceClient):
    """Operations for the `contexts_for_field` resource."""

    @operation(
        name='get_contexts_for_field',
        title='GetContextsForField',
        input_model=GetContextsForFieldInput,
        output_model=GetContextsForFieldOutput,
        tools_used=('get_contexts_for_field',),
        tags=tuple(['Issue custom field contexts']),
    )
    async def get(self, data: GetContextsForFieldInput) -> GetContextsForFieldOutput:
        """Returns a [paginated](#pagination) list of [ contexts](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html) for a custom field. Contexts can be returned as follows: * With no other parameters set, all contexts. * By defining `id` only, all contexts from the list of IDs. * By defining `isAnyIssueType`, limit the list of contexts returned to either those that apply to all issue types (true) or those that apply to only a subset of issue types (false) * By defining `isGlobalContext`, limit the list of contexts return to either those that apply to all projects (global contexts) (true) or those that apply to only a subset of projects (false). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, is_any_issue_type, is_global_context, context_id, start_at, max_results"""
        tool = self._client.get_tool('get_contexts_for_field')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetContextsForFieldOutput.model_validate(coerce_tool_result(result))
