from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import RtmConnectToolInput, RtmConnectToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class RtmConnectInput(RtmConnectToolInput):
    """Operation input for `rtm_connect`."""
    pass

class RtmConnectOutput(RtmConnectToolOutput):
    """Operation output for `rtm_connect`."""
    pass

class SlackRtmResource(BaseResourceClient):
    """Operations for the `rtm` resource."""

    @operation(
        name='rtm_connect',
        title='RtmConnect',
        input_model=RtmConnectInput,
        output_model=RtmConnectOutput,
        tools_used=('rtm_connect',),
        tags=tuple(['rtm']),
    )
    async def connect(self, data: RtmConnectInput) -> RtmConnectOutput:
        """Starts a Real Time Messaging session.

Important inputs: token, batch_presence_aware, presence_sub"""
        tool = self._client.get_tool('rtm_connect')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RtmConnectOutput.model_validate(coerce_tool_result(result))
