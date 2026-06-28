from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllGadgetsToolInput, GetAllGadgetsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllGadgetsInput(GetAllGadgetsToolInput):
    """Operation input for `get_all_gadgets`."""
    pass

class GetAllGadgetsOutput(GetAllGadgetsToolOutput):
    """Operation output for `get_all_gadgets`."""
    pass

class JiraAllGadgetsResource(BaseResourceClient):
    """Operations for the `all_gadgets` resource."""

    @operation(
        name='get_all_gadgets',
        title='GetAllGadgets',
        input_model=GetAllGadgetsInput,
        output_model=GetAllGadgetsOutput,
        tools_used=('get_all_gadgets',),
        tags=tuple(['Dashboards']),
    )
    async def get(self, data: GetAllGadgetsInput) -> GetAllGadgetsOutput:
        """Returns a list of dashboard gadgets on a dashboard. This operation returns: * Gadgets from a list of IDs, when `id` is set. * Gadgets with a module key, when `moduleKey` is set. * Gadgets from a list of URIs, when `uri` is set. * All gadgets, when no other parameters are set. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: dashboard_id, module_key, uri, gadget_id"""
        tool = self._client.get_tool('get_all_gadgets')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllGadgetsOutput.model_validate(coerce_tool_result(result))
