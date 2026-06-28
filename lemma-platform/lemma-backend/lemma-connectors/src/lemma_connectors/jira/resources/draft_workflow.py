from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetDraftWorkflowToolInput, GetDraftWorkflowToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetDraftWorkflowInput(GetDraftWorkflowToolInput):
    """Operation input for `get_draft_workflow`."""
    pass

class GetDraftWorkflowOutput(GetDraftWorkflowToolOutput):
    """Operation output for `get_draft_workflow`."""
    pass

class JiraDraftWorkflowResource(BaseResourceClient):
    """Operations for the `draft_workflow` resource."""

    @operation(
        name='get_draft_workflow',
        title='GetDraftWorkflow',
        input_model=GetDraftWorkflowInput,
        output_model=GetDraftWorkflowOutput,
        tools_used=('get_draft_workflow',),
        tags=tuple(['Workflow scheme drafts']),
    )
    async def get(self, data: GetDraftWorkflowInput) -> GetDraftWorkflowOutput:
        """Returns the workflow-issue type mappings for a workflow scheme's draft. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, workflow_name"""
        tool = self._client.get_tool('get_draft_workflow')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetDraftWorkflowOutput.model_validate(coerce_tool_result(result))
