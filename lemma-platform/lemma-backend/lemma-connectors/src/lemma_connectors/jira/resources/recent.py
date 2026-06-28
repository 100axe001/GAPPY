from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetRecentToolInput, GetRecentToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetRecentInput(GetRecentToolInput):
    """Operation input for `get_recent`."""
    pass

class GetRecentOutput(GetRecentToolOutput):
    """Operation output for `get_recent`."""
    pass

class JiraRecentResource(BaseResourceClient):
    """Operations for the `recent` resource."""

    @operation(
        name='get_recent',
        title='GetRecent',
        input_model=GetRecentInput,
        output_model=GetRecentOutput,
        tools_used=('get_recent',),
        tags=tuple(['Projects']),
    )
    async def get(self, data: GetRecentInput) -> GetRecentOutput:
        """Returns a list of up to 20 projects recently viewed by the user that are still visible to the user. This operation can be accessed anonymously. **[Permissions](#permissions) required:** Projects are returned only where the user has one of: * *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project. * *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project. * *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: expand, properties"""
        tool = self._client.get_tool('get_recent')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetRecentOutput.model_validate(coerce_tool_result(result))
