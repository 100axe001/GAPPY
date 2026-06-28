from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIdsOfWorklogsModifiedSinceToolInput, GetIdsOfWorklogsModifiedSinceToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIdsOfWorklogsModifiedSinceInput(GetIdsOfWorklogsModifiedSinceToolInput):
    """Operation input for `get_ids_of_worklogs_modified_since`."""
    pass

class GetIdsOfWorklogsModifiedSinceOutput(GetIdsOfWorklogsModifiedSinceToolOutput):
    """Operation output for `get_ids_of_worklogs_modified_since`."""
    pass

class JiraIdsOfWorklogsModifiedSinceResource(BaseResourceClient):
    """Operations for the `ids_of_worklogs_modified_since` resource."""

    @operation(
        name='get_ids_of_worklogs_modified_since',
        title='GetIdsOfWorklogsModifiedSince',
        input_model=GetIdsOfWorklogsModifiedSinceInput,
        output_model=GetIdsOfWorklogsModifiedSinceOutput,
        tools_used=('get_ids_of_worklogs_modified_since',),
        tags=tuple(['Issue worklogs']),
    )
    async def get(self, data: GetIdsOfWorklogsModifiedSinceInput) -> GetIdsOfWorklogsModifiedSinceOutput:
        """Returns a list of IDs and update timestamps for worklogs updated after a date and time. This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of worklogs. The `lastPage` parameter is set to true on the last page of worklogs. This resource does not return worklogs updated during the minute preceding the request. **[Permissions](#permissions) required:** Permission to access Jira, however, worklogs are only returned where either of the following is true: * the worklog is set as *Viewable by All Users*. * the user is a member of a project role or group with permission to view the worklog.

Important inputs: since, expand"""
        tool = self._client.get_tool('get_ids_of_worklogs_modified_since')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIdsOfWorklogsModifiedSinceOutput.model_validate(coerce_tool_result(result))
