from __future__ import annotations

from lemma_connectors.google_drive.generated.tool_types import DriveChannelsStopToolInput, DriveChannelsStopToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ChannelsStopInput(DriveChannelsStopToolInput):
    """Operation input for `channels_stop`."""
    pass

class ChannelsStopOutput(DriveChannelsStopToolOutput):
    """Operation output for `channels_stop`."""
    pass

class GoogleDriveChannelsResource(BaseResourceClient):
    """Operations for the `channels` resource."""

    @operation(
        name='channels_stop',
        title='ChannelsStop',
        input_model=ChannelsStopInput,
        output_model=ChannelsStopOutput,
        tools_used=('drive_channels_stop',),
        tags=tuple(['channels']),
    )
    async def stop(self, data: ChannelsStopInput) -> ChannelsStopOutput:
        """Stop watching resources through this channel.

Important inputs: fields, body"""
        tool = self._client.get_tool('drive_channels_stop')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ChannelsStopOutput.model_validate(coerce_tool_result(result))
