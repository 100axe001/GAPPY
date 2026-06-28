from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import BotsInfoToolInput, BotsInfoToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class BotsInfoInput(BotsInfoToolInput):
    """Operation input for `bots_info`."""
    pass

class BotsInfoOutput(BotsInfoToolOutput):
    """Operation output for `bots_info`."""
    pass

class SlackBotsResource(BaseResourceClient):
    """Operations for the `bots` resource."""

    @operation(
        name='bots_info',
        title='BotsInfo',
        input_model=BotsInfoInput,
        output_model=BotsInfoOutput,
        tools_used=('bots_info',),
        tags=tuple(['bots']),
    )
    async def info(self, data: BotsInfoInput) -> BotsInfoOutput:
        """Gets information about a bot user.

Important inputs: token, bot"""
        tool = self._client.get_tool('bots_info')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return BotsInfoOutput.model_validate(coerce_tool_result(result))
