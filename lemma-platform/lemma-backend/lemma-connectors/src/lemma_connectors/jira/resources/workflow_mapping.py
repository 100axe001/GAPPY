from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteWorkflowMappingToolInput, DeleteWorkflowMappingToolOutput, UpdateWorkflowMappingToolInput, UpdateWorkflowMappingToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteWorkflowMappingInput(DeleteWorkflowMappingToolInput):
    """Operation input for `delete_workflow_mapping`."""
    pass

class DeleteWorkflowMappingOutput(DeleteWorkflowMappingToolOutput):
    """Operation output for `delete_workflow_mapping`."""
    pass

class UpdateWorkflowMappingInput(UpdateWorkflowMappingToolInput):
    """Operation input for `update_workflow_mapping`."""
    pass

class UpdateWorkflowMappingOutput(UpdateWorkflowMappingToolOutput):
    """Operation output for `update_workflow_mapping`."""
    pass

class JiraWorkflowMappingResource(BaseResourceClient):
    """Operations for the `workflow_mapping` resource."""

    @operation(
        name='delete_workflow_mapping',
        title='DeleteWorkflowMapping',
        input_model=DeleteWorkflowMappingInput,
        output_model=DeleteWorkflowMappingOutput,
        tools_used=('delete_workflow_mapping',),
        tags=tuple(['Workflow schemes']),
    )
    async def delete(self, data: DeleteWorkflowMappingInput) -> DeleteWorkflowMappingOutput:
        """Deletes the workflow-issue type mapping for a workflow in a workflow scheme. Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` and a draft workflow scheme is created or updated with the workflow-issue type mapping deleted. The draft workflow scheme can be published in Jira. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, workflow_name, update_draft_if_needed"""
        tool = self._client.get_tool('delete_workflow_mapping')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteWorkflowMappingOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_workflow_mapping',
        title='UpdateWorkflowMapping',
        input_model=UpdateWorkflowMappingInput,
        output_model=UpdateWorkflowMappingOutput,
        tools_used=('update_workflow_mapping',),
        tags=tuple(['Workflow schemes']),
    )
    async def update(self, data: UpdateWorkflowMappingInput) -> UpdateWorkflowMappingOutput:
        """Sets the issue types for a workflow in a workflow scheme. The workflow can also be set as the default workflow for the workflow scheme. Unmapped issues types are mapped to the default workflow. Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` in the request body and a draft workflow scheme is created or updated with the new workflow-issue types mappings. The draft workflow scheme can be published in Jira. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, workflow_name, body"""
        tool = self._client.get_tool('update_workflow_mapping')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateWorkflowMappingOutput.model_validate(coerce_tool_result(result))
