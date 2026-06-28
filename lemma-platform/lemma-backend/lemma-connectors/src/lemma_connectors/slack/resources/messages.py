from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import SearchMessagesToolInput, SearchMessagesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class SearchMessagesInput(SearchMessagesToolInput):
    """Operation input for `search_messages`."""
    pass

class SearchMessagesOutput(SearchMessagesToolOutput):
    """Operation output for `search_messages`."""
    pass

class SlackMessagesResource(BaseResourceClient):
    """Operations for the `messages` resource."""

    @operation(
        name='search_messages',
        title='SearchMessages',
        input_model=SearchMessagesInput,
        output_model=SearchMessagesOutput,
        tools_used=('search_messages',),
        tags=tuple(['search']),
    )
    async def search(self, data: SearchMessagesInput) -> SearchMessagesOutput:
        """Searches for messages matching a query.

Important inputs: token, count, highlight, page, query, sort, sort_dir"""
        tool = self._client.get_tool('search_messages')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SearchMessagesOutput.model_validate(coerce_tool_result(result))
