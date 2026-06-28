from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetFieldConfigurationSchemeMappingsToolInput, GetFieldConfigurationSchemeMappingsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetFieldConfigurationSchemeMappingsInput(GetFieldConfigurationSchemeMappingsToolInput):
    """Operation input for `get_field_configuration_scheme_mappings`."""
    pass

class GetFieldConfigurationSchemeMappingsOutput(GetFieldConfigurationSchemeMappingsToolOutput):
    """Operation output for `get_field_configuration_scheme_mappings`."""
    pass

class JiraFieldConfigurationSchemeMappingsResource(BaseResourceClient):
    """Operations for the `field_configuration_scheme_mappings` resource."""

    @operation(
        name='get_field_configuration_scheme_mappings',
        title='GetFieldConfigurationSchemeMappings',
        input_model=GetFieldConfigurationSchemeMappingsInput,
        output_model=GetFieldConfigurationSchemeMappingsOutput,
        tools_used=('get_field_configuration_scheme_mappings',),
        tags=tuple(['Issue field configurations']),
    )
    async def get(self, data: GetFieldConfigurationSchemeMappingsInput) -> GetFieldConfigurationSchemeMappingsOutput:
        """Returns a [paginated](#pagination) list of field configuration issue type items. Only items used in classic projects are returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, field_configuration_scheme_id"""
        tool = self._client.get_tool('get_field_configuration_scheme_mappings')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetFieldConfigurationSchemeMappingsOutput.model_validate(coerce_tool_result(result))
