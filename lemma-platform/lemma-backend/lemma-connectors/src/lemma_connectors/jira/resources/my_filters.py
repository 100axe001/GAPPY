from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetMyFiltersToolInput, GetMyFiltersToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetMyFiltersInput(GetMyFiltersToolInput):
    """Operation input for `get_my_filters`."""
    pass

class GetMyFiltersOutput(GetMyFiltersToolOutput):
    """Operation output for `get_my_filters`."""
    pass

class JiraMyFiltersResource(BaseResourceClient):
    """Operations for the `my_filters` resource."""

    @operation(
        name='get_my_filters',
        title='GetMyFilters',
        input_model=GetMyFiltersInput,
        output_model=GetMyFiltersOutput,
        tools_used=('get_my_filters',),
        tags=tuple(['Filters']),
    )
    async def get(self, data: GetMyFiltersInput) -> GetMyFiltersOutput:
        """Returns the filters owned by the user. If `includeFavourites` is `true`, the user's visible favorite filters are also returned. **[Permissions](#permissions) required:** Permission to access Jira, however, a favorite filters is only visible to the user where the filter is: * owned by the user. * shared with a group that the user is a member of. * shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for. * shared with a public project. * shared with the public. For example, if the user favorites a public filter that is subsequently made private that filter is not returned by this operation.

Important inputs: expand, include_favourites"""
        tool = self._client.get_tool('get_my_filters')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetMyFiltersOutput.model_validate(coerce_tool_result(result))
