from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetChangeLogsByIdsToolInput, GetChangeLogsByIdsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetChangeLogsByIdsInput(GetChangeLogsByIdsToolInput):
    """Operation input for `get_change_logs_by_ids`."""
    pass

class GetChangeLogsByIdsOutput(GetChangeLogsByIdsToolOutput):
    """Operation output for `get_change_logs_by_ids`."""
    pass

class JiraChangeLogsByIdsResource(BaseResourceClient):
    """Operations for the `change_logs_by_ids` resource."""

    @operation(
        name='get_change_logs_by_ids',
        title='GetChangeLogsByIds',
        input_model=GetChangeLogsByIdsInput,
        output_model=GetChangeLogsByIdsOutput,
        tools_used=('get_change_logs_by_ids',),
        tags=tuple(['Issues']),
    )
    async def get(self, data: GetChangeLogsByIdsInput) -> GetChangeLogsByIdsOutput:
        """Returns changelogs for an issue specified by a list of changelog IDs. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, body"""
        tool = self._client.get_tool('get_change_logs_by_ids')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetChangeLogsByIdsOutput.model_validate(coerce_tool_result(result))
