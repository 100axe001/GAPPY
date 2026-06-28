from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import CallsParticipantsAddToolInput, CallsParticipantsAddToolOutput, CallsParticipantsRemoveToolInput, CallsParticipantsRemoveToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CallsParticipantsAddInput(CallsParticipantsAddToolInput):
    """Operation input for `calls_participants_add`."""
    pass

class CallsParticipantsAddOutput(CallsParticipantsAddToolOutput):
    """Operation output for `calls_participants_add`."""
    pass

class CallsParticipantsRemoveInput(CallsParticipantsRemoveToolInput):
    """Operation input for `calls_participants_remove`."""
    pass

class CallsParticipantsRemoveOutput(CallsParticipantsRemoveToolOutput):
    """Operation output for `calls_participants_remove`."""
    pass

class SlackCallsParticipantsResource(BaseResourceClient):
    """Operations for the `calls_participants` resource."""

    @operation(
        name='calls_participants_add',
        title='CallsParticipantsAdd',
        input_model=CallsParticipantsAddInput,
        output_model=CallsParticipantsAddOutput,
        tools_used=('calls_participants_add',),
        tags=tuple(['calls.participants', 'calls']),
    )
    async def add(self, data: CallsParticipantsAddInput) -> CallsParticipantsAddOutput:
        """Registers new participants added to a Call.

Important inputs: token, body"""
        tool = self._client.get_tool('calls_participants_add')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CallsParticipantsAddOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='calls_participants_remove',
        title='CallsParticipantsRemove',
        input_model=CallsParticipantsRemoveInput,
        output_model=CallsParticipantsRemoveOutput,
        tools_used=('calls_participants_remove',),
        tags=tuple(['calls.participants', 'calls']),
    )
    async def remove(self, data: CallsParticipantsRemoveInput) -> CallsParticipantsRemoveOutput:
        """Registers participants removed from a Call.

Important inputs: token, body"""
        tool = self._client.get_tool('calls_participants_remove')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CallsParticipantsRemoveOutput.model_validate(coerce_tool_result(result))
