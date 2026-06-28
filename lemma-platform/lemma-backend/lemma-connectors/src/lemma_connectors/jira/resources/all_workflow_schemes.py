from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllWorkflowSchemesToolInput, GetAllWorkflowSchemesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllWorkflowSchemesInput(GetAllWorkflowSchemesToolInput):
    """Operation input for `get_all_workflow_schemes`."""
    pass

class GetAllWorkflowSchemesOutput(GetAllWorkflowSchemesToolOutput):
    """Operation output for `get_all_workflow_schemes`."""
    pass

class JiraAllWorkflowSchemesResource(BaseResourceClient):
    """Operations for the `all_workflow_schemes` resource."""

    @operation(
        name='get_all_workflow_schemes',
        title='GetAllWorkflowSchemes',
        input_model=GetAllWorkflowSchemesInput,
        output_model=GetAllWorkflowSchemesOutput,
        tools_used=('get_all_workflow_schemes',),
        tags=tuple(['Workflow schemes']),
    )
    async def get(self, data: GetAllWorkflowSchemesInput) -> GetAllWorkflowSchemesOutput:
        """Returns a [paginated](#pagination) list of all workflow schemes, not including draft workflow schemes. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results"""
        tool = self._client.get_tool('get_all_workflow_schemes')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllWorkflowSchemesOutput.model_validate(coerce_tool_result(result))
