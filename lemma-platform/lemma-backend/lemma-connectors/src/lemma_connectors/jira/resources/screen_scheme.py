from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateScreenSchemeToolInput, CreateScreenSchemeToolOutput, DeleteScreenSchemeToolInput, DeleteScreenSchemeToolOutput, UpdateScreenSchemeToolInput, UpdateScreenSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateScreenSchemeInput(CreateScreenSchemeToolInput):
    """Operation input for `create_screen_scheme`."""
    pass

class CreateScreenSchemeOutput(CreateScreenSchemeToolOutput):
    """Operation output for `create_screen_scheme`."""
    pass

class DeleteScreenSchemeInput(DeleteScreenSchemeToolInput):
    """Operation input for `delete_screen_scheme`."""
    pass

class DeleteScreenSchemeOutput(DeleteScreenSchemeToolOutput):
    """Operation output for `delete_screen_scheme`."""
    pass

class UpdateScreenSchemeInput(UpdateScreenSchemeToolInput):
    """Operation input for `update_screen_scheme`."""
    pass

class UpdateScreenSchemeOutput(UpdateScreenSchemeToolOutput):
    """Operation output for `update_screen_scheme`."""
    pass

class JiraScreenSchemeResource(BaseResourceClient):
    """Operations for the `screen_scheme` resource."""

    @operation(
        name='create_screen_scheme',
        title='CreateScreenScheme',
        input_model=CreateScreenSchemeInput,
        output_model=CreateScreenSchemeOutput,
        tools_used=('create_screen_scheme',),
        tags=tuple(['Screen schemes']),
    )
    async def create(self, data: CreateScreenSchemeInput) -> CreateScreenSchemeOutput:
        """Creates a screen scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_screen_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateScreenSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_screen_scheme',
        title='DeleteScreenScheme',
        input_model=DeleteScreenSchemeInput,
        output_model=DeleteScreenSchemeOutput,
        tools_used=('delete_screen_scheme',),
        tags=tuple(['Screen schemes']),
    )
    async def delete(self, data: DeleteScreenSchemeInput) -> DeleteScreenSchemeOutput:
        """Deletes a screen scheme. A screen scheme cannot be deleted if it is used in an issue type screen scheme. Only screens schemes used in classic projects can be deleted. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: screen_scheme_id"""
        tool = self._client.get_tool('delete_screen_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteScreenSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_screen_scheme',
        title='UpdateScreenScheme',
        input_model=UpdateScreenSchemeInput,
        output_model=UpdateScreenSchemeOutput,
        tools_used=('update_screen_scheme',),
        tags=tuple(['Screen schemes']),
    )
    async def update(self, data: UpdateScreenSchemeInput) -> UpdateScreenSchemeOutput:
        """Updates a screen scheme. Only screen schemes used in classic projects can be updated. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: screen_scheme_id, body"""
        tool = self._client.get_tool('update_screen_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateScreenSchemeOutput.model_validate(coerce_tool_result(result))
