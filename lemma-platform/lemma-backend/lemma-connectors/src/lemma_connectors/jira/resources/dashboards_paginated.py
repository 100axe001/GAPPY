from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetDashboardsPaginatedToolInput, GetDashboardsPaginatedToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetDashboardsPaginatedInput(GetDashboardsPaginatedToolInput):
    """Operation input for `get_dashboards_paginated`."""
    pass

class GetDashboardsPaginatedOutput(GetDashboardsPaginatedToolOutput):
    """Operation output for `get_dashboards_paginated`."""
    pass

class JiraDashboardsPaginatedResource(BaseResourceClient):
    """Operations for the `dashboards_paginated` resource."""

    @operation(
        name='get_dashboards_paginated',
        title='GetDashboardsPaginated',
        input_model=GetDashboardsPaginatedInput,
        output_model=GetDashboardsPaginatedOutput,
        tools_used=('get_dashboards_paginated',),
        tags=tuple(['Dashboards']),
    )
    async def get(self, data: GetDashboardsPaginatedInput) -> GetDashboardsPaginatedOutput:
        """Returns a [paginated](#pagination) list of dashboards. This operation is similar to [Get dashboards](#api-rest-api-3-dashboard-get) except that the results can be refined to include dashboards that have specific attributes. For example, dashboards with a particular name. When multiple attributes are specified only filters matching all attributes are returned. This operation can be accessed anonymously. **[Permissions](#permissions) required:** The following dashboards that match the query parameters are returned: * Dashboards owned by the user. Not returned for anonymous users. * Dashboards shared with a group that the user is a member of. Not returned for anonymous users. * Dashboards shared with a private project that the user can browse. Not returned for anonymous users. * Dashboards shared with a public project. * Dashboards shared with the public.

Important inputs: dashboard_name, account_id, owner, groupname, group_id, project_id, order_by, start_at, max_results, status, expand"""
        tool = self._client.get_tool('get_dashboards_paginated')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetDashboardsPaginatedOutput.model_validate(coerce_tool_result(result))
