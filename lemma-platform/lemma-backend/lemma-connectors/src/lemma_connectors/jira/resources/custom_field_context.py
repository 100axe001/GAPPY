from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateCustomFieldContextToolInput, CreateCustomFieldContextToolOutput, DeleteCustomFieldContextToolInput, DeleteCustomFieldContextToolOutput, UpdateCustomFieldContextToolInput, UpdateCustomFieldContextToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateCustomFieldContextInput(CreateCustomFieldContextToolInput):
    """Operation input for `create_custom_field_context`."""
    pass

class CreateCustomFieldContextOutput(CreateCustomFieldContextToolOutput):
    """Operation output for `create_custom_field_context`."""
    pass

class DeleteCustomFieldContextInput(DeleteCustomFieldContextToolInput):
    """Operation input for `delete_custom_field_context`."""
    pass

class DeleteCustomFieldContextOutput(DeleteCustomFieldContextToolOutput):
    """Operation output for `delete_custom_field_context`."""
    pass

class UpdateCustomFieldContextInput(UpdateCustomFieldContextToolInput):
    """Operation input for `update_custom_field_context`."""
    pass

class UpdateCustomFieldContextOutput(UpdateCustomFieldContextToolOutput):
    """Operation output for `update_custom_field_context`."""
    pass

class JiraCustomFieldContextResource(BaseResourceClient):
    """Operations for the `custom_field_context` resource."""

    @operation(
        name='create_custom_field_context',
        title='CreateCustomFieldContext',
        input_model=CreateCustomFieldContextInput,
        output_model=CreateCustomFieldContextOutput,
        tools_used=('create_custom_field_context',),
        tags=tuple(['Issue custom field contexts']),
    )
    async def create(self, data: CreateCustomFieldContextInput) -> CreateCustomFieldContextOutput:
        """Creates a custom field context. If `projectIds` is empty, a global context is created. A global context is one that applies to all project. If `issueTypeIds` is empty, the context applies to all issue types. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, body"""
        tool = self._client.get_tool('create_custom_field_context')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateCustomFieldContextOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_custom_field_context',
        title='DeleteCustomFieldContext',
        input_model=DeleteCustomFieldContextInput,
        output_model=DeleteCustomFieldContextOutput,
        tools_used=('delete_custom_field_context',),
        tags=tuple(['Issue custom field contexts']),
    )
    async def delete(self, data: DeleteCustomFieldContextInput) -> DeleteCustomFieldContextOutput:
        """Deletes a [ custom field context](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, context_id"""
        tool = self._client.get_tool('delete_custom_field_context')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteCustomFieldContextOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_custom_field_context',
        title='UpdateCustomFieldContext',
        input_model=UpdateCustomFieldContextInput,
        output_model=UpdateCustomFieldContextOutput,
        tools_used=('update_custom_field_context',),
        tags=tuple(['Issue custom field contexts']),
    )
    async def update(self, data: UpdateCustomFieldContextInput) -> UpdateCustomFieldContextOutput:
        """Updates a [ custom field context](https://confluence.atlassian.com/adminjiracloud/what-are-custom-field-contexts-991923859.html). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, context_id, body"""
        tool = self._client.get_tool('update_custom_field_context')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateCustomFieldContextOutput.model_validate(coerce_tool_result(result))
