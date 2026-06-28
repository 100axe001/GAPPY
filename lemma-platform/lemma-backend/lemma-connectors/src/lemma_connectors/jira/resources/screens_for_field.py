from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetScreensForFieldToolInput, GetScreensForFieldToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetScreensForFieldInput(GetScreensForFieldToolInput):
    """Operation input for `get_screens_for_field`."""
    pass

class GetScreensForFieldOutput(GetScreensForFieldToolOutput):
    """Operation output for `get_screens_for_field`."""
    pass

class JiraScreensForFieldResource(BaseResourceClient):
    """Operations for the `screens_for_field` resource."""

    @operation(
        name='get_screens_for_field',
        title='GetScreensForField',
        input_model=GetScreensForFieldInput,
        output_model=GetScreensForFieldOutput,
        tools_used=('get_screens_for_field',),
        tags=tuple(['Screens']),
    )
    async def get(self, data: GetScreensForFieldInput) -> GetScreensForFieldOutput:
        """Returns a [paginated](#pagination) list of the screens a field is used in. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: field_id, start_at, max_results, expand"""
        tool = self._client.get_tool('get_screens_for_field')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetScreensForFieldOutput.model_validate(coerce_tool_result(result))
