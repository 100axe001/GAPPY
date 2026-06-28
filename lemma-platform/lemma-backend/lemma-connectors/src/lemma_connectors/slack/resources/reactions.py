from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import ReactionsAddToolInput, ReactionsAddToolOutput, ReactionsGetToolInput, ReactionsGetToolOutput, ReactionsListToolInput, ReactionsListToolOutput, ReactionsRemoveToolInput, ReactionsRemoveToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ReactionsAddInput(ReactionsAddToolInput):
    """Operation input for `reactions_add`."""
    pass

class ReactionsAddOutput(ReactionsAddToolOutput):
    """Operation output for `reactions_add`."""
    pass

class ReactionsGetInput(ReactionsGetToolInput):
    """Operation input for `reactions_get`."""
    pass

class ReactionsGetOutput(ReactionsGetToolOutput):
    """Operation output for `reactions_get`."""
    pass

class ReactionsListInput(ReactionsListToolInput):
    """Operation input for `reactions_list`."""
    pass

class ReactionsListOutput(ReactionsListToolOutput):
    """Operation output for `reactions_list`."""
    pass

class ReactionsRemoveInput(ReactionsRemoveToolInput):
    """Operation input for `reactions_remove`."""
    pass

class ReactionsRemoveOutput(ReactionsRemoveToolOutput):
    """Operation output for `reactions_remove`."""
    pass

class SlackReactionsResource(BaseResourceClient):
    """Operations for the `reactions` resource."""

    @operation(
        name='reactions_add',
        title='ReactionsAdd',
        input_model=ReactionsAddInput,
        output_model=ReactionsAddOutput,
        tools_used=('reactions_add',),
        tags=tuple(['reactions']),
    )
    async def add(self, data: ReactionsAddInput) -> ReactionsAddOutput:
        """Adds a reaction to an item.

Important inputs: token, body"""
        tool = self._client.get_tool('reactions_add')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ReactionsAddOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='reactions_get',
        title='ReactionsGet',
        input_model=ReactionsGetInput,
        output_model=ReactionsGetOutput,
        tools_used=('reactions_get',),
        tags=tuple(['reactions']),
    )
    async def get(self, data: ReactionsGetInput) -> ReactionsGetOutput:
        """Gets reactions for an item.

Important inputs: token, channel, file, file_comment, full, timestamp"""
        tool = self._client.get_tool('reactions_get')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ReactionsGetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='reactions_list',
        title='ReactionsList',
        input_model=ReactionsListInput,
        output_model=ReactionsListOutput,
        tools_used=('reactions_list',),
        tags=tuple(['reactions']),
    )
    async def list(self, data: ReactionsListInput) -> ReactionsListOutput:
        """Lists reactions made by a user.

Important inputs: token, user, full, count, page, cursor, limit"""
        tool = self._client.get_tool('reactions_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ReactionsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='reactions_remove',
        title='ReactionsRemove',
        input_model=ReactionsRemoveInput,
        output_model=ReactionsRemoveOutput,
        tools_used=('reactions_remove',),
        tags=tuple(['reactions']),
    )
    async def remove(self, data: ReactionsRemoveInput) -> ReactionsRemoveOutput:
        """Removes a reaction from an item.

Important inputs: token, body"""
        tool = self._client.get_tool('reactions_remove')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ReactionsRemoveOutput.model_validate(coerce_tool_result(result))
