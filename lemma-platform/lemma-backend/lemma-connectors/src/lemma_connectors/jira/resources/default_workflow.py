from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteDefaultWorkflowToolInput, DeleteDefaultWorkflowToolOutput, GetDefaultWorkflowToolInput, GetDefaultWorkflowToolOutput, UpdateDefaultWorkflowToolInput, UpdateDefaultWorkflowToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteDefaultWorkflowInput(DeleteDefaultWorkflowToolInput):
    """Operation input for `delete_default_workflow`."""
    pass

class DeleteDefaultWorkflowOutput(DeleteDefaultWorkflowToolOutput):
    """Operation output for `delete_default_workflow`."""
    pass

class GetDefaultWorkflowInput(GetDefaultWorkflowToolInput):
    """Operation input for `get_default_workflow`."""
    pass

class GetDefaultWorkflowOutput(GetDefaultWorkflowToolOutput):
    """Operation output for `get_default_workflow`."""
    pass

class UpdateDefaultWorkflowInput(UpdateDefaultWorkflowToolInput):
    """Operation input for `update_default_workflow`."""
    pass

class UpdateDefaultWorkflowOutput(UpdateDefaultWorkflowToolOutput):
    """Operation output for `update_default_workflow`."""
    pass

class JiraDefaultWorkflowResource(BaseResourceClient):
    """Operations for the `default_workflow` resource."""

    @operation(
        name='delete_default_workflow',
        title='DeleteDefaultWorkflow',
        input_model=DeleteDefaultWorkflowInput,
        output_model=DeleteDefaultWorkflowOutput,
        tools_used=('delete_default_workflow',),
        tags=tuple(['Workflow schemes']),
    )
    async def delete(self, data: DeleteDefaultWorkflowInput) -> DeleteDefaultWorkflowOutput:
        """Resets the default workflow for a workflow scheme. That is, the default workflow is set to Jira's system workflow (the *jira* workflow). Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` and a draft workflow scheme is created or updated with the default workflow reset. The draft workflow scheme can be published in Jira. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, update_draft_if_needed"""
        tool = self._client.get_tool('delete_default_workflow')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteDefaultWorkflowOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_default_workflow',
        title='GetDefaultWorkflow',
        input_model=GetDefaultWorkflowInput,
        output_model=GetDefaultWorkflowOutput,
        tools_used=('get_default_workflow',),
        tags=tuple(['Workflow schemes']),
    )
    async def get(self, data: GetDefaultWorkflowInput) -> GetDefaultWorkflowOutput:
        """Returns the default workflow for a workflow scheme. The default workflow is the workflow that is assigned any issue types that have not been mapped to any other workflow. The default workflow has *All Unassigned Issue Types* listed in its issue types for the workflow scheme in Jira. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, return_draft_if_exists"""
        tool = self._client.get_tool('get_default_workflow')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetDefaultWorkflowOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_default_workflow',
        title='UpdateDefaultWorkflow',
        input_model=UpdateDefaultWorkflowInput,
        output_model=UpdateDefaultWorkflowOutput,
        tools_used=('update_default_workflow',),
        tags=tuple(['Workflow schemes']),
    )
    async def update(self, data: UpdateDefaultWorkflowInput) -> UpdateDefaultWorkflowOutput:
        """Sets the default workflow for a workflow scheme. Note that active workflow schemes cannot be edited. If the workflow scheme is active, set `updateDraftIfNeeded` to `true` in the request object and a draft workflow scheme is created or updated with the new default workflow. The draft workflow scheme can be published in Jira. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('update_default_workflow')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateDefaultWorkflowOutput.model_validate(coerce_tool_result(result))
