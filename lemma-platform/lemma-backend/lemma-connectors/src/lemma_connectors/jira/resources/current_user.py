from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetCurrentUserToolInput, GetCurrentUserToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetCurrentUserInput(GetCurrentUserToolInput):
    """Operation input for `get_current_user`."""
    pass

class GetCurrentUserOutput(GetCurrentUserToolOutput):
    """Operation output for `get_current_user`."""
    pass

class JiraCurrentUserResource(BaseResourceClient):
    """Operations for the `current_user` resource."""

    @operation(
        name='get_current_user',
        title='GetCurrentUser',
        input_model=GetCurrentUserInput,
        output_model=GetCurrentUserOutput,
        tools_used=('get_current_user',),
        tags=tuple(['Myself']),
    )
    async def get(self, data: GetCurrentUserInput) -> GetCurrentUserOutput:
        """Returns details for the current user. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: expand"""
        tool = self._client.get_tool('get_current_user')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetCurrentUserOutput.model_validate(coerce_tool_result(result))
