from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetUiModificationsToolInput, GetUiModificationsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetUiModificationsInput(GetUiModificationsToolInput):
    """Operation input for `get_ui_modifications`."""
    pass

class GetUiModificationsOutput(GetUiModificationsToolOutput):
    """Operation output for `get_ui_modifications`."""
    pass

class JiraUiModificationsResource(BaseResourceClient):
    """Operations for the `ui_modifications` resource."""

    @operation(
        name='get_ui_modifications',
        title='GetUiModifications',
        input_model=GetUiModificationsInput,
        output_model=GetUiModificationsOutput,
        tools_used=('get_ui_modifications',),
        tags=tuple(['UI modifications (apps)']),
    )
    async def get(self, data: GetUiModificationsInput) -> GetUiModificationsOutput:
        """Gets UI modifications. UI modifications can only be retrieved by Forge apps. **[Permissions](#permissions) required:** None.

Important inputs: start_at, max_results, expand"""
        tool = self._client.get_tool('get_ui_modifications')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetUiModificationsOutput.model_validate(coerce_tool_result(result))
