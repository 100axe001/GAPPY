from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetStatusToolInput, GetStatusToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetStatusInput(GetStatusToolInput):
    """Operation input for `get_status`."""
    pass

class GetStatusOutput(GetStatusToolOutput):
    """Operation output for `get_status`."""
    pass

class JiraStatusResource(BaseResourceClient):
    """Operations for the `status` resource."""

    @operation(
        name='get_status',
        title='GetStatus',
        input_model=GetStatusInput,
        output_model=GetStatusOutput,
        tools_used=('get_status',),
        tags=tuple(['Workflow statuses']),
    )
    async def get(self, data: GetStatusInput) -> GetStatusOutput:
        """Returns a status. The status must be associated with an active workflow to be returned. If a name is used on more than one status, only the status found first is returned. Therefore, identifying the status by its ID may be preferable. This operation can be accessed anonymously. [Permissions](#permissions) required: None.

Important inputs: id_or_name"""
        tool = self._client.get_tool('get_status')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetStatusOutput.model_validate(coerce_tool_result(result))
