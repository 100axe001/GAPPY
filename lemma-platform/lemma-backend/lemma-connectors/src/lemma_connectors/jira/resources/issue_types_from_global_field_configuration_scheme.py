from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import RemoveIssueTypesFromGlobalFieldConfigurationSchemeToolInput, RemoveIssueTypesFromGlobalFieldConfigurationSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class RemoveIssueTypesFromGlobalFieldConfigurationSchemeInput(RemoveIssueTypesFromGlobalFieldConfigurationSchemeToolInput):
    """Operation input for `remove_issue_types_from_global_field_configuration_scheme`."""
    pass

class RemoveIssueTypesFromGlobalFieldConfigurationSchemeOutput(RemoveIssueTypesFromGlobalFieldConfigurationSchemeToolOutput):
    """Operation output for `remove_issue_types_from_global_field_configuration_scheme`."""
    pass

class JiraIssueTypesFromGlobalFieldConfigurationSchemeResource(BaseResourceClient):
    """Operations for the `issue_types_from_global_field_configuration_scheme` resource."""

    @operation(
        name='remove_issue_types_from_global_field_configuration_scheme',
        title='RemoveIssueTypesFromGlobalFieldConfigurationScheme',
        input_model=RemoveIssueTypesFromGlobalFieldConfigurationSchemeInput,
        output_model=RemoveIssueTypesFromGlobalFieldConfigurationSchemeOutput,
        tools_used=('remove_issue_types_from_global_field_configuration_scheme',),
        tags=tuple(['Issue field configurations']),
    )
    async def remove(self, data: RemoveIssueTypesFromGlobalFieldConfigurationSchemeInput) -> RemoveIssueTypesFromGlobalFieldConfigurationSchemeOutput:
        """Removes issue types from the field configuration scheme. This operation can only modify field configuration schemes used in company-managed (classic) projects. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('remove_issue_types_from_global_field_configuration_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemoveIssueTypesFromGlobalFieldConfigurationSchemeOutput.model_validate(coerce_tool_result(result))
