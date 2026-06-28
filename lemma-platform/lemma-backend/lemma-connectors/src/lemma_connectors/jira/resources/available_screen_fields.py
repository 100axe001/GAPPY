from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAvailableScreenFieldsToolInput, GetAvailableScreenFieldsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAvailableScreenFieldsInput(GetAvailableScreenFieldsToolInput):
    """Operation input for `get_available_screen_fields`."""
    pass

class GetAvailableScreenFieldsOutput(GetAvailableScreenFieldsToolOutput):
    """Operation output for `get_available_screen_fields`."""
    pass

class JiraAvailableScreenFieldsResource(BaseResourceClient):
    """Operations for the `available_screen_fields` resource."""

    @operation(
        name='get_available_screen_fields',
        title='GetAvailableScreenFields',
        input_model=GetAvailableScreenFieldsInput,
        output_model=GetAvailableScreenFieldsOutput,
        tools_used=('get_available_screen_fields',),
        tags=tuple(['Screens']),
    )
    async def get(self, data: GetAvailableScreenFieldsInput) -> GetAvailableScreenFieldsOutput:
        """Returns the fields that can be added to a tab on a screen. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: screen_id"""
        tool = self._client.get_tool('get_available_screen_fields')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAvailableScreenFieldsOutput.model_validate(coerce_tool_result(result))
