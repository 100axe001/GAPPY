from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddScreenTabToolInput, AddScreenTabToolOutput, DeleteScreenTabToolInput, DeleteScreenTabToolOutput, MoveScreenTabToolInput, MoveScreenTabToolOutput, RenameScreenTabToolInput, RenameScreenTabToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddScreenTabInput(AddScreenTabToolInput):
    """Operation input for `add_screen_tab`."""
    pass

class AddScreenTabOutput(AddScreenTabToolOutput):
    """Operation output for `add_screen_tab`."""
    pass

class DeleteScreenTabInput(DeleteScreenTabToolInput):
    """Operation input for `delete_screen_tab`."""
    pass

class DeleteScreenTabOutput(DeleteScreenTabToolOutput):
    """Operation output for `delete_screen_tab`."""
    pass

class MoveScreenTabInput(MoveScreenTabToolInput):
    """Operation input for `move_screen_tab`."""
    pass

class MoveScreenTabOutput(MoveScreenTabToolOutput):
    """Operation output for `move_screen_tab`."""
    pass

class RenameScreenTabInput(RenameScreenTabToolInput):
    """Operation input for `rename_screen_tab`."""
    pass

class RenameScreenTabOutput(RenameScreenTabToolOutput):
    """Operation output for `rename_screen_tab`."""
    pass

class JiraScreenTabResource(BaseResourceClient):
    """Operations for the `screen_tab` resource."""

    @operation(
        name='add_screen_tab',
        title='AddScreenTab',
        input_model=AddScreenTabInput,
        output_model=AddScreenTabOutput,
        tools_used=('add_screen_tab',),
        tags=tuple(['Screen tabs']),
    )
    async def add(self, data: AddScreenTabInput) -> AddScreenTabOutput:
        """Creates a tab for a screen. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: screen_id, body"""
        tool = self._client.get_tool('add_screen_tab')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddScreenTabOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_screen_tab',
        title='DeleteScreenTab',
        input_model=DeleteScreenTabInput,
        output_model=DeleteScreenTabOutput,
        tools_used=('delete_screen_tab',),
        tags=tuple(['Screen tabs']),
    )
    async def delete(self, data: DeleteScreenTabInput) -> DeleteScreenTabOutput:
        """Deletes a screen tab. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: screen_id, tab_id"""
        tool = self._client.get_tool('delete_screen_tab')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteScreenTabOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='move_screen_tab',
        title='MoveScreenTab',
        input_model=MoveScreenTabInput,
        output_model=MoveScreenTabOutput,
        tools_used=('move_screen_tab',),
        tags=tuple(['Screen tabs']),
    )
    async def move(self, data: MoveScreenTabInput) -> MoveScreenTabOutput:
        """Moves a screen tab. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: screen_id, tab_id, pos"""
        tool = self._client.get_tool('move_screen_tab')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MoveScreenTabOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='rename_screen_tab',
        title='RenameScreenTab',
        input_model=RenameScreenTabInput,
        output_model=RenameScreenTabOutput,
        tools_used=('rename_screen_tab',),
        tags=tuple(['Screen tabs']),
    )
    async def rename(self, data: RenameScreenTabInput) -> RenameScreenTabOutput:
        """Updates the name of a screen tab. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: screen_id, tab_id, body"""
        tool = self._client.get_tool('rename_screen_tab')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RenameScreenTabOutput.model_validate(coerce_tool_result(result))
