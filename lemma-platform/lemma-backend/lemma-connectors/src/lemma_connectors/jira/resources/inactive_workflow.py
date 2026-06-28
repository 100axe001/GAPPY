from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import DeleteInactiveWorkflowToolInput, DeleteInactiveWorkflowToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class DeleteInactiveWorkflowInput(DeleteInactiveWorkflowToolInput):
    """Operation input for `delete_inactive_workflow`."""
    pass

class DeleteInactiveWorkflowOutput(DeleteInactiveWorkflowToolOutput):
    """Operation output for `delete_inactive_workflow`."""
    pass

class JiraInactiveWorkflowResource(BaseResourceClient):
    """Operations for the `inactive_workflow` resource."""

    @operation(
        name='delete_inactive_workflow',
        title='DeleteInactiveWorkflow',
        input_model=DeleteInactiveWorkflowInput,
        output_model=DeleteInactiveWorkflowOutput,
        tools_used=('delete_inactive_workflow',),
        tags=tuple(['Workflows']),
    )
    async def delete(self, data: DeleteInactiveWorkflowInput) -> DeleteInactiveWorkflowOutput:
        """Deletes a workflow. The workflow cannot be deleted if it is: * an active workflow. * a system workflow. * associated with any workflow scheme. * associated with any draft workflow scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: entity_id"""
        tool = self._client.get_tool('delete_inactive_workflow')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteInactiveWorkflowOutput.model_validate(coerce_tool_result(result))
