from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetScreensToolInput, GetScreensToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetScreensInput(GetScreensToolInput):
    """Operation input for `get_screens`."""
    pass

class GetScreensOutput(GetScreensToolOutput):
    """Operation output for `get_screens`."""
    pass

class JiraScreensResource(BaseResourceClient):
    """Operations for the `screens` resource."""

    @operation(
        name='get_screens',
        title='GetScreens',
        input_model=GetScreensInput,
        output_model=GetScreensOutput,
        tools_used=('get_screens',),
        tags=tuple(['Screens']),
    )
    async def get(self, data: GetScreensInput) -> GetScreensOutput:
        """Returns a [paginated](#pagination) list of all screens or those specified by one or more screen IDs. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, id, query_string, scope, order_by"""
        tool = self._client.get_tool('get_screens')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetScreensOutput.model_validate(coerce_tool_result(result))
