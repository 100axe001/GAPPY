from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import UpdateCustomFieldValueToolInput, UpdateCustomFieldValueToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UpdateCustomFieldValueInput(UpdateCustomFieldValueToolInput):
    """Operation input for `update_custom_field_value`."""
    pass

class UpdateCustomFieldValueOutput(UpdateCustomFieldValueToolOutput):
    """Operation output for `update_custom_field_value`."""
    pass

class JiraCustomFieldValueResource(BaseResourceClient):
    """Operations for the `custom_field_value` resource."""

    @operation(
        name='update_custom_field_value',
        title='UpdateCustomFieldValue',
        input_model=UpdateCustomFieldValueInput,
        output_model=UpdateCustomFieldValueOutput,
        tools_used=('update_custom_field_value',),
        tags=tuple(['Issue custom field values (apps)']),
    )
    async def update(self, data: UpdateCustomFieldValueInput) -> UpdateCustomFieldValueOutput:
        """Updates the value of a custom field on one or more issues. Custom fields can only be updated by the Forge app that created them. **[Permissions](#permissions) required:** Only the app that created the custom field can update its values with this operation.

Important inputs: field_id_or_key, generate_changelog, body"""
        tool = self._client.get_tool('update_custom_field_value')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateCustomFieldValueOutput.model_validate(coerce_tool_result(result))
