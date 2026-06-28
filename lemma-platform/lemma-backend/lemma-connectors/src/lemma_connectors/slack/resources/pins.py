from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import PinsAddToolInput, PinsAddToolOutput, PinsListToolInput, PinsListToolOutput, PinsRemoveToolInput, PinsRemoveToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class PinsAddInput(PinsAddToolInput):
    """Operation input for `pins_add`."""
    pass

class PinsAddOutput(PinsAddToolOutput):
    """Operation output for `pins_add`."""
    pass

class PinsListInput(PinsListToolInput):
    """Operation input for `pins_list`."""
    pass

class PinsListOutput(PinsListToolOutput):
    """Operation output for `pins_list`."""
    pass

class PinsRemoveInput(PinsRemoveToolInput):
    """Operation input for `pins_remove`."""
    pass

class PinsRemoveOutput(PinsRemoveToolOutput):
    """Operation output for `pins_remove`."""
    pass

class SlackPinsResource(BaseResourceClient):
    """Operations for the `pins` resource."""

    @operation(
        name='pins_add',
        title='PinsAdd',
        input_model=PinsAddInput,
        output_model=PinsAddOutput,
        tools_used=('pins_add',),
        tags=tuple(['pins']),
    )
    async def add(self, data: PinsAddInput) -> PinsAddOutput:
        """Pins an item to a channel.

Important inputs: token, body"""
        tool = self._client.get_tool('pins_add')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return PinsAddOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='pins_list',
        title='PinsList',
        input_model=PinsListInput,
        output_model=PinsListOutput,
        tools_used=('pins_list',),
        tags=tuple(['pins']),
    )
    async def list(self, data: PinsListInput) -> PinsListOutput:
        """Lists items pinned to a channel.

Important inputs: token, channel"""
        tool = self._client.get_tool('pins_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return PinsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='pins_remove',
        title='PinsRemove',
        input_model=PinsRemoveInput,
        output_model=PinsRemoveOutput,
        tools_used=('pins_remove',),
        tags=tuple(['pins']),
    )
    async def remove(self, data: PinsRemoveInput) -> PinsRemoveOutput:
        """Un-pins an item from a channel.

Important inputs: token, body"""
        tool = self._client.get_tool('pins_remove')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return PinsRemoveOutput.model_validate(coerce_tool_result(result))
