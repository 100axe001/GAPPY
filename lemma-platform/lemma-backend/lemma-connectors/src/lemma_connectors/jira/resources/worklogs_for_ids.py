from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetWorklogsForIdsToolInput, GetWorklogsForIdsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetWorklogsForIdsInput(GetWorklogsForIdsToolInput):
    """Operation input for `get_worklogs_for_ids`."""
    pass

class GetWorklogsForIdsOutput(GetWorklogsForIdsToolOutput):
    """Operation output for `get_worklogs_for_ids`."""
    pass

class JiraWorklogsForIdsResource(BaseResourceClient):
    """Operations for the `worklogs_for_ids` resource."""

    @operation(
        name='get_worklogs_for_ids',
        title='GetWorklogsForIds',
        input_model=GetWorklogsForIdsInput,
        output_model=GetWorklogsForIdsOutput,
        tools_used=('get_worklogs_for_ids',),
        tags=tuple(['Issue worklogs']),
    )
    async def get(self, data: GetWorklogsForIdsInput) -> GetWorklogsForIdsOutput:
        """Returns worklog details for a list of worklog IDs. The returned list of worklogs is limited to 1000 items. **[Permissions](#permissions) required:** Permission to access Jira, however, worklogs are only returned where either of the following is true: * the worklog is set as *Viewable by All Users*. * the user is a member of a project role or group with permission to view the worklog.

Important inputs: expand, body"""
        tool = self._client.get_tool('get_worklogs_for_ids')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetWorklogsForIdsOutput.model_validate(coerce_tool_result(result))
