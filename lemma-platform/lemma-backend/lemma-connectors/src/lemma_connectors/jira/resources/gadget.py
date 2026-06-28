from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddGadgetToolInput, AddGadgetToolOutput, RemoveGadgetToolInput, RemoveGadgetToolOutput, UpdateGadgetToolInput, UpdateGadgetToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddGadgetInput(AddGadgetToolInput):
    """Operation input for `add_gadget`."""
    pass

class AddGadgetOutput(AddGadgetToolOutput):
    """Operation output for `add_gadget`."""
    pass

class RemoveGadgetInput(RemoveGadgetToolInput):
    """Operation input for `remove_gadget`."""
    pass

class RemoveGadgetOutput(RemoveGadgetToolOutput):
    """Operation output for `remove_gadget`."""
    pass

class UpdateGadgetInput(UpdateGadgetToolInput):
    """Operation input for `update_gadget`."""
    pass

class UpdateGadgetOutput(UpdateGadgetToolOutput):
    """Operation output for `update_gadget`."""
    pass

class JiraGadgetResource(BaseResourceClient):
    """Operations for the `gadget` resource."""

    @operation(
        name='add_gadget',
        title='AddGadget',
        input_model=AddGadgetInput,
        output_model=AddGadgetOutput,
        tools_used=('add_gadget',),
        tags=tuple(['Dashboards']),
    )
    async def add(self, data: AddGadgetInput) -> AddGadgetOutput:
        """Adds a gadget to a dashboard. **[Permissions](#permissions) required:** None.

Important inputs: dashboard_id, body"""
        tool = self._client.get_tool('add_gadget')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddGadgetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='remove_gadget',
        title='RemoveGadget',
        input_model=RemoveGadgetInput,
        output_model=RemoveGadgetOutput,
        tools_used=('remove_gadget',),
        tags=tuple(['Dashboards']),
    )
    async def remove(self, data: RemoveGadgetInput) -> RemoveGadgetOutput:
        """Removes a dashboard gadget from a dashboard. When a gadget is removed from a dashboard, other gadgets in the same column are moved up to fill the emptied position. **[Permissions](#permissions) required:** None.

Important inputs: dashboard_id, gadget_id"""
        tool = self._client.get_tool('remove_gadget')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemoveGadgetOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_gadget',
        title='UpdateGadget',
        input_model=UpdateGadgetInput,
        output_model=UpdateGadgetOutput,
        tools_used=('update_gadget',),
        tags=tuple(['Dashboards']),
    )
    async def update(self, data: UpdateGadgetInput) -> UpdateGadgetOutput:
        """Changes the title, position, and color of the gadget on a dashboard. **[Permissions](#permissions) required:** None.

Important inputs: dashboard_id, gadget_id, body"""
        tool = self._client.get_tool('update_gadget')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateGadgetOutput.model_validate(coerce_tool_result(result))
