from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetFavouriteFiltersToolInput, GetFavouriteFiltersToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetFavouriteFiltersInput(GetFavouriteFiltersToolInput):
    """Operation input for `get_favourite_filters`."""
    pass

class GetFavouriteFiltersOutput(GetFavouriteFiltersToolOutput):
    """Operation output for `get_favourite_filters`."""
    pass

class JiraFavouriteFiltersResource(BaseResourceClient):
    """Operations for the `favourite_filters` resource."""

    @operation(
        name='get_favourite_filters',
        title='GetFavouriteFilters',
        input_model=GetFavouriteFiltersInput,
        output_model=GetFavouriteFiltersOutput,
        tools_used=('get_favourite_filters',),
        tags=tuple(['Filters']),
    )
    async def get(self, data: GetFavouriteFiltersInput) -> GetFavouriteFiltersOutput:
        """Returns the visible favorite filters of the user. This operation can be accessed anonymously. **[Permissions](#permissions) required:** A favorite filter is only visible to the user where the filter is: * owned by the user. * shared with a group that the user is a member of. * shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for. * shared with a public project. * shared with the public. For example, if the user favorites a public filter that is subsequently made private that filter is not returned by this operation.

Important inputs: expand"""
        tool = self._client.get_tool('get_favourite_filters')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetFavouriteFiltersOutput.model_validate(coerce_tool_result(result))
