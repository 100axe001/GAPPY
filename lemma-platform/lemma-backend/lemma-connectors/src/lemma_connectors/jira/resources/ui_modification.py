from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateUiModificationToolInput, CreateUiModificationToolOutput, DeleteUiModificationToolInput, DeleteUiModificationToolOutput, UpdateUiModificationToolInput, UpdateUiModificationToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateUiModificationInput(CreateUiModificationToolInput):
    """Operation input for `create_ui_modification`."""
    pass

class CreateUiModificationOutput(CreateUiModificationToolOutput):
    """Operation output for `create_ui_modification`."""
    pass

class DeleteUiModificationInput(DeleteUiModificationToolInput):
    """Operation input for `delete_ui_modification`."""
    pass

class DeleteUiModificationOutput(DeleteUiModificationToolOutput):
    """Operation output for `delete_ui_modification`."""
    pass

class UpdateUiModificationInput(UpdateUiModificationToolInput):
    """Operation input for `update_ui_modification`."""
    pass

class UpdateUiModificationOutput(UpdateUiModificationToolOutput):
    """Operation output for `update_ui_modification`."""
    pass

class JiraUiModificationResource(BaseResourceClient):
    """Operations for the `ui_modification` resource."""

    @operation(
        name='create_ui_modification',
        title='CreateUiModification',
        input_model=CreateUiModificationInput,
        output_model=CreateUiModificationOutput,
        tools_used=('create_ui_modification',),
        tags=tuple(['UI modifications (apps)']),
    )
    async def create(self, data: CreateUiModificationInput) -> CreateUiModificationOutput:
        """Creates a UI modification. UI modification can only be created by Forge apps. Each app can define up to 100 UI modifications. Each UI modification can define up to 1000 contexts. **[Permissions](#permissions) required:** * *None* if the UI modification is created without contexts. * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, if the UI modification is created with contexts.

Important inputs: body"""
        tool = self._client.get_tool('create_ui_modification')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateUiModificationOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_ui_modification',
        title='DeleteUiModification',
        input_model=DeleteUiModificationInput,
        output_model=DeleteUiModificationOutput,
        tools_used=('delete_ui_modification',),
        tags=tuple(['UI modifications (apps)']),
    )
    async def delete(self, data: DeleteUiModificationInput) -> DeleteUiModificationOutput:
        """Deletes a UI modification. All the contexts that belong to the UI modification are deleted too. UI modification can only be deleted by Forge apps. **[Permissions](#permissions) required:** None.

Important inputs: ui_modification_id"""
        tool = self._client.get_tool('delete_ui_modification')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteUiModificationOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_ui_modification',
        title='UpdateUiModification',
        input_model=UpdateUiModificationInput,
        output_model=UpdateUiModificationOutput,
        tools_used=('update_ui_modification',),
        tags=tuple(['UI modifications (apps)']),
    )
    async def update(self, data: UpdateUiModificationInput) -> UpdateUiModificationOutput:
        """Updates a UI modification. UI modification can only be updated by Forge apps. Each UI modification can define up to 1000 contexts. **[Permissions](#permissions) required:** * *None* if the UI modification is created without contexts. * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, if the UI modification is created with contexts.

Important inputs: ui_modification_id, body"""
        tool = self._client.get_tool('update_ui_modification')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateUiModificationOutput.model_validate(coerce_tool_result(result))
