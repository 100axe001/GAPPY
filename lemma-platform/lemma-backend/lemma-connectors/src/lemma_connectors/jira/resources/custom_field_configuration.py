from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetCustomFieldConfigurationToolInput, GetCustomFieldConfigurationToolOutput, UpdateCustomFieldConfigurationToolInput, UpdateCustomFieldConfigurationToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetCustomFieldConfigurationInput(GetCustomFieldConfigurationToolInput):
    """Operation input for `get_custom_field_configuration`."""
    pass

class GetCustomFieldConfigurationOutput(GetCustomFieldConfigurationToolOutput):
    """Operation output for `get_custom_field_configuration`."""
    pass

class UpdateCustomFieldConfigurationInput(UpdateCustomFieldConfigurationToolInput):
    """Operation input for `update_custom_field_configuration`."""
    pass

class UpdateCustomFieldConfigurationOutput(UpdateCustomFieldConfigurationToolOutput):
    """Operation output for `update_custom_field_configuration`."""
    pass

class JiraCustomFieldConfigurationResource(BaseResourceClient):
    """Operations for the `custom_field_configuration` resource."""

    @operation(
        name='get_custom_field_configuration',
        title='GetCustomFieldConfiguration',
        input_model=GetCustomFieldConfigurationInput,
        output_model=GetCustomFieldConfigurationOutput,
        tools_used=('get_custom_field_configuration',),
        tags=tuple(['Issue custom field configuration (apps)']),
    )
    async def get(self, data: GetCustomFieldConfigurationInput) -> GetCustomFieldConfigurationOutput:
        """Returns a [paginated](#pagination) list of configurations for a custom field created by a [Forge app](https://developer.atlassian.com/platform/forge/). The result can be filtered by one of these criteria: * `id`. * `fieldContextId`. * `issueId`. * `projectKeyOrId` and `issueTypeId`. Otherwise, all configurations are returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the Forge app that created the custom field.

Important inputs: field_id_or_key, id, field_context_id, issue_id, project_key_or_id, issue_type_id, start_at, max_results"""
        tool = self._client.get_tool('get_custom_field_configuration')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetCustomFieldConfigurationOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_custom_field_configuration',
        title='UpdateCustomFieldConfiguration',
        input_model=UpdateCustomFieldConfigurationInput,
        output_model=UpdateCustomFieldConfigurationOutput,
        tools_used=('update_custom_field_configuration',),
        tags=tuple(['Issue custom field configuration (apps)']),
    )
    async def update(self, data: UpdateCustomFieldConfigurationInput) -> UpdateCustomFieldConfigurationOutput:
        """Update the configuration for contexts of a custom field created by a [Forge app](https://developer.atlassian.com/platform/forge/). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the Forge app that created the custom field.

Important inputs: field_id_or_key, body"""
        tool = self._client.get_tool('update_custom_field_configuration')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateCustomFieldConfigurationOutput.model_validate(coerce_tool_result(result))
