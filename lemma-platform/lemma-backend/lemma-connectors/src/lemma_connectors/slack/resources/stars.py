from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import StarsAddToolInput, StarsAddToolOutput, StarsListToolInput, StarsListToolOutput, StarsRemoveToolInput, StarsRemoveToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class StarsAddInput(StarsAddToolInput):
    """Operation input for `stars_add`."""
    pass

class StarsAddOutput(StarsAddToolOutput):
    """Operation output for `stars_add`."""
    pass

class StarsListInput(StarsListToolInput):
    """Operation input for `stars_list`."""
    pass

class StarsListOutput(StarsListToolOutput):
    """Operation output for `stars_list`."""
    pass

class StarsRemoveInput(StarsRemoveToolInput):
    """Operation input for `stars_remove`."""
    pass

class StarsRemoveOutput(StarsRemoveToolOutput):
    """Operation output for `stars_remove`."""
    pass

class SlackStarsResource(BaseResourceClient):
    """Operations for the `stars` resource."""

    @operation(
        name='stars_add',
        title='StarsAdd',
        input_model=StarsAddInput,
        output_model=StarsAddOutput,
        tools_used=('stars_add',),
        tags=tuple(['stars']),
    )
    async def add(self, data: StarsAddInput) -> StarsAddOutput:
        """Adds a star to an item.

Important inputs: token, body"""
        tool = self._client.get_tool('stars_add')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return StarsAddOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='stars_list',
        title='StarsList',
        input_model=StarsListInput,
        output_model=StarsListOutput,
        tools_used=('stars_list',),
        tags=tuple(['stars']),
    )
    async def list(self, data: StarsListInput) -> StarsListOutput:
        """Lists stars for a user.

Important inputs: token, count, page, cursor, limit"""
        tool = self._client.get_tool('stars_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return StarsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='stars_remove',
        title='StarsRemove',
        input_model=StarsRemoveInput,
        output_model=StarsRemoveOutput,
        tools_used=('stars_remove',),
        tags=tuple(['stars']),
    )
    async def remove(self, data: StarsRemoveInput) -> StarsRemoveOutput:
        """Removes a star from an item.

Important inputs: token, body"""
        tool = self._client.get_tool('stars_remove')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return StarsRemoveOutput.model_validate(coerce_tool_result(result))
