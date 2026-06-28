from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import UpdateMultipleCustomFieldValuesToolInput, UpdateMultipleCustomFieldValuesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UpdateMultipleCustomFieldValuesInput(UpdateMultipleCustomFieldValuesToolInput):
    """Operation input for `update_multiple_custom_field_values`."""
    pass

class UpdateMultipleCustomFieldValuesOutput(UpdateMultipleCustomFieldValuesToolOutput):
    """Operation output for `update_multiple_custom_field_values`."""
    pass

class JiraMultipleCustomFieldValuesResource(BaseResourceClient):
    """Operations for the `multiple_custom_field_values` resource."""

    @operation(
        name='update_multiple_custom_field_values',
        title='UpdateMultipleCustomFieldValues',
        input_model=UpdateMultipleCustomFieldValuesInput,
        output_model=UpdateMultipleCustomFieldValuesOutput,
        tools_used=('update_multiple_custom_field_values',),
        tags=tuple(['Issue custom field values (apps)']),
    )
    async def update(self, data: UpdateMultipleCustomFieldValuesInput) -> UpdateMultipleCustomFieldValuesOutput:
        """Updates the value of one or more custom fields on one or more issues. Combinations of custom field and issue should be unique within the request. Custom fields can only be updated by the Forge app that created them. **[Permissions](#permissions) required:** Only the app that created the custom field can update its values with this operation.

Important inputs: generate_changelog, body"""
        tool = self._client.get_tool('update_multiple_custom_field_values')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateMultipleCustomFieldValuesOutput.model_validate(coerce_tool_result(result))
