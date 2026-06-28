from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateCustomFieldOptionToolInput, CreateCustomFieldOptionToolOutput, DeleteCustomFieldOptionToolInput, DeleteCustomFieldOptionToolOutput, GetCustomFieldOptionToolInput, GetCustomFieldOptionToolOutput, UpdateCustomFieldOptionToolInput, UpdateCustomFieldOptionToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateCustomFieldOptionInput(CreateCustomFieldOptionToolInput):
    """Operation input for `create_custom_field_option`."""
    pass

class CreateCustomFieldOptionOutput(CreateCustomFieldOptionToolOutput):
    """Operation output for `create_custom_field_option`."""
    pass

class DeleteCustomFieldOptionInput(DeleteCustomFieldOptionToolInput):
    """Operation input for `delete_custom_field_option`."""
    pass

class DeleteCustomFieldOptionOutput(DeleteCustomFieldOptionToolOutput):
    """Operation output for `delete_custom_field_option`."""
    pass

class GetCustomFieldOptionInput(GetCustomFieldOptionToolInput):
    """Operation input for `get_custom_field_option`."""
    pass

class GetCustomFieldOptionOutput(GetCustomFieldOptionToolOutput):
    """Operation output for `get_custom_field_option`."""
    pass

class UpdateCustomFieldOptionInput(UpdateCustomFieldOptionToolInput):
    """Operation input for `update_custom_field_option`."""
    pass

class UpdateCustomFieldOptionOutput(UpdateCustomFieldOptionToolOutput):
    """Operation output for `update_custom_field_option`."""
    pass

class JiraCustomFieldOptionResource(BaseResourceClient):
    """Operations for the `custom_field_option` resource."""

    @operation(
        name='create_custom_field_option',
        title='CreateCustomFieldOption',
        input_model=CreateCustomFieldOptionInput,
        output_model=CreateCustomFieldOptionOutput,
        tools_used=('create_custom_field_option',),
        tags=tuple(['Issue custom field options']),
    )
    async def create(self, data: CreateCustomFieldOptionInput) -> CreateCustomFieldOptionOutput:
        """Creates options and, where the custom select field is of the type Select List (cascading), cascading options for a custom select field. The options are added to a context of the field. The maximum number of options that can be created per request is 1000 and each field can have a maximum of 10000 options. This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.** **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, context_id, body"""
        tool = self._client.get_tool('create_custom_field_option')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateCustomFieldOptionOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_custom_field_option',
        title='DeleteCustomFieldOption',
        input_model=DeleteCustomFieldOptionInput,
        output_model=DeleteCustomFieldOptionOutput,
        tools_used=('delete_custom_field_option',),
        tags=tuple(['Issue custom field options']),
    )
    async def delete(self, data: DeleteCustomFieldOptionInput) -> DeleteCustomFieldOptionOutput:
        """Deletes a custom field option. Options with cascading options cannot be deleted without deleting the cascading options first. This operation works for custom field options created in Jira or the operations from this resource. **To work with issue field select list options created for Connect apps use the [Issue custom field options (apps)](#api-group-issue-custom-field-options--apps-) operations.** **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, context_id, option_id"""
        tool = self._client.get_tool('delete_custom_field_option')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteCustomFieldOptionOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_custom_field_option',
        title='GetCustomFieldOption',
        input_model=GetCustomFieldOptionInput,
        output_model=GetCustomFieldOptionOutput,
        tools_used=('get_custom_field_option',),
        tags=tuple(['Issue custom field options']),
    )
    async def get(self, data: GetCustomFieldOptionInput) -> GetCustomFieldOptionOutput:
        """Returns a custom field option. For example, an option in a select list. Note that this operation **only works for issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect apps. This operation can be accessed anonymously. **[Permissions](#permissions) required:** The custom field option is returned as follows: * if the user has the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). * if the user has the *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for at least one project the custom field is used in, and the field is visible in at least one layout the user has permission to view.

Important inputs: id"""
        tool = self._client.get_tool('get_custom_field_option')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetCustomFieldOptionOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_custom_field_option',
        title='UpdateCustomFieldOption',
        input_model=UpdateCustomFieldOptionInput,
        output_model=UpdateCustomFieldOptionOutput,
        tools_used=('update_custom_field_option',),
        tags=tuple(['Issue custom field options']),
    )
    async def update(self, data: UpdateCustomFieldOptionInput) -> UpdateCustomFieldOptionOutput:
        """Updates the options of a custom field. If any of the options are not found, no options are updated. Options where the values in the request match the current values aren't updated and aren't reported in the response. Note that this operation **only works for issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource**, it cannot be used with issue field select list options created by Connect apps. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, context_id, body"""
        tool = self._client.get_tool('update_custom_field_option')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateCustomFieldOptionOutput.model_validate(coerce_tool_result(result))
