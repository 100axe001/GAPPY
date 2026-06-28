from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllLabelsToolInput, GetAllLabelsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllLabelsInput(GetAllLabelsToolInput):
    """Operation input for `get_all_labels`."""
    pass

class GetAllLabelsOutput(GetAllLabelsToolOutput):
    """Operation output for `get_all_labels`."""
    pass

class JiraAllLabelsResource(BaseResourceClient):
    """Operations for the `all_labels` resource."""

    @operation(
        name='get_all_labels',
        title='GetAllLabels',
        input_model=GetAllLabelsInput,
        output_model=GetAllLabelsOutput,
        tools_used=('get_all_labels',),
        tags=tuple(['Labels']),
    )
    async def get(self, data: GetAllLabelsInput) -> GetAllLabelsOutput:
        """Returns a [paginated](#pagination) list of labels.

Important inputs: start_at, max_results"""
        tool = self._client.get_tool('get_all_labels')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllLabelsOutput.model_validate(coerce_tool_result(result))
