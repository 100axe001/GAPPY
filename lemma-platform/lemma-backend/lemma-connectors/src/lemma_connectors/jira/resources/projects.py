from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import SearchProjectsToolInput, SearchProjectsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SearchProjectsInput(SearchProjectsToolInput):
    """Operation input for `search_projects`."""
    pass

class SearchProjectsOutput(SearchProjectsToolOutput):
    """Operation output for `search_projects`."""
    pass

class JiraProjectsResource(BaseResourceClient):
    """Operations for the `projects` resource."""

    @operation(
        name='search_projects',
        title='SearchProjects',
        input_model=SearchProjectsInput,
        output_model=SearchProjectsOutput,
        tools_used=('search_projects',),
        tags=tuple(['Projects']),
    )
    async def search(self, data: SearchProjectsInput) -> SearchProjectsOutput:
        """Returns a [paginated](#pagination) list of projects visible to the user. This operation can be accessed anonymously. **[Permissions](#permissions) required:** Projects are returned only where the user has one of: * *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project. * *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project. * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, order_by, id, keys, query, type_key, category_id, action, expand, status, properties, property_query"""
        tool = self._client.get_tool('search_projects')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SearchProjectsOutput.model_validate(coerce_tool_result(result))
