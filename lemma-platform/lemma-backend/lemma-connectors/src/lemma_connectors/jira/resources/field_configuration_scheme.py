from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateFieldConfigurationSchemeToolInput, CreateFieldConfigurationSchemeToolOutput, DeleteFieldConfigurationSchemeToolInput, DeleteFieldConfigurationSchemeToolOutput, UpdateFieldConfigurationSchemeToolInput, UpdateFieldConfigurationSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateFieldConfigurationSchemeInput(CreateFieldConfigurationSchemeToolInput):
    """Operation input for `create_field_configuration_scheme`."""
    pass

class CreateFieldConfigurationSchemeOutput(CreateFieldConfigurationSchemeToolOutput):
    """Operation output for `create_field_configuration_scheme`."""
    pass

class DeleteFieldConfigurationSchemeInput(DeleteFieldConfigurationSchemeToolInput):
    """Operation input for `delete_field_configuration_scheme`."""
    pass

class DeleteFieldConfigurationSchemeOutput(DeleteFieldConfigurationSchemeToolOutput):
    """Operation output for `delete_field_configuration_scheme`."""
    pass

class UpdateFieldConfigurationSchemeInput(UpdateFieldConfigurationSchemeToolInput):
    """Operation input for `update_field_configuration_scheme`."""
    pass

class UpdateFieldConfigurationSchemeOutput(UpdateFieldConfigurationSchemeToolOutput):
    """Operation output for `update_field_configuration_scheme`."""
    pass

class JiraFieldConfigurationSchemeResource(BaseResourceClient):
    """Operations for the `field_configuration_scheme` resource."""

    @operation(
        name='create_field_configuration_scheme',
        title='CreateFieldConfigurationScheme',
        input_model=CreateFieldConfigurationSchemeInput,
        output_model=CreateFieldConfigurationSchemeOutput,
        tools_used=('create_field_configuration_scheme',),
        tags=tuple(['Issue field configurations']),
    )
    async def create(self, data: CreateFieldConfigurationSchemeInput) -> CreateFieldConfigurationSchemeOutput:
        """Creates a field configuration scheme. This operation can only create field configuration schemes used in company-managed (classic) projects. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_field_configuration_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateFieldConfigurationSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_field_configuration_scheme',
        title='DeleteFieldConfigurationScheme',
        input_model=DeleteFieldConfigurationSchemeInput,
        output_model=DeleteFieldConfigurationSchemeOutput,
        tools_used=('delete_field_configuration_scheme',),
        tags=tuple(['Issue field configurations']),
    )
    async def delete(self, data: DeleteFieldConfigurationSchemeInput) -> DeleteFieldConfigurationSchemeOutput:
        """Deletes a field configuration scheme. This operation can only delete field configuration schemes used in company-managed (classic) projects. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('delete_field_configuration_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteFieldConfigurationSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_field_configuration_scheme',
        title='UpdateFieldConfigurationScheme',
        input_model=UpdateFieldConfigurationSchemeInput,
        output_model=UpdateFieldConfigurationSchemeOutput,
        tools_used=('update_field_configuration_scheme',),
        tags=tuple(['Issue field configurations']),
    )
    async def update(self, data: UpdateFieldConfigurationSchemeInput) -> UpdateFieldConfigurationSchemeOutput:
        """Updates a field configuration scheme. This operation can only update field configuration schemes used in company-managed (classic) projects. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('update_field_configuration_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateFieldConfigurationSchemeOutput.model_validate(coerce_tool_result(result))
