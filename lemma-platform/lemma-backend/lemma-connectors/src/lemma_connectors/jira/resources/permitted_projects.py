from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetPermittedProjectsToolInput, GetPermittedProjectsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetPermittedProjectsInput(GetPermittedProjectsToolInput):
    """Operation input for `get_permitted_projects`."""
    pass

class GetPermittedProjectsOutput(GetPermittedProjectsToolOutput):
    """Operation output for `get_permitted_projects`."""
    pass

class JiraPermittedProjectsResource(BaseResourceClient):
    """Operations for the `permitted_projects` resource."""

    @operation(
        name='get_permitted_projects',
        title='GetPermittedProjects',
        input_model=GetPermittedProjectsInput,
        output_model=GetPermittedProjectsOutput,
        tools_used=('get_permitted_projects',),
        tags=tuple(['Permissions']),
    )
    async def get(self, data: GetPermittedProjectsInput) -> GetPermittedProjectsOutput:
        """Returns all the projects where the user is granted a list of project permissions. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: body"""
        tool = self._client.get_tool('get_permitted_projects')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetPermittedProjectsOutput.model_validate(coerce_tool_result(result))
