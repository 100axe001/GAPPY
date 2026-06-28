from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetFiltersPaginatedToolInput, GetFiltersPaginatedToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetFiltersPaginatedInput(GetFiltersPaginatedToolInput):
    """Operation input for `get_filters_paginated`."""
    pass

class GetFiltersPaginatedOutput(GetFiltersPaginatedToolOutput):
    """Operation output for `get_filters_paginated`."""
    pass

class JiraFiltersPaginatedResource(BaseResourceClient):
    """Operations for the `filters_paginated` resource."""

    @operation(
        name='get_filters_paginated',
        title='GetFiltersPaginated',
        input_model=GetFiltersPaginatedInput,
        output_model=GetFiltersPaginatedOutput,
        tools_used=('get_filters_paginated',),
        tags=tuple(['Filters']),
    )
    async def get(self, data: GetFiltersPaginatedInput) -> GetFiltersPaginatedOutput:
        """Returns a [paginated](#pagination) list of filters. Use this operation to get: * specific filters, by defining `id` only. * filters that match all of the specified attributes. For example, all filters for a user with a particular word in their name. When multiple attributes are specified only filters matching all attributes are returned. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None, however, only the following filters that match the query parameters are returned: * filters owned by the user. * filters shared with a group that the user is a member of. * filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for. * filters shared with a public project. * filters shared with the public.

Important inputs: filter_name, account_id, owner, groupname, group_id, project_id, id, order_by, start_at, max_results, expand, override_share_permissions"""
        tool = self._client.get_tool('get_filters_paginated')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetFiltersPaginatedOutput.model_validate(coerce_tool_result(result))
