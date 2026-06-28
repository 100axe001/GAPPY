from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetScreenSchemesToolInput, GetScreenSchemesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetScreenSchemesInput(GetScreenSchemesToolInput):
    """Operation input for `get_screen_schemes`."""
    pass

class GetScreenSchemesOutput(GetScreenSchemesToolOutput):
    """Operation output for `get_screen_schemes`."""
    pass

class JiraScreenSchemesResource(BaseResourceClient):
    """Operations for the `screen_schemes` resource."""

    @operation(
        name='get_screen_schemes',
        title='GetScreenSchemes',
        input_model=GetScreenSchemesInput,
        output_model=GetScreenSchemesOutput,
        tools_used=('get_screen_schemes',),
        tags=tuple(['Screen schemes']),
    )
    async def get(self, data: GetScreenSchemesInput) -> GetScreenSchemesOutput:
        """Returns a [paginated](#pagination) list of screen schemes. Only screen schemes used in classic projects are returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: start_at, max_results, id, expand, query_string, order_by"""
        tool = self._client.get_tool('get_screen_schemes')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetScreenSchemesOutput.model_validate(coerce_tool_result(result))
