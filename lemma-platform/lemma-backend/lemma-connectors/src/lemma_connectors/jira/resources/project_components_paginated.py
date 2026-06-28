from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetProjectComponentsPaginatedToolInput, GetProjectComponentsPaginatedToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProjectComponentsPaginatedInput(GetProjectComponentsPaginatedToolInput):
    """Operation input for `get_project_components_paginated`."""
    pass

class GetProjectComponentsPaginatedOutput(GetProjectComponentsPaginatedToolOutput):
    """Operation output for `get_project_components_paginated`."""
    pass

class JiraProjectComponentsPaginatedResource(BaseResourceClient):
    """Operations for the `project_components_paginated` resource."""

    @operation(
        name='get_project_components_paginated',
        title='GetProjectComponentsPaginated',
        input_model=GetProjectComponentsPaginatedInput,
        output_model=GetProjectComponentsPaginatedOutput,
        tools_used=('get_project_components_paginated',),
        tags=tuple(['Project components']),
    )
    async def get(self, data: GetProjectComponentsPaginatedInput) -> GetProjectComponentsPaginatedOutput:
        """Returns a [paginated](#pagination) list of all components in a project. See the [Get project components](#api-rest-api-3-project-projectIdOrKey-components-get) resource if you want to get a full list of versions without pagination. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

Important inputs: project_id_or_key, start_at, max_results, order_by, query"""
        tool = self._client.get_tool('get_project_components_paginated')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectComponentsPaginatedOutput.model_validate(coerce_tool_result(result))
