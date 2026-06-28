from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteWorkflowSchemeIssueTypeToolInput, DeleteWorkflowSchemeIssueTypeToolOutput, GetWorkflowSchemeIssueTypeToolInput, GetWorkflowSchemeIssueTypeToolOutput, SetWorkflowSchemeIssueTypeToolInput, SetWorkflowSchemeIssueTypeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteWorkflowSchemeIssueTypeInput(DeleteWorkflowSchemeIssueTypeToolInput):
    """Operation input for `delete_workflow_scheme_issue_type`."""
    pass

class DeleteWorkflowSchemeIssueTypeOutput(DeleteWorkflowSchemeIssueTypeToolOutput):
    """Operation output for `delete_workflow_scheme_issue_type`."""
    pass

class GetWorkflowSchemeIssueTypeInput(GetWorkflowSchemeIssueTypeToolInput):
    """Operation input for `get_workflow_scheme_issue_type`."""
    pass

class GetWorkflowSchemeIssueTypeOutput(GetWorkflowSchemeIssueTypeToolOutput):
    """Operation output for `get_workflow_scheme_issue_type`."""
    pass

class SetWorkflowSchemeIssueTypeInput(SetWorkflowSchemeIssueTypeToolInput):
    """Operation input for `set_workflow_scheme_issue_type`."""
    pass

class SetWorkflowSchemeIssueTypeOutput(SetWorkflowSchemeIssueTypeToolOutput):
    """Operation output for `set_workflow_scheme_issue_type`."""
    pass

class JiraWorkflowSchemeIssueTypeResource(BaseResourceClient):
    """Operations for the `workflow_scheme_issue_type` resource."""

    @operation(
        name='delete_workflow_scheme_issue_type',
        title='DeleteWorkflowSchemeIssueType',
        input_model=DeleteWorkflowSchemeIssueTypeInput,
        output_model=DeleteWorkflowSchemeIssueTypeOutput,
        tools_used=('delete_workflow_scheme_issue_type',),
        tags=tuple(['Workflow schemes']),
    )
    async def delete(self, data: DeleteWorkflowSchemeIssueTypeInput) -> DeleteWorkflowSchemeIssueTypeOutput:
        """Deletes the issue type-workflow mapping for an issue type in a workflow scheme. Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` and a draft workflow scheme is created or updated with the issue type-workflow mapping deleted. The draft workflow scheme can be published in Jira. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, issue_type, update_draft_if_needed"""
        tool = self._client.get_tool('delete_workflow_scheme_issue_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteWorkflowSchemeIssueTypeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_workflow_scheme_issue_type',
        title='GetWorkflowSchemeIssueType',
        input_model=GetWorkflowSchemeIssueTypeInput,
        output_model=GetWorkflowSchemeIssueTypeOutput,
        tools_used=('get_workflow_scheme_issue_type',),
        tags=tuple(['Workflow schemes']),
    )
    async def get(self, data: GetWorkflowSchemeIssueTypeInput) -> GetWorkflowSchemeIssueTypeOutput:
        """Returns the issue type-workflow mapping for an issue type in a workflow scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, issue_type, return_draft_if_exists"""
        tool = self._client.get_tool('get_workflow_scheme_issue_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetWorkflowSchemeIssueTypeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_workflow_scheme_issue_type',
        title='SetWorkflowSchemeIssueType',
        input_model=SetWorkflowSchemeIssueTypeInput,
        output_model=SetWorkflowSchemeIssueTypeOutput,
        tools_used=('set_workflow_scheme_issue_type',),
        tags=tuple(['Workflow schemes']),
    )
    async def set(self, data: SetWorkflowSchemeIssueTypeInput) -> SetWorkflowSchemeIssueTypeOutput:
        """Sets the workflow for an issue type in a workflow scheme. Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` in the request body and a draft workflow scheme is created or updated with the new issue type-workflow mapping. The draft workflow scheme can be published in Jira. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, issue_type, body"""
        tool = self._client.get_tool('set_workflow_scheme_issue_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetWorkflowSchemeIssueTypeOutput.model_validate(coerce_tool_result(result))
