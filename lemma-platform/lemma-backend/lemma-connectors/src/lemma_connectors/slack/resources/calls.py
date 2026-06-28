from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import CallsAddToolInput, CallsAddToolOutput, CallsEndToolInput, CallsEndToolOutput, CallsInfoToolInput, CallsInfoToolOutput, CallsUpdateToolInput, CallsUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CallsAddInput(CallsAddToolInput):
    """Operation input for `calls_add`."""
    pass

class CallsAddOutput(CallsAddToolOutput):
    """Operation output for `calls_add`."""
    pass

class CallsEndInput(CallsEndToolInput):
    """Operation input for `calls_end`."""
    pass

class CallsEndOutput(CallsEndToolOutput):
    """Operation output for `calls_end`."""
    pass

class CallsInfoInput(CallsInfoToolInput):
    """Operation input for `calls_info`."""
    pass

class CallsInfoOutput(CallsInfoToolOutput):
    """Operation output for `calls_info`."""
    pass

class CallsUpdateInput(CallsUpdateToolInput):
    """Operation input for `calls_update`."""
    pass

class CallsUpdateOutput(CallsUpdateToolOutput):
    """Operation output for `calls_update`."""
    pass

class SlackCallsResource(BaseResourceClient):
    """Operations for the `calls` resource."""

    @operation(
        name='calls_add',
        title='CallsAdd',
        input_model=CallsAddInput,
        output_model=CallsAddOutput,
        tools_used=('calls_add',),
        tags=tuple(['calls']),
    )
    async def add(self, data: CallsAddInput) -> CallsAddOutput:
        """Registers a new Call.

Important inputs: token, body"""
        tool = self._client.get_tool('calls_add')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CallsAddOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='calls_end',
        title='CallsEnd',
        input_model=CallsEndInput,
        output_model=CallsEndOutput,
        tools_used=('calls_end',),
        tags=tuple(['calls']),
    )
    async def end(self, data: CallsEndInput) -> CallsEndOutput:
        """Ends a Call.

Important inputs: token, body"""
        tool = self._client.get_tool('calls_end')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CallsEndOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='calls_info',
        title='CallsInfo',
        input_model=CallsInfoInput,
        output_model=CallsInfoOutput,
        tools_used=('calls_info',),
        tags=tuple(['calls']),
    )
    async def info(self, data: CallsInfoInput) -> CallsInfoOutput:
        """Returns information about a Call.

Important inputs: token, id"""
        tool = self._client.get_tool('calls_info')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CallsInfoOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='calls_update',
        title='CallsUpdate',
        input_model=CallsUpdateInput,
        output_model=CallsUpdateOutput,
        tools_used=('calls_update',),
        tags=tuple(['calls']),
    )
    async def update(self, data: CallsUpdateInput) -> CallsUpdateOutput:
        """Updates information about a Call.

Important inputs: token, body"""
        tool = self._client.get_tool('calls_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CallsUpdateOutput.model_validate(coerce_tool_result(result))
