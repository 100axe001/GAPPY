from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateIssueTypeSchemeToolInput, CreateIssueTypeSchemeToolOutput, DeleteIssueTypeSchemeToolInput, DeleteIssueTypeSchemeToolOutput, UpdateIssueTypeSchemeToolInput, UpdateIssueTypeSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateIssueTypeSchemeInput(CreateIssueTypeSchemeToolInput):
    """Operation input for `create_issue_type_scheme`."""
    pass

class CreateIssueTypeSchemeOutput(CreateIssueTypeSchemeToolOutput):
    """Operation output for `create_issue_type_scheme`."""
    pass

class DeleteIssueTypeSchemeInput(DeleteIssueTypeSchemeToolInput):
    """Operation input for `delete_issue_type_scheme`."""
    pass

class DeleteIssueTypeSchemeOutput(DeleteIssueTypeSchemeToolOutput):
    """Operation output for `delete_issue_type_scheme`."""
    pass

class UpdateIssueTypeSchemeInput(UpdateIssueTypeSchemeToolInput):
    """Operation input for `update_issue_type_scheme`."""
    pass

class UpdateIssueTypeSchemeOutput(UpdateIssueTypeSchemeToolOutput):
    """Operation output for `update_issue_type_scheme`."""
    pass

class JiraIssueTypeSchemeResource(BaseResourceClient):
    """Operations for the `issue_type_scheme` resource."""

    @operation(
        name='create_issue_type_scheme',
        title='CreateIssueTypeScheme',
        input_model=CreateIssueTypeSchemeInput,
        output_model=CreateIssueTypeSchemeOutput,
        tools_used=('create_issue_type_scheme',),
        tags=tuple(['Issue type schemes']),
    )
    async def create(self, data: CreateIssueTypeSchemeInput) -> CreateIssueTypeSchemeOutput:
        """Creates an issue type scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_issue_type_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateIssueTypeSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_issue_type_scheme',
        title='DeleteIssueTypeScheme',
        input_model=DeleteIssueTypeSchemeInput,
        output_model=DeleteIssueTypeSchemeOutput,
        tools_used=('delete_issue_type_scheme',),
        tags=tuple(['Issue type schemes']),
    )
    async def delete(self, data: DeleteIssueTypeSchemeInput) -> DeleteIssueTypeSchemeOutput:
        """Deletes an issue type scheme. Only issue type schemes used in classic projects can be deleted. Any projects assigned to the scheme are reassigned to the default issue type scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_type_scheme_id"""
        tool = self._client.get_tool('delete_issue_type_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteIssueTypeSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_issue_type_scheme',
        title='UpdateIssueTypeScheme',
        input_model=UpdateIssueTypeSchemeInput,
        output_model=UpdateIssueTypeSchemeOutput,
        tools_used=('update_issue_type_scheme',),
        tags=tuple(['Issue type schemes']),
    )
    async def update(self, data: UpdateIssueTypeSchemeInput) -> UpdateIssueTypeSchemeOutput:
        """Updates an issue type scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_type_scheme_id, body"""
        tool = self._client.get_tool('update_issue_type_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateIssueTypeSchemeOutput.model_validate(coerce_tool_result(result))
