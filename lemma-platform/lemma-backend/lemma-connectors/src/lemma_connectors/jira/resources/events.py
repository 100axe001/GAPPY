from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetEventsToolInput, GetEventsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetEventsInput(GetEventsToolInput):
    """Operation input for `get_events`."""
    pass

class GetEventsOutput(GetEventsToolOutput):
    """Operation output for `get_events`."""
    pass

class JiraEventsResource(BaseResourceClient):
    """Operations for the `events` resource."""

    @operation(
        name='get_events',
        title='GetEvents',
        input_model=GetEventsInput,
        output_model=GetEventsOutput,
        tools_used=('get_events',),
        tags=tuple(['Issues']),
    )
    async def get(self, data: GetEventsInput) -> GetEventsOutput:
        """Returns all issue events. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_events')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetEventsOutput.model_validate(coerce_tool_result(result))
