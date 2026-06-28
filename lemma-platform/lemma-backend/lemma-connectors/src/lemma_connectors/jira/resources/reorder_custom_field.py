from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import ReorderCustomFieldOptionsToolInput, ReorderCustomFieldOptionsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ReorderCustomFieldOptionsInput(ReorderCustomFieldOptionsToolInput):
    """Operation input for `reorder_custom_field_options`."""
    pass

class ReorderCustomFieldOptionsOutput(ReorderCustomFieldOptionsToolOutput):
    """Operation output for `reorder_custom_field_options`."""
    pass

class JiraReorderCustomFieldResource(BaseResourceClient):
    """Operations for the `reorder_custom_field` resource."""

    @operation(
        name='reorder_custom_field_options',
        title='ReorderCustomFieldOptions',
        input_model=ReorderCustomFieldOptionsInput,
        output_model=ReorderCustomFieldOptionsOutput,
        tools_used=('reorder_custom_field_options',),
        tags=tuple(['Issue custom field options']),
    )
    async def options(self, data: ReorderCustomFieldOptionsInput) -> ReorderCustomFieldOptionsOutput:
        """Changes the order of custom field options or cascading options in a context. This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.** **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, context_id, body"""
        tool = self._client.get_tool('reorder_custom_field_options')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ReorderCustomFieldOptionsOutput.model_validate(coerce_tool_result(result))
