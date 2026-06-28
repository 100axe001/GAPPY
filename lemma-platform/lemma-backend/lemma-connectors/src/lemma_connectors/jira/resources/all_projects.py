from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllProjectsToolInput, GetAllProjectsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllProjectsInput(GetAllProjectsToolInput):
    """Operation input for `get_all_projects`."""
    pass

class GetAllProjectsOutput(GetAllProjectsToolOutput):
    """Operation output for `get_all_projects`."""
    pass

class JiraAllProjectsResource(BaseResourceClient):
    """Operations for the `all_projects` resource."""

    @operation(
        name='get_all_projects',
        title='GetAllProjects',
        input_model=GetAllProjectsInput,
        output_model=GetAllProjectsOutput,
        tools_used=('get_all_projects',),
        tags=tuple(['Projects']),
    )
    async def get(self, data: GetAllProjectsInput) -> GetAllProjectsOutput:
        """Returns all projects visible to the user. Deprecated, use [ Get projects paginated](#api-rest-api-3-project-search-get) that supports search and pagination. This operation can be accessed anonymously. **[Permissions](#permissions) required:** Projects are returned only where the user has *Browse Projects* or *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

Important inputs: expand, recent, properties"""
        tool = self._client.get_tool('get_all_projects')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllProjectsOutput.model_validate(coerce_tool_result(result))
