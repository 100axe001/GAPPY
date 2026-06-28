from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateIssueTypeScreenSchemeToolInput, CreateIssueTypeScreenSchemeToolOutput, DeleteIssueTypeScreenSchemeToolInput, DeleteIssueTypeScreenSchemeToolOutput, UpdateIssueTypeScreenSchemeToolInput, UpdateIssueTypeScreenSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateIssueTypeScreenSchemeInput(CreateIssueTypeScreenSchemeToolInput):
    """Operation input for `create_issue_type_screen_scheme`."""
    pass

class CreateIssueTypeScreenSchemeOutput(CreateIssueTypeScreenSchemeToolOutput):
    """Operation output for `create_issue_type_screen_scheme`."""
    pass

class DeleteIssueTypeScreenSchemeInput(DeleteIssueTypeScreenSchemeToolInput):
    """Operation input for `delete_issue_type_screen_scheme`."""
    pass

class DeleteIssueTypeScreenSchemeOutput(DeleteIssueTypeScreenSchemeToolOutput):
    """Operation output for `delete_issue_type_screen_scheme`."""
    pass

class UpdateIssueTypeScreenSchemeInput(UpdateIssueTypeScreenSchemeToolInput):
    """Operation input for `update_issue_type_screen_scheme`."""
    pass

class UpdateIssueTypeScreenSchemeOutput(UpdateIssueTypeScreenSchemeToolOutput):
    """Operation output for `update_issue_type_screen_scheme`."""
    pass

class JiraIssueTypeScreenSchemeResource(BaseResourceClient):
    """Operations for the `issue_type_screen_scheme` resource."""

    @operation(
        name='create_issue_type_screen_scheme',
        title='CreateIssueTypeScreenScheme',
        input_model=CreateIssueTypeScreenSchemeInput,
        output_model=CreateIssueTypeScreenSchemeOutput,
        tools_used=('create_issue_type_screen_scheme',),
        tags=tuple(['Issue type screen schemes']),
    )
    async def create(self, data: CreateIssueTypeScreenSchemeInput) -> CreateIssueTypeScreenSchemeOutput:
        """Creates an issue type screen scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_issue_type_screen_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateIssueTypeScreenSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_issue_type_screen_scheme',
        title='DeleteIssueTypeScreenScheme',
        input_model=DeleteIssueTypeScreenSchemeInput,
        output_model=DeleteIssueTypeScreenSchemeOutput,
        tools_used=('delete_issue_type_screen_scheme',),
        tags=tuple(['Issue type screen schemes']),
    )
    async def delete(self, data: DeleteIssueTypeScreenSchemeInput) -> DeleteIssueTypeScreenSchemeOutput:
        """Deletes an issue type screen scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_type_screen_scheme_id"""
        tool = self._client.get_tool('delete_issue_type_screen_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteIssueTypeScreenSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_issue_type_screen_scheme',
        title='UpdateIssueTypeScreenScheme',
        input_model=UpdateIssueTypeScreenSchemeInput,
        output_model=UpdateIssueTypeScreenSchemeOutput,
        tools_used=('update_issue_type_screen_scheme',),
        tags=tuple(['Issue type screen schemes']),
    )
    async def update(self, data: UpdateIssueTypeScreenSchemeInput) -> UpdateIssueTypeScreenSchemeOutput:
        """Updates an issue type screen scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_type_screen_scheme_id, body"""
        tool = self._client.get_tool('update_issue_type_screen_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateIssueTypeScreenSchemeOutput.model_validate(coerce_tool_result(result))
