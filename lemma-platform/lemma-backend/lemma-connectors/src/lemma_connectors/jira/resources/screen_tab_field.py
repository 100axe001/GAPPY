from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddScreenTabFieldToolInput, AddScreenTabFieldToolOutput, MoveScreenTabFieldToolInput, MoveScreenTabFieldToolOutput, RemoveScreenTabFieldToolInput, RemoveScreenTabFieldToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddScreenTabFieldInput(AddScreenTabFieldToolInput):
    """Operation input for `add_screen_tab_field`."""
    pass

class AddScreenTabFieldOutput(AddScreenTabFieldToolOutput):
    """Operation output for `add_screen_tab_field`."""
    pass

class MoveScreenTabFieldInput(MoveScreenTabFieldToolInput):
    """Operation input for `move_screen_tab_field`."""
    pass

class MoveScreenTabFieldOutput(MoveScreenTabFieldToolOutput):
    """Operation output for `move_screen_tab_field`."""
    pass

class RemoveScreenTabFieldInput(RemoveScreenTabFieldToolInput):
    """Operation input for `remove_screen_tab_field`."""
    pass

class RemoveScreenTabFieldOutput(RemoveScreenTabFieldToolOutput):
    """Operation output for `remove_screen_tab_field`."""
    pass

class JiraScreenTabFieldResource(BaseResourceClient):
    """Operations for the `screen_tab_field` resource."""

    @operation(
        name='add_screen_tab_field',
        title='AddScreenTabField',
        input_model=AddScreenTabFieldInput,
        output_model=AddScreenTabFieldOutput,
        tools_used=('add_screen_tab_field',),
        tags=tuple(['Screen tab fields']),
    )
    async def add(self, data: AddScreenTabFieldInput) -> AddScreenTabFieldOutput:
        """Adds a field to a screen tab. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: screen_id, tab_id, body"""
        tool = self._client.get_tool('add_screen_tab_field')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddScreenTabFieldOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='move_screen_tab_field',
        title='MoveScreenTabField',
        input_model=MoveScreenTabFieldInput,
        output_model=MoveScreenTabFieldOutput,
        tools_used=('move_screen_tab_field',),
        tags=tuple(['Screen tab fields']),
    )
    async def move(self, data: MoveScreenTabFieldInput) -> MoveScreenTabFieldOutput:
        """Moves a screen tab field. If `after` and `position` are provided in the request, `position` is ignored. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: screen_id, tab_id, id, body"""
        tool = self._client.get_tool('move_screen_tab_field')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MoveScreenTabFieldOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='remove_screen_tab_field',
        title='RemoveScreenTabField',
        input_model=RemoveScreenTabFieldInput,
        output_model=RemoveScreenTabFieldOutput,
        tools_used=('remove_screen_tab_field',),
        tags=tuple(['Screen tab fields']),
    )
    async def remove(self, data: RemoveScreenTabFieldInput) -> RemoveScreenTabFieldOutput:
        """Removes a field from a screen tab. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: screen_id, tab_id, id"""
        tool = self._client.get_tool('remove_screen_tab_field')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemoveScreenTabFieldOutput.model_validate(coerce_tool_result(result))
