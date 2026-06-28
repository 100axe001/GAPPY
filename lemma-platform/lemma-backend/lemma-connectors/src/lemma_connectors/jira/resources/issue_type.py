from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateIssueTypeToolInput, CreateIssueTypeToolOutput, DeleteIssueTypeToolInput, DeleteIssueTypeToolOutput, GetIssueTypeToolInput, GetIssueTypeToolOutput, UpdateIssueTypeToolInput, UpdateIssueTypeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateIssueTypeInput(CreateIssueTypeToolInput):
    """Operation input for `create_issue_type`."""
    pass

class CreateIssueTypeOutput(CreateIssueTypeToolOutput):
    """Operation output for `create_issue_type`."""
    pass

class DeleteIssueTypeInput(DeleteIssueTypeToolInput):
    """Operation input for `delete_issue_type`."""
    pass

class DeleteIssueTypeOutput(DeleteIssueTypeToolOutput):
    """Operation output for `delete_issue_type`."""
    pass

class GetIssueTypeInput(GetIssueTypeToolInput):
    """Operation input for `get_issue_type`."""
    pass

class GetIssueTypeOutput(GetIssueTypeToolOutput):
    """Operation output for `get_issue_type`."""
    pass

class UpdateIssueTypeInput(UpdateIssueTypeToolInput):
    """Operation input for `update_issue_type`."""
    pass

class UpdateIssueTypeOutput(UpdateIssueTypeToolOutput):
    """Operation output for `update_issue_type`."""
    pass

class JiraIssueTypeResource(BaseResourceClient):
    """Operations for the `issue_type` resource."""

    @operation(
        name='create_issue_type',
        title='CreateIssueType',
        input_model=CreateIssueTypeInput,
        output_model=CreateIssueTypeOutput,
        tools_used=('create_issue_type',),
        tags=tuple(['Issue types']),
    )
    async def create(self, data: CreateIssueTypeInput) -> CreateIssueTypeOutput:
        """Creates an issue type and adds it to the default issue type scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_issue_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateIssueTypeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_issue_type',
        title='DeleteIssueType',
        input_model=DeleteIssueTypeInput,
        output_model=DeleteIssueTypeOutput,
        tools_used=('delete_issue_type',),
        tags=tuple(['Issue types']),
    )
    async def delete(self, data: DeleteIssueTypeInput) -> DeleteIssueTypeOutput:
        """Deletes the issue type. If the issue type is in use, all uses are updated with the alternative issue type (`alternativeIssueTypeId`). A list of alternative issue types are obtained from the [Get alternative issue types](#api-rest-api-3-issuetype-id-alternatives-get) resource. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, alternative_issue_type_id"""
        tool = self._client.get_tool('delete_issue_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteIssueTypeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_issue_type',
        title='GetIssueType',
        input_model=GetIssueTypeInput,
        output_model=GetIssueTypeOutput,
        tools_used=('get_issue_type',),
        tags=tuple(['Issue types']),
    )
    async def get(self, data: GetIssueTypeInput) -> GetIssueTypeOutput:
        """Returns an issue type. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) in a project the issue type is associated with or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('get_issue_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueTypeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_issue_type',
        title='UpdateIssueType',
        input_model=UpdateIssueTypeInput,
        output_model=UpdateIssueTypeOutput,
        tools_used=('update_issue_type',),
        tags=tuple(['Issue types']),
    )
    async def update(self, data: UpdateIssueTypeInput) -> UpdateIssueTypeOutput:
        """Updates the issue type. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('update_issue_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateIssueTypeOutput.model_validate(coerce_tool_result(result))
