from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import SetFieldConfigurationSchemeMappingToolInput, SetFieldConfigurationSchemeMappingToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SetFieldConfigurationSchemeMappingInput(SetFieldConfigurationSchemeMappingToolInput):
    """Operation input for `set_field_configuration_scheme_mapping`."""
    pass

class SetFieldConfigurationSchemeMappingOutput(SetFieldConfigurationSchemeMappingToolOutput):
    """Operation output for `set_field_configuration_scheme_mapping`."""
    pass

class JiraFieldConfigurationSchemeMappingResource(BaseResourceClient):
    """Operations for the `field_configuration_scheme_mapping` resource."""

    @operation(
        name='set_field_configuration_scheme_mapping',
        title='SetFieldConfigurationSchemeMapping',
        input_model=SetFieldConfigurationSchemeMappingInput,
        output_model=SetFieldConfigurationSchemeMappingOutput,
        tools_used=('set_field_configuration_scheme_mapping',),
        tags=tuple(['Issue field configurations']),
    )
    async def set(self, data: SetFieldConfigurationSchemeMappingInput) -> SetFieldConfigurationSchemeMappingOutput:
        """Assigns issue types to field configurations on field configuration scheme. This operation can only modify field configuration schemes used in company-managed (classic) projects. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('set_field_configuration_scheme_mapping')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetFieldConfigurationSchemeMappingOutput.model_validate(coerce_tool_result(result))
