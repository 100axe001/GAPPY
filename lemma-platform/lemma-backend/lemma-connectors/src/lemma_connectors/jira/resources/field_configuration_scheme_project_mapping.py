from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetFieldConfigurationSchemeProjectMappingToolInput, GetFieldConfigurationSchemeProjectMappingToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetFieldConfigurationSchemeProjectMappingInput(GetFieldConfigurationSchemeProjectMappingToolInput):
    """Operation input for `get_field_configuration_scheme_project_mapping`."""
    pass

class GetFieldConfigurationSchemeProjectMappingOutput(GetFieldConfigurationSchemeProjectMappingToolOutput):
    """Operation output for `get_field_configuration_scheme_project_mapping`."""
    pass

class JiraFieldConfigurationSchemeProjectMappingResource(BaseResourceClient):
    """Operations for the `field_configuration_scheme_project_mapping` resource."""

    @operation(
        name='get_field_configuration_scheme_project_mapping',
        title='GetFieldConfigurationSchemeProjectMapping',
        input_model=GetFieldConfigurationSchemeProjectMappingInput,
        output_model=GetFieldConfigurationSchemeProjectMappingOutput,
        tools_used=('get_field_configuration_scheme_project_mapping',),
        tags=tuple(['Issue field configurations']),
    )
    async def get(self, data: GetFieldConfigurationSchemeProjectMappingInput) -> GetFieldConfigurationSchemeProjectMappingOutput:
        """Returns a [paginated](#pagination) list of field configuration schemes and, for each scheme, a list of the projects that use it. The list is sorted by field configuration scheme ID. The first item contains the list of project IDs assigned to the default field configuration scheme. Only field configuration schemes used in classic projects are returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, project_id"""
        tool = self._client.get_tool('get_field_configuration_scheme_project_mapping')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetFieldConfigurationSchemeProjectMappingOutput.model_validate(coerce_tool_result(result))
