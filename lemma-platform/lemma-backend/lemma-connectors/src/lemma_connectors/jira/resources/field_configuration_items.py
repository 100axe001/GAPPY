from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetFieldConfigurationItemsToolInput, GetFieldConfigurationItemsToolOutput, UpdateFieldConfigurationItemsToolInput, UpdateFieldConfigurationItemsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetFieldConfigurationItemsInput(GetFieldConfigurationItemsToolInput):
    """Operation input for `get_field_configuration_items`."""
    pass

class GetFieldConfigurationItemsOutput(GetFieldConfigurationItemsToolOutput):
    """Operation output for `get_field_configuration_items`."""
    pass

class UpdateFieldConfigurationItemsInput(UpdateFieldConfigurationItemsToolInput):
    """Operation input for `update_field_configuration_items`."""
    pass

class UpdateFieldConfigurationItemsOutput(UpdateFieldConfigurationItemsToolOutput):
    """Operation output for `update_field_configuration_items`."""
    pass

class JiraFieldConfigurationItemsResource(BaseResourceClient):
    """Operations for the `field_configuration_items` resource."""

    @operation(
        name='get_field_configuration_items',
        title='GetFieldConfigurationItems',
        input_model=GetFieldConfigurationItemsInput,
        output_model=GetFieldConfigurationItemsOutput,
        tools_used=('get_field_configuration_items',),
        tags=tuple(['Issue field configurations']),
    )
    async def get(self, data: GetFieldConfigurationItemsInput) -> GetFieldConfigurationItemsOutput:
        """Returns a [paginated](#pagination) list of all fields for a configuration. Only the fields from configurations used in company-managed (classic) projects are returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, start_at, max_results"""
        tool = self._client.get_tool('get_field_configuration_items')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetFieldConfigurationItemsOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_field_configuration_items',
        title='UpdateFieldConfigurationItems',
        input_model=UpdateFieldConfigurationItemsInput,
        output_model=UpdateFieldConfigurationItemsOutput,
        tools_used=('update_field_configuration_items',),
        tags=tuple(['Issue field configurations']),
    )
    async def update(self, data: UpdateFieldConfigurationItemsInput) -> UpdateFieldConfigurationItemsOutput:
        """Updates fields in a field configuration. The properties of the field configuration fields provided override the existing values. This operation can only update field configurations used in company-managed (classic) projects. The operation can set the renderer for text fields to the default text renderer (`text-renderer`) or wiki style renderer (`wiki-renderer`). However, the renderer cannot be updated for fields using the autocomplete renderer (`autocomplete-renderer`). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('update_field_configuration_items')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateFieldConfigurationItemsOutput.model_validate(coerce_tool_result(result))
