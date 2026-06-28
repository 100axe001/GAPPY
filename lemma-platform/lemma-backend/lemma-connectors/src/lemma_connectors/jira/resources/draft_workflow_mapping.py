from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteDraftWorkflowMappingToolInput, DeleteDraftWorkflowMappingToolOutput, UpdateDraftWorkflowMappingToolInput, UpdateDraftWorkflowMappingToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteDraftWorkflowMappingInput(DeleteDraftWorkflowMappingToolInput):
    """Operation input for `delete_draft_workflow_mapping`."""
    pass

class DeleteDraftWorkflowMappingOutput(DeleteDraftWorkflowMappingToolOutput):
    """Operation output for `delete_draft_workflow_mapping`."""
    pass

class UpdateDraftWorkflowMappingInput(UpdateDraftWorkflowMappingToolInput):
    """Operation input for `update_draft_workflow_mapping`."""
    pass

class UpdateDraftWorkflowMappingOutput(UpdateDraftWorkflowMappingToolOutput):
    """Operation output for `update_draft_workflow_mapping`."""
    pass

class JiraDraftWorkflowMappingResource(BaseResourceClient):
    """Operations for the `draft_workflow_mapping` resource."""

    @operation(
        name='delete_draft_workflow_mapping',
        title='DeleteDraftWorkflowMapping',
        input_model=DeleteDraftWorkflowMappingInput,
        output_model=DeleteDraftWorkflowMappingOutput,
        tools_used=('delete_draft_workflow_mapping',),
        tags=tuple(['Workflow scheme drafts']),
    )
    async def delete(self, data: DeleteDraftWorkflowMappingInput) -> DeleteDraftWorkflowMappingOutput:
        """Deletes the workflow-issue type mapping for a workflow in a workflow scheme's draft. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, workflow_name"""
        tool = self._client.get_tool('delete_draft_workflow_mapping')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteDraftWorkflowMappingOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_draft_workflow_mapping',
        title='UpdateDraftWorkflowMapping',
        input_model=UpdateDraftWorkflowMappingInput,
        output_model=UpdateDraftWorkflowMappingOutput,
        tools_used=('update_draft_workflow_mapping',),
        tags=tuple(['Workflow scheme drafts']),
    )
    async def update(self, data: UpdateDraftWorkflowMappingInput) -> UpdateDraftWorkflowMappingOutput:
        """Sets the issue types for a workflow in a workflow scheme's draft. The workflow can also be set as the default workflow for the draft workflow scheme. Unmapped issues types are mapped to the default workflow. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, workflow_name, body"""
        tool = self._client.get_tool('update_draft_workflow_mapping')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateDraftWorkflowMappingOutput.model_validate(coerce_tool_result(result))
