from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateScreenToolInput, CreateScreenToolOutput, DeleteScreenToolInput, DeleteScreenToolOutput, UpdateScreenToolInput, UpdateScreenToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateScreenInput(CreateScreenToolInput):
    """Operation input for `create_screen`."""
    pass

class CreateScreenOutput(CreateScreenToolOutput):
    """Operation output for `create_screen`."""
    pass

class DeleteScreenInput(DeleteScreenToolInput):
    """Operation input for `delete_screen`."""
    pass

class DeleteScreenOutput(DeleteScreenToolOutput):
    """Operation output for `delete_screen`."""
    pass

class UpdateScreenInput(UpdateScreenToolInput):
    """Operation input for `update_screen`."""
    pass

class UpdateScreenOutput(UpdateScreenToolOutput):
    """Operation output for `update_screen`."""
    pass

class JiraScreenResource(BaseResourceClient):
    """Operations for the `screen` resource."""

    @operation(
        name='create_screen',
        title='CreateScreen',
        input_model=CreateScreenInput,
        output_model=CreateScreenOutput,
        tools_used=('create_screen',),
        tags=tuple(['Screens']),
    )
    async def create(self, data: CreateScreenInput) -> CreateScreenOutput:
        """Creates a screen with a default field tab. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_screen')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateScreenOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_screen',
        title='DeleteScreen',
        input_model=DeleteScreenInput,
        output_model=DeleteScreenOutput,
        tools_used=('delete_screen',),
        tags=tuple(['Screens']),
    )
    async def delete(self, data: DeleteScreenInput) -> DeleteScreenOutput:
        """Deletes a screen. A screen cannot be deleted if it is used in a screen scheme, workflow, or workflow draft. Only screens used in classic projects can be deleted.

Important inputs: screen_id"""
        tool = self._client.get_tool('delete_screen')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteScreenOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_screen',
        title='UpdateScreen',
        input_model=UpdateScreenInput,
        output_model=UpdateScreenOutput,
        tools_used=('update_screen',),
        tags=tuple(['Screens']),
    )
    async def update(self, data: UpdateScreenInput) -> UpdateScreenOutput:
        """Updates a screen. Only screens used in classic projects can be updated. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: screen_id, body"""
        tool = self._client.get_tool('update_screen')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateScreenOutput.model_validate(coerce_tool_result(result))
