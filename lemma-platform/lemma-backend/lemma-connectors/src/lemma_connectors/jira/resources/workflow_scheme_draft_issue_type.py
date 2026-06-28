from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteWorkflowSchemeDraftIssueTypeToolInput, DeleteWorkflowSchemeDraftIssueTypeToolOutput, GetWorkflowSchemeDraftIssueTypeToolInput, GetWorkflowSchemeDraftIssueTypeToolOutput, SetWorkflowSchemeDraftIssueTypeToolInput, SetWorkflowSchemeDraftIssueTypeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteWorkflowSchemeDraftIssueTypeInput(DeleteWorkflowSchemeDraftIssueTypeToolInput):
    """Operation input for `delete_workflow_scheme_draft_issue_type`."""
    pass

class DeleteWorkflowSchemeDraftIssueTypeOutput(DeleteWorkflowSchemeDraftIssueTypeToolOutput):
    """Operation output for `delete_workflow_scheme_draft_issue_type`."""
    pass

class GetWorkflowSchemeDraftIssueTypeInput(GetWorkflowSchemeDraftIssueTypeToolInput):
    """Operation input for `get_workflow_scheme_draft_issue_type`."""
    pass

class GetWorkflowSchemeDraftIssueTypeOutput(GetWorkflowSchemeDraftIssueTypeToolOutput):
    """Operation output for `get_workflow_scheme_draft_issue_type`."""
    pass

class SetWorkflowSchemeDraftIssueTypeInput(SetWorkflowSchemeDraftIssueTypeToolInput):
    """Operation input for `set_workflow_scheme_draft_issue_type`."""
    pass

class SetWorkflowSchemeDraftIssueTypeOutput(SetWorkflowSchemeDraftIssueTypeToolOutput):
    """Operation output for `set_workflow_scheme_draft_issue_type`."""
    pass

class JiraWorkflowSchemeDraftIssueTypeResource(BaseResourceClient):
    """Operations for the `workflow_scheme_draft_issue_type` resource."""

    @operation(
        name='delete_workflow_scheme_draft_issue_type',
        title='DeleteWorkflowSchemeDraftIssueType',
        input_model=DeleteWorkflowSchemeDraftIssueTypeInput,
        output_model=DeleteWorkflowSchemeDraftIssueTypeOutput,
        tools_used=('delete_workflow_scheme_draft_issue_type',),
        tags=tuple(['Workflow scheme drafts']),
    )
    async def delete(self, data: DeleteWorkflowSchemeDraftIssueTypeInput) -> DeleteWorkflowSchemeDraftIssueTypeOutput:
        """Deletes the issue type-workflow mapping for an issue type in a workflow scheme's draft. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, issue_type"""
        tool = self._client.get_tool('delete_workflow_scheme_draft_issue_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteWorkflowSchemeDraftIssueTypeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_workflow_scheme_draft_issue_type',
        title='GetWorkflowSchemeDraftIssueType',
        input_model=GetWorkflowSchemeDraftIssueTypeInput,
        output_model=GetWorkflowSchemeDraftIssueTypeOutput,
        tools_used=('get_workflow_scheme_draft_issue_type',),
        tags=tuple(['Workflow scheme drafts']),
    )
    async def get(self, data: GetWorkflowSchemeDraftIssueTypeInput) -> GetWorkflowSchemeDraftIssueTypeOutput:
        """Returns the issue type-workflow mapping for an issue type in a workflow scheme's draft. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, issue_type"""
        tool = self._client.get_tool('get_workflow_scheme_draft_issue_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetWorkflowSchemeDraftIssueTypeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_workflow_scheme_draft_issue_type',
        title='SetWorkflowSchemeDraftIssueType',
        input_model=SetWorkflowSchemeDraftIssueTypeInput,
        output_model=SetWorkflowSchemeDraftIssueTypeOutput,
        tools_used=('set_workflow_scheme_draft_issue_type',),
        tags=tuple(['Workflow scheme drafts']),
    )
    async def set(self, data: SetWorkflowSchemeDraftIssueTypeInput) -> SetWorkflowSchemeDraftIssueTypeOutput:
        """Sets the workflow for an issue type in a workflow scheme's draft. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, issue_type, body"""
        tool = self._client.get_tool('set_workflow_scheme_draft_issue_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetWorkflowSchemeDraftIssueTypeOutput.model_validate(coerce_tool_result(result))
