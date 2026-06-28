from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateResolutionToolInput, CreateResolutionToolOutput, DeleteResolutionToolInput, DeleteResolutionToolOutput, GetResolutionToolInput, GetResolutionToolOutput, UpdateResolutionToolInput, UpdateResolutionToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateResolutionInput(CreateResolutionToolInput):
    """Operation input for `create_resolution`."""
    pass

class CreateResolutionOutput(CreateResolutionToolOutput):
    """Operation output for `create_resolution`."""
    pass

class DeleteResolutionInput(DeleteResolutionToolInput):
    """Operation input for `delete_resolution`."""
    pass

class DeleteResolutionOutput(DeleteResolutionToolOutput):
    """Operation output for `delete_resolution`."""
    pass

class GetResolutionInput(GetResolutionToolInput):
    """Operation input for `get_resolution`."""
    pass

class GetResolutionOutput(GetResolutionToolOutput):
    """Operation output for `get_resolution`."""
    pass

class UpdateResolutionInput(UpdateResolutionToolInput):
    """Operation input for `update_resolution`."""
    pass

class UpdateResolutionOutput(UpdateResolutionToolOutput):
    """Operation output for `update_resolution`."""
    pass

class JiraResolutionResource(BaseResourceClient):
    """Operations for the `resolution` resource."""

    @operation(
        name='create_resolution',
        title='CreateResolution',
        input_model=CreateResolutionInput,
        output_model=CreateResolutionOutput,
        tools_used=('create_resolution',),
        tags=tuple(['Issue resolutions']),
    )
    async def create(self, data: CreateResolutionInput) -> CreateResolutionOutput:
        """Creates an issue resolution. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_resolution')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateResolutionOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_resolution',
        title='DeleteResolution',
        input_model=DeleteResolutionInput,
        output_model=DeleteResolutionOutput,
        tools_used=('delete_resolution',),
        tags=tuple(['Issue resolutions']),
    )
    async def delete(self, data: DeleteResolutionInput) -> DeleteResolutionOutput:
        """Deletes an issue resolution. This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, replace_with"""
        tool = self._client.get_tool('delete_resolution')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteResolutionOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_resolution',
        title='GetResolution',
        input_model=GetResolutionInput,
        output_model=GetResolutionOutput,
        tools_used=('get_resolution',),
        tags=tuple(['Issue resolutions']),
    )
    async def get(self, data: GetResolutionInput) -> GetResolutionOutput:
        """Returns an issue resolution value. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: id"""
        tool = self._client.get_tool('get_resolution')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetResolutionOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_resolution',
        title='UpdateResolution',
        input_model=UpdateResolutionInput,
        output_model=UpdateResolutionOutput,
        tools_used=('update_resolution',),
        tags=tuple(['Issue resolutions']),
    )
    async def update(self, data: UpdateResolutionInput) -> UpdateResolutionOutput:
        """Updates an issue resolution. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('update_resolution')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateResolutionOutput.model_validate(coerce_tool_result(result))
