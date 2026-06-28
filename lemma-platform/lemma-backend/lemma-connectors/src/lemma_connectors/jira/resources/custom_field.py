from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateCustomFieldToolInput, CreateCustomFieldToolOutput, DeleteCustomFieldToolInput, DeleteCustomFieldToolOutput, RestoreCustomFieldToolInput, RestoreCustomFieldToolOutput, TrashCustomFieldToolInput, TrashCustomFieldToolOutput, UpdateCustomFieldToolInput, UpdateCustomFieldToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateCustomFieldInput(CreateCustomFieldToolInput):
    """Operation input for `create_custom_field`."""
    pass

class CreateCustomFieldOutput(CreateCustomFieldToolOutput):
    """Operation output for `create_custom_field`."""
    pass

class DeleteCustomFieldInput(DeleteCustomFieldToolInput):
    """Operation input for `delete_custom_field`."""
    pass

class DeleteCustomFieldOutput(DeleteCustomFieldToolOutput):
    """Operation output for `delete_custom_field`."""
    pass

class RestoreCustomFieldInput(RestoreCustomFieldToolInput):
    """Operation input for `restore_custom_field`."""
    pass

class RestoreCustomFieldOutput(RestoreCustomFieldToolOutput):
    """Operation output for `restore_custom_field`."""
    pass

class TrashCustomFieldInput(TrashCustomFieldToolInput):
    """Operation input for `trash_custom_field`."""
    pass

class TrashCustomFieldOutput(TrashCustomFieldToolOutput):
    """Operation output for `trash_custom_field`."""
    pass

class UpdateCustomFieldInput(UpdateCustomFieldToolInput):
    """Operation input for `update_custom_field`."""
    pass

class UpdateCustomFieldOutput(UpdateCustomFieldToolOutput):
    """Operation output for `update_custom_field`."""
    pass

class JiraCustomFieldResource(BaseResourceClient):
    """Operations for the `custom_field` resource."""

    @operation(
        name='create_custom_field',
        title='CreateCustomField',
        input_model=CreateCustomFieldInput,
        output_model=CreateCustomFieldOutput,
        tools_used=('create_custom_field',),
        tags=tuple(['Issue fields']),
    )
    async def create(self, data: CreateCustomFieldInput) -> CreateCustomFieldOutput:
        """Creates a custom field. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_custom_field')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateCustomFieldOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_custom_field',
        title='DeleteCustomField',
        input_model=DeleteCustomFieldInput,
        output_model=DeleteCustomFieldOutput,
        tools_used=('delete_custom_field',),
        tags=tuple(['Issue fields']),
    )
    async def delete(self, data: DeleteCustomFieldInput) -> DeleteCustomFieldOutput:
        """Deletes a custom field. The custom field is deleted whether it is in the trash or not. See [Edit or delete a custom field](https://confluence.atlassian.com/x/Z44fOw) for more information on trashing and deleting custom fields. This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('delete_custom_field')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteCustomFieldOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='restore_custom_field',
        title='RestoreCustomField',
        input_model=RestoreCustomFieldInput,
        output_model=RestoreCustomFieldOutput,
        tools_used=('restore_custom_field',),
        tags=tuple(['Issue fields']),
    )
    async def restore(self, data: RestoreCustomFieldInput) -> RestoreCustomFieldOutput:
        """Restores a custom field from trash. See [Edit or delete a custom field](https://confluence.atlassian.com/x/Z44fOw) for more information on trashing and deleting custom fields. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('restore_custom_field')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RestoreCustomFieldOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='trash_custom_field',
        title='TrashCustomField',
        input_model=TrashCustomFieldInput,
        output_model=TrashCustomFieldOutput,
        tools_used=('trash_custom_field',),
        tags=tuple(['Issue fields']),
    )
    async def trash(self, data: TrashCustomFieldInput) -> TrashCustomFieldOutput:
        """Moves a custom field to trash. See [Edit or delete a custom field](https://confluence.atlassian.com/x/Z44fOw) for more information on trashing and deleting custom fields. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('trash_custom_field')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return TrashCustomFieldOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_custom_field',
        title='UpdateCustomField',
        input_model=UpdateCustomFieldInput,
        output_model=UpdateCustomFieldOutput,
        tools_used=('update_custom_field',),
        tags=tuple(['Issue fields']),
    )
    async def update(self, data: UpdateCustomFieldInput) -> UpdateCustomFieldOutput:
        """Updates a custom field. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, body"""
        tool = self._client.get_tool('update_custom_field')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateCustomFieldOutput.model_validate(coerce_tool_result(result))
