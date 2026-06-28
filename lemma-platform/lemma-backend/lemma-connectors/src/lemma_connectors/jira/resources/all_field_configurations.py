from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllFieldConfigurationsToolInput, GetAllFieldConfigurationsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllFieldConfigurationsInput(GetAllFieldConfigurationsToolInput):
    """Operation input for `get_all_field_configurations`."""
    pass

class GetAllFieldConfigurationsOutput(GetAllFieldConfigurationsToolOutput):
    """Operation output for `get_all_field_configurations`."""
    pass

class JiraAllFieldConfigurationsResource(BaseResourceClient):
    """Operations for the `all_field_configurations` resource."""

    @operation(
        name='get_all_field_configurations',
        title='GetAllFieldConfigurations',
        input_model=GetAllFieldConfigurationsInput,
        output_model=GetAllFieldConfigurationsOutput,
        tools_used=('get_all_field_configurations',),
        tags=tuple(['Issue field configurations']),
    )
    async def get(self, data: GetAllFieldConfigurationsInput) -> GetAllFieldConfigurationsOutput:
        """Returns a [paginated](#pagination) list of field configurations. The list can be for all field configurations or a subset determined by any combination of these criteria: * a list of field configuration item IDs. * whether the field configuration is a default. * whether the field configuration name or description contains a query string. Only field configurations used in company-managed (classic) projects are returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, id, is_default, query"""
        tool = self._client.get_tool('get_all_field_configurations')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllFieldConfigurationsOutput.model_validate(coerce_tool_result(result))
