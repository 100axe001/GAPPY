from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllWorkflowsToolInput, GetAllWorkflowsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllWorkflowsInput(GetAllWorkflowsToolInput):
    """Operation input for `get_all_workflows`."""
    pass

class GetAllWorkflowsOutput(GetAllWorkflowsToolOutput):
    """Operation output for `get_all_workflows`."""
    pass

class JiraAllWorkflowsResource(BaseResourceClient):
    """Operations for the `all_workflows` resource."""

    @operation(
        name='get_all_workflows',
        title='GetAllWorkflows',
        input_model=GetAllWorkflowsInput,
        output_model=GetAllWorkflowsOutput,
        tools_used=('get_all_workflows',),
        tags=tuple(['Workflows']),
    )
    async def get(self, data: GetAllWorkflowsInput) -> GetAllWorkflowsOutput:
        """Returns all workflows in Jira or a workflow. Deprecated, use [Get workflows paginated](#api-rest-api-3-workflow-search-get). If the `workflowName` parameter is specified, the workflow is returned as an object (not in an array). Otherwise, an array of workflow objects is returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: workflow_name"""
        tool = self._client.get_tool('get_all_workflows')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllWorkflowsOutput.model_validate(coerce_tool_result(result))
