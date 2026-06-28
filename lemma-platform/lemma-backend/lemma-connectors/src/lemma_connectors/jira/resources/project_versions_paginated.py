from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetProjectVersionsPaginatedToolInput, GetProjectVersionsPaginatedToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProjectVersionsPaginatedInput(GetProjectVersionsPaginatedToolInput):
    """Operation input for `get_project_versions_paginated`."""
    pass

class GetProjectVersionsPaginatedOutput(GetProjectVersionsPaginatedToolOutput):
    """Operation output for `get_project_versions_paginated`."""
    pass

class JiraProjectVersionsPaginatedResource(BaseResourceClient):
    """Operations for the `project_versions_paginated` resource."""

    @operation(
        name='get_project_versions_paginated',
        title='GetProjectVersionsPaginated',
        input_model=GetProjectVersionsPaginatedInput,
        output_model=GetProjectVersionsPaginatedOutput,
        tools_used=('get_project_versions_paginated',),
        tags=tuple(['Project versions']),
    )
    async def get(self, data: GetProjectVersionsPaginatedInput) -> GetProjectVersionsPaginatedOutput:
        """Returns a [paginated](#pagination) list of all versions in a project. See the [Get project versions](#api-rest-api-3-project-projectIdOrKey-versions-get) resource if you want to get a full list of versions without pagination. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

Important inputs: project_id_or_key, start_at, max_results, order_by, query, status, expand"""
        tool = self._client.get_tool('get_project_versions_paginated')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectVersionsPaginatedOutput.model_validate(coerce_tool_result(result))
