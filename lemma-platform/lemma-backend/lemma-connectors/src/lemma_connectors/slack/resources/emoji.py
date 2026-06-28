from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import EmojiListToolInput, EmojiListToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class EmojiListInput(EmojiListToolInput):
    """Operation input for `emoji_list`."""
    pass

class EmojiListOutput(EmojiListToolOutput):
    """Operation output for `emoji_list`."""
    pass

class SlackEmojiResource(BaseResourceClient):
    """Operations for the `emoji` resource."""

    @operation(
        name='emoji_list',
        title='EmojiList',
        input_model=EmojiListInput,
        output_model=EmojiListOutput,
        tools_used=('emoji_list',),
        tags=tuple(['emoji']),
    )
    async def list(self, data: EmojiListInput) -> EmojiListOutput:
        """Lists custom emoji for a team.

Important inputs: token"""
        tool = self._client.get_tool('emoji_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return EmojiListOutput.model_validate(coerce_tool_result(result))
