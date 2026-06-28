from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetWorkflowsPaginatedToolInput, GetWorkflowsPaginatedToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetWorkflowsPaginatedInput(GetWorkflowsPaginatedToolInput):
    """Operation input for `get_workflows_paginated`."""
    pass

class GetWorkflowsPaginatedOutput(GetWorkflowsPaginatedToolOutput):
    """Operation output for `get_workflows_paginated`."""
    pass

class JiraWorkflowsPaginatedResource(BaseResourceClient):
    """Operations for the `workflows_paginated` resource."""

    @operation(
        name='get_workflows_paginated',
        title='GetWorkflowsPaginated',
        input_model=GetWorkflowsPaginatedInput,
        output_model=GetWorkflowsPaginatedOutput,
        tools_used=('get_workflows_paginated',),
        tags=tuple(['Workflows']),
    )
    async def get(self, data: GetWorkflowsPaginatedInput) -> GetWorkflowsPaginatedOutput:
        """Returns a [paginated](#pagination) list of published classic workflows. When workflow names are specified, details of those workflows are returned. Otherwise, all published classic workflows are returned. This operation does not return next-gen workflows. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, workflow_name, expand, query_string, order_by, is_active"""
        tool = self._client.get_tool('get_workflows_paginated')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetWorkflowsPaginatedOutput.model_validate(coerce_tool_result(result))
