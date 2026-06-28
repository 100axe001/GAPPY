from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetPrecomputationsToolInput, GetPrecomputationsToolOutput, UpdatePrecomputationsToolInput, UpdatePrecomputationsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetPrecomputationsInput(GetPrecomputationsToolInput):
    """Operation input for `get_precomputations`."""
    pass

class GetPrecomputationsOutput(GetPrecomputationsToolOutput):
    """Operation output for `get_precomputations`."""
    pass

class UpdatePrecomputationsInput(UpdatePrecomputationsToolInput):
    """Operation input for `update_precomputations`."""
    pass

class UpdatePrecomputationsOutput(UpdatePrecomputationsToolOutput):
    """Operation output for `update_precomputations`."""
    pass

class JiraPrecomputationsResource(BaseResourceClient):
    """Operations for the `precomputations` resource."""

    @operation(
        name='get_precomputations',
        title='GetPrecomputations',
        input_model=GetPrecomputationsInput,
        output_model=GetPrecomputationsOutput,
        tools_used=('get_precomputations',),
        tags=tuple([]),
    )
    async def get(self, data: GetPrecomputationsInput) -> GetPrecomputationsOutput:
        """Get precomputation.

Important inputs: function_key, start_at, max_results, order_by, filter"""
        tool = self._client.get_tool('get_precomputations')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetPrecomputationsOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_precomputations',
        title='UpdatePrecomputations',
        input_model=UpdatePrecomputationsInput,
        output_model=UpdatePrecomputationsOutput,
        tools_used=('update_precomputations',),
        tags=tuple([]),
    )
    async def update(self, data: UpdatePrecomputationsInput) -> UpdatePrecomputationsOutput:
        """Update precomputations.

Important inputs: body"""
        tool = self._client.get_tool('update_precomputations')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdatePrecomputationsOutput.model_validate(coerce_tool_result(result))
