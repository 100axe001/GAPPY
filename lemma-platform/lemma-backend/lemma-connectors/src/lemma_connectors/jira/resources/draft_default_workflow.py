from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteDraftDefaultWorkflowToolInput, DeleteDraftDefaultWorkflowToolOutput, GetDraftDefaultWorkflowToolInput, GetDraftDefaultWorkflowToolOutput, UpdateDraftDefaultWorkflowToolInput, UpdateDraftDefaultWorkflowToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteDraftDefaultWorkflowInput(DeleteDraftDefaultWorkflowToolInput):
    """Operation input for `delete_draft_default_workflow`."""
    pass

class DeleteDraftDefaultWorkflowOutput(DeleteDraftDefaultWorkflowToolOutput):
    """Operation output for `delete_draft_default_workflow`."""
    pass

class GetDraftDefaultWorkflowInput(GetDraftDefaultWorkflowToolInput):
    """Operation input for `get_draft_default_workflow`."""
    pass

class GetDraftDefaultWorkflowOutput(GetDraftDefaultWorkflowToolOutput):
    """Operation output for `get_draft_default_workflow`."""
    pass

class UpdateDraftDefaultWorkflowInput(UpdateDraftDefaultWorkflowToolInput):
    """Operation input for `update_draft_default_workflow`."""
    pass

class UpdateDraftDefaultWorkflowOutput(UpdateDraftDefaultWorkflowToolOutput):
    """Operation output for `update_draft_default_workflow`."""
    pass

class JiraDraftDefaultWorkflowResource(BaseResourceClient):
    """Operations for the `draft_default_workflow` resource."""

    @operation(
        name='delete_draft_default_workflow',
        title='DeleteDraftDefaultWorkflow',
        input_model=DeleteDraftDefaultWorkflowInput,
        output_model=DeleteDraftDefaultWorkflowOutput,
        tools_used=('delete_draft_default_workflow',),
        tags=tuple(['Workflow scheme drafts']),
    )
    async def delete(self, data: DeleteDraftDefaultWorkflowInput) -> DeleteDraftDefaultWorkflowOutput:
        """Resets the default workflow for a workflow scheme's draft. That is, the default workflow is set to Jira's system workflow (the *jira* workflow). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('delete_draft_default_workflow')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteDraftDefaultWorkflowOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_draft_default_workflow',
        title='GetDraftDefaultWorkflow',
        input_model=GetDraftDefaultWorkflowInput,
        output_model=GetDraftDefaultWorkflowOutput,
        tools_used=('get_draft_default_workflow',),
        tags=tuple(['Workflow scheme drafts']),
    )
    async def get(self, data: GetDraftDefaultWorkflowInput) -> GetDraftDefaultWorkflowOutput:
        """Returns the default workflow for a workflow scheme's draft. The default workflow is the workflow that is assigned any issue types that have not been mapped to any other workflow. The default workflow has *All Unassigned Issue Types* listed in its issue types for the workflow scheme in Jira. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('get_draft_default_workflow')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetDraftDefaultWorkflowOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_draft_default_workflow',
        title='UpdateDraftDefaultWorkflow',
        input_model=UpdateDraftDefaultWorkflowInput,
        output_model=UpdateDraftDefaultWorkflowOutput,
        tools_used=('update_draft_default_workflow',),
        tags=tuple(['Workflow scheme drafts']),
    )
    async def update(self, data: UpdateDraftDefaultWorkflowInput) -> UpdateDraftDefaultWorkflowOutput:
        """Sets the default workflow for a workflow scheme's draft. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('update_draft_default_workflow')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateDraftDefaultWorkflowOutput.model_validate(coerce_tool_result(result))
