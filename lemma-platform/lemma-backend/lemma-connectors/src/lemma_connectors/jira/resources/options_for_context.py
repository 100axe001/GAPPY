from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetOptionsForContextToolInput, GetOptionsForContextToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetOptionsForContextInput(GetOptionsForContextToolInput):
    """Operation input for `get_options_for_context`."""
    pass

class GetOptionsForContextOutput(GetOptionsForContextToolOutput):
    """Operation output for `get_options_for_context`."""
    pass

class JiraOptionsForContextResource(BaseResourceClient):
    """Operations for the `options_for_context` resource."""

    @operation(
        name='get_options_for_context',
        title='GetOptionsForContext',
        input_model=GetOptionsForContextInput,
        output_model=GetOptionsForContextOutput,
        tools_used=('get_options_for_context',),
        tags=tuple(['Issue custom field options']),
    )
    async def get(self, data: GetOptionsForContextInput) -> GetOptionsForContextOutput:
        """Returns a [paginated](#pagination) list of all custom field option for a context. Options are returned first then cascading options, in the order they display in Jira. This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.** **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, context_id, option_id, only_options, start_at, max_results"""
        tool = self._client.get_tool('get_options_for_context')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetOptionsForContextOutput.model_validate(coerce_tool_result(result))
