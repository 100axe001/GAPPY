from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreatePriorityToolInput, CreatePriorityToolOutput, DeletePriorityToolInput, DeletePriorityToolOutput, GetPriorityToolInput, GetPriorityToolOutput, UpdatePriorityToolInput, UpdatePriorityToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreatePriorityInput(CreatePriorityToolInput):
    """Operation input for `create_priority`."""
    pass

class CreatePriorityOutput(CreatePriorityToolOutput):
    """Operation output for `create_priority`."""
    pass

class DeletePriorityInput(DeletePriorityToolInput):
    """Operation input for `delete_priority`."""
    pass

class DeletePriorityOutput(DeletePriorityToolOutput):
    """Operation output for `delete_priority`."""
    pass

class GetPriorityInput(GetPriorityToolInput):
    """Operation input for `get_priority`."""
    pass

class GetPriorityOutput(GetPriorityToolOutput):
    """Operation output for `get_priority`."""
    pass

class UpdatePriorityInput(UpdatePriorityToolInput):
    """Operation input for `update_priority`."""
    pass

class UpdatePriorityOutput(UpdatePriorityToolOutput):
    """Operation output for `update_priority`."""
    pass

class JiraPriorityResource(BaseResourceClient):
    """Operations for the `priority` resource."""

    @operation(
        name='create_priority',
        title='CreatePriority',
        input_model=CreatePriorityInput,
        output_model=CreatePriorityOutput,
        tools_used=('create_priority',),
        tags=tuple(['Issue priorities']),
    )
    async def create(self, data: CreatePriorityInput) -> CreatePriorityOutput:
        """Creates an issue priority. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_priority')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreatePriorityOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_priority',
        title='DeletePriority',
        input_model=DeletePriorityInput,
        output_model=DeletePriorityOutput,
        tools_used=('delete_priority',),
        tags=tuple(['Issue priorities']),
    )
    async def delete(self, data: DeletePriorityInput) -> DeletePriorityOutput:
        """Deletes an issue priority. This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain subsequent updates. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, replace_with"""
        tool = self._client.get_tool('delete_priority')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeletePriorityOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_priority',
        title='GetPriority',
        input_model=GetPriorityInput,
        output_model=GetPriorityOutput,
        tools_used=('get_priority',),
        tags=tuple(['Issue priorities']),
    )
    async def get(self, data: GetPriorityInput) -> GetPriorityOutput:
        """Returns an issue priority. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: id"""
        tool = self._client.get_tool('get_priority')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetPriorityOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_priority',
        title='UpdatePriority',
        input_model=UpdatePriorityInput,
        output_model=UpdatePriorityOutput,
        tools_used=('update_priority',),
        tags=tuple(['Issue priorities']),
    )
    async def update(self, data: UpdatePriorityInput) -> UpdatePriorityOutput:
        """Updates an issue priority. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('update_priority')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdatePriorityOutput.model_validate(coerce_tool_result(result))
