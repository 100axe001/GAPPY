from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetServerInfoToolInput, GetServerInfoToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetServerInfoInput(GetServerInfoToolInput):
    """Operation input for `get_server_info`."""
    pass

class GetServerInfoOutput(GetServerInfoToolOutput):
    """Operation output for `get_server_info`."""
    pass

class JiraServerInfoResource(BaseResourceClient):
    """Operations for the `server_info` resource."""

    @operation(
        name='get_server_info',
        title='GetServerInfo',
        input_model=GetServerInfoInput,
        output_model=GetServerInfoOutput,
        tools_used=('get_server_info',),
        tags=tuple(['Server info']),
    )
    async def get(self, data: GetServerInfoInput) -> GetServerInfoOutput:
        """Returns information about the Jira instance. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_server_info')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetServerInfoOutput.model_validate(coerce_tool_result(result))
