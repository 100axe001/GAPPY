from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AssignFieldConfigurationSchemeToProjectToolInput, AssignFieldConfigurationSchemeToProjectToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AssignFieldConfigurationSchemeToProjectInput(AssignFieldConfigurationSchemeToProjectToolInput):
    """Operation input for `assign_field_configuration_scheme_to_project`."""
    pass

class AssignFieldConfigurationSchemeToProjectOutput(AssignFieldConfigurationSchemeToProjectToolOutput):
    """Operation output for `assign_field_configuration_scheme_to_project`."""
    pass

class JiraAssignFieldConfigurationSchemeToResource(BaseResourceClient):
    """Operations for the `assign_field_configuration_scheme_to` resource."""

    @operation(
        name='assign_field_configuration_scheme_to_project',
        title='AssignFieldConfigurationSchemeToProject',
        input_model=AssignFieldConfigurationSchemeToProjectInput,
        output_model=AssignFieldConfigurationSchemeToProjectOutput,
        tools_used=('assign_field_configuration_scheme_to_project',),
        tags=tuple(['Issue field configurations']),
    )
    async def project(self, data: AssignFieldConfigurationSchemeToProjectInput) -> AssignFieldConfigurationSchemeToProjectOutput:
        """Assigns a field configuration scheme to a project. If the field configuration scheme ID is `null`, the operation assigns the default field configuration scheme. Field configuration schemes can only be assigned to classic projects. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('assign_field_configuration_scheme_to_project')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AssignFieldConfigurationSchemeToProjectOutput.model_validate(coerce_tool_result(result))
