from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIdsOfWorklogsDeletedSinceToolInput, GetIdsOfWorklogsDeletedSinceToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIdsOfWorklogsDeletedSinceInput(GetIdsOfWorklogsDeletedSinceToolInput):
    """Operation input for `get_ids_of_worklogs_deleted_since`."""
    pass

class GetIdsOfWorklogsDeletedSinceOutput(GetIdsOfWorklogsDeletedSinceToolOutput):
    """Operation output for `get_ids_of_worklogs_deleted_since`."""
    pass

class JiraIdsOfWorklogsDeletedSinceResource(BaseResourceClient):
    """Operations for the `ids_of_worklogs_deleted_since` resource."""

    @operation(
        name='get_ids_of_worklogs_deleted_since',
        title='GetIdsOfWorklogsDeletedSince',
        input_model=GetIdsOfWorklogsDeletedSinceInput,
        output_model=GetIdsOfWorklogsDeletedSinceOutput,
        tools_used=('get_ids_of_worklogs_deleted_since',),
        tags=tuple(['Issue worklogs']),
    )
    async def get(self, data: GetIdsOfWorklogsDeletedSinceInput) -> GetIdsOfWorklogsDeletedSinceOutput:
        """Returns a list of IDs and delete timestamps for worklogs deleted after a date and time. This resource is paginated, with a limit of 1000 worklogs per page. Each page lists worklogs from oldest to youngest. If the number of items in the date range exceeds 1000, `until` indicates the timestamp of the youngest item on the page. Also, `nextPage` provides the URL for the next page of worklogs. The `lastPage` parameter is set to true on the last page of worklogs. This resource does not return worklogs deleted during the minute preceding the request. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: since"""
        tool = self._client.get_tool('get_ids_of_worklogs_deleted_since')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIdsOfWorklogsDeletedSinceOutput.model_validate(coerce_tool_result(result))
