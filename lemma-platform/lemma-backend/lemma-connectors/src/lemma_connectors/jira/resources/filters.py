from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetFiltersToolInput, GetFiltersToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetFiltersInput(GetFiltersToolInput):
    """Operation input for `get_filters`."""
    pass

class GetFiltersOutput(GetFiltersToolOutput):
    """Operation output for `get_filters`."""
    pass

class JiraFiltersResource(BaseResourceClient):
    """Operations for the `filters` resource."""

    @operation(
        name='get_filters',
        title='GetFilters',
        input_model=GetFiltersInput,
        output_model=GetFiltersOutput,
        tools_used=('get_filters',),
        tags=tuple(['Filters']),
    )
    async def get(self, data: GetFiltersInput) -> GetFiltersOutput:
        """Returns all filters. Deprecated, use [ Search for filters](#api-rest-api-3-filter-search-get) that supports search and pagination. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None, however, only the following filters are returned: * filters owned by the user. * filters shared with a group that the user is a member of. * filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for. * filters shared with a public project. * filters shared with the public.

Important inputs: expand"""
        tool = self._client.get_tool('get_filters')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetFiltersOutput.model_validate(coerce_tool_result(result))
