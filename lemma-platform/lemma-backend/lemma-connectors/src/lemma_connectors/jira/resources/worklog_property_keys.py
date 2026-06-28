from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetWorklogPropertyKeysToolInput, GetWorklogPropertyKeysToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetWorklogPropertyKeysInput(GetWorklogPropertyKeysToolInput):
    """Operation input for `get_worklog_property_keys`."""
    pass

class GetWorklogPropertyKeysOutput(GetWorklogPropertyKeysToolOutput):
    """Operation output for `get_worklog_property_keys`."""
    pass

class JiraWorklogPropertyKeysResource(BaseResourceClient):
    """Operations for the `worklog_property_keys` resource."""

    @operation(
        name='get_worklog_property_keys',
        title='GetWorklogPropertyKeys',
        input_model=GetWorklogPropertyKeysInput,
        output_model=GetWorklogPropertyKeysOutput,
        tools_used=('get_worklog_property_keys',),
        tags=tuple(['Issue worklog properties']),
    )
    async def get(self, data: GetWorklogPropertyKeysInput) -> GetWorklogPropertyKeysOutput:
        """Returns the keys of all properties for a worklog. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * If the worklog has visibility restrictions, belongs to the group or has the role visibility is restricted to.

Important inputs: issue_id_or_key, worklog_id"""
        tool = self._client.get_tool('get_worklog_property_keys')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetWorklogPropertyKeysOutput.model_validate(coerce_tool_result(result))
