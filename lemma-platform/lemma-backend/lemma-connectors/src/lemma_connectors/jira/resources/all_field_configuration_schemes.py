from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllFieldConfigurationSchemesToolInput, GetAllFieldConfigurationSchemesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllFieldConfigurationSchemesInput(GetAllFieldConfigurationSchemesToolInput):
    """Operation input for `get_all_field_configuration_schemes`."""
    pass

class GetAllFieldConfigurationSchemesOutput(GetAllFieldConfigurationSchemesToolOutput):
    """Operation output for `get_all_field_configuration_schemes`."""
    pass

class JiraAllFieldConfigurationSchemesResource(BaseResourceClient):
    """Operations for the `all_field_configuration_schemes` resource."""

    @operation(
        name='get_all_field_configuration_schemes',
        title='GetAllFieldConfigurationSchemes',
        input_model=GetAllFieldConfigurationSchemesInput,
        output_model=GetAllFieldConfigurationSchemesOutput,
        tools_used=('get_all_field_configuration_schemes',),
        tags=tuple(['Issue field configurations']),
    )
    async def get(self, data: GetAllFieldConfigurationSchemesInput) -> GetAllFieldConfigurationSchemesOutput:
        """Returns a [paginated](#pagination) list of field configuration schemes. Only field configuration schemes used in classic projects are returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, id"""
        tool = self._client.get_tool('get_all_field_configuration_schemes')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllFieldConfigurationSchemesOutput.model_validate(coerce_tool_result(result))
