from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateIssueFieldOptionToolInput, CreateIssueFieldOptionToolOutput, DeleteIssueFieldOptionToolInput, DeleteIssueFieldOptionToolOutput, GetIssueFieldOptionToolInput, GetIssueFieldOptionToolOutput, UpdateIssueFieldOptionToolInput, UpdateIssueFieldOptionToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateIssueFieldOptionInput(CreateIssueFieldOptionToolInput):
    """Operation input for `create_issue_field_option`."""
    pass

class CreateIssueFieldOptionOutput(CreateIssueFieldOptionToolOutput):
    """Operation output for `create_issue_field_option`."""
    pass

class DeleteIssueFieldOptionInput(DeleteIssueFieldOptionToolInput):
    """Operation input for `delete_issue_field_option`."""
    pass

class DeleteIssueFieldOptionOutput(DeleteIssueFieldOptionToolOutput):
    """Operation output for `delete_issue_field_option`."""
    pass

class GetIssueFieldOptionInput(GetIssueFieldOptionToolInput):
    """Operation input for `get_issue_field_option`."""
    pass

class GetIssueFieldOptionOutput(GetIssueFieldOptionToolOutput):
    """Operation output for `get_issue_field_option`."""
    pass

class UpdateIssueFieldOptionInput(UpdateIssueFieldOptionToolInput):
    """Operation input for `update_issue_field_option`."""
    pass

class UpdateIssueFieldOptionOutput(UpdateIssueFieldOptionToolOutput):
    """Operation output for `update_issue_field_option`."""
    pass

class JiraIssueFieldOptionResource(BaseResourceClient):
    """Operations for the `issue_field_option` resource."""

    @operation(
        name='create_issue_field_option',
        title='CreateIssueFieldOption',
        input_model=CreateIssueFieldOptionInput,
        output_model=CreateIssueFieldOptionOutput,
        tools_used=('create_issue_field_option',),
        tags=tuple(['Issue custom field options (apps)']),
    )
    async def create(self, data: CreateIssueFieldOptionInput) -> CreateIssueFieldOptionOutput:
        """Creates an option for a select list issue field. Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.

Important inputs: field_key, body"""
        tool = self._client.get_tool('create_issue_field_option')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateIssueFieldOptionOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_issue_field_option',
        title='DeleteIssueFieldOption',
        input_model=DeleteIssueFieldOptionInput,
        output_model=DeleteIssueFieldOptionOutput,
        tools_used=('delete_issue_field_option',),
        tags=tuple(['Issue custom field options (apps)']),
    )
    async def delete(self, data: DeleteIssueFieldOptionInput) -> DeleteIssueFieldOptionOutput:
        """Deletes an option from a select list issue field. Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.

Important inputs: field_key, option_id"""
        tool = self._client.get_tool('delete_issue_field_option')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteIssueFieldOptionOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_issue_field_option',
        title='GetIssueFieldOption',
        input_model=GetIssueFieldOptionInput,
        output_model=GetIssueFieldOptionOutput,
        tools_used=('get_issue_field_option',),
        tags=tuple(['Issue custom field options (apps)']),
    )
    async def get(self, data: GetIssueFieldOptionInput) -> GetIssueFieldOptionOutput:
        """Returns an option from a select list issue field. Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.

Important inputs: field_key, option_id"""
        tool = self._client.get_tool('get_issue_field_option')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueFieldOptionOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_issue_field_option',
        title='UpdateIssueFieldOption',
        input_model=UpdateIssueFieldOptionInput,
        output_model=UpdateIssueFieldOptionOutput,
        tools_used=('update_issue_field_option',),
        tags=tuple(['Issue custom field options (apps)']),
    )
    async def update(self, data: UpdateIssueFieldOptionInput) -> UpdateIssueFieldOptionOutput:
        """Updates or creates an option for a select list issue field. This operation requires that the option ID is provided when creating an option, therefore, the option ID needs to be specified as a path and body parameter. The option ID provided in the path and body must be identical. Note that this operation **only works for issue field select list options added by Connect apps**, it cannot be used with issue field select list options created in Jira or using operations from the [Issue custom field options](#api-group-Issue-custom-field-options) resource. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the app providing the field.

Important inputs: field_key, option_id, body"""
        tool = self._client.get_tool('update_issue_field_option')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateIssueFieldOptionOutput.model_validate(coerce_tool_result(result))
