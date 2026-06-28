from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateFieldConfigurationToolInput, CreateFieldConfigurationToolOutput, DeleteFieldConfigurationToolInput, DeleteFieldConfigurationToolOutput, UpdateFieldConfigurationToolInput, UpdateFieldConfigurationToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateFieldConfigurationInput(CreateFieldConfigurationToolInput):
    """Operation input for `create_field_configuration`."""
    pass

class CreateFieldConfigurationOutput(CreateFieldConfigurationToolOutput):
    """Operation output for `create_field_configuration`."""
    pass

class DeleteFieldConfigurationInput(DeleteFieldConfigurationToolInput):
    """Operation input for `delete_field_configuration`."""
    pass

class DeleteFieldConfigurationOutput(DeleteFieldConfigurationToolOutput):
    """Operation output for `delete_field_configuration`."""
    pass

class UpdateFieldConfigurationInput(UpdateFieldConfigurationToolInput):
    """Operation input for `update_field_configuration`."""
    pass

class UpdateFieldConfigurationOutput(UpdateFieldConfigurationToolOutput):
    """Operation output for `update_field_configuration`."""
    pass

class JiraFieldConfigurationResource(BaseResourceClient):
    """Operations for the `field_configuration` resource."""

    @operation(
        name='create_field_configuration',
        title='CreateFieldConfiguration',
        input_model=CreateFieldConfigurationInput,
        output_model=CreateFieldConfigurationOutput,
        tools_used=('create_field_configuration',),
        tags=tuple(['Issue field configurations']),
    )
    async def create(self, data: CreateFieldConfigurationInput) -> CreateFieldConfigurationOutput:
        """Creates a field configuration. The field configuration is created with the same field properties as the default configuration, with all the fields being optional. This operation can only create configurations for use in company-managed (classic) projects. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_field_configuration')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateFieldConfigurationOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_field_configuration',
        title='DeleteFieldConfiguration',
        input_model=DeleteFieldConfigurationInput,
        output_model=DeleteFieldConfigurationOutput,
        tools_used=('delete_field_configuration',),
        tags=tuple(['Issue field configurations']),
    )
    async def delete(self, data: DeleteFieldConfigurationInput) -> DeleteFieldConfigurationOutput:
        """Deletes a field configuration. This operation can only delete configurations used in company-managed (classic) projects. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('delete_field_configuration')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteFieldConfigurationOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_field_configuration',
        title='UpdateFieldConfiguration',
        input_model=UpdateFieldConfigurationInput,
        output_model=UpdateFieldConfigurationOutput,
        tools_used=('update_field_configuration',),
        tags=tuple(['Issue field configurations']),
    )
    async def update(self, data: UpdateFieldConfigurationInput) -> UpdateFieldConfigurationOutput:
        """Updates a field configuration. The name and the description provided in the request override the existing values. This operation can only update configurations used in company-managed (classic) projects. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('update_field_configuration')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateFieldConfigurationOutput.model_validate(coerce_tool_result(result))
