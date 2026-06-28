from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateComponentToolInput, CreateComponentToolOutput, DeleteComponentToolInput, DeleteComponentToolOutput, GetComponentToolInput, GetComponentToolOutput, UpdateComponentToolInput, UpdateComponentToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateComponentInput(CreateComponentToolInput):
    """Operation input for `create_component`."""
    pass

class CreateComponentOutput(CreateComponentToolOutput):
    """Operation output for `create_component`."""
    pass

class DeleteComponentInput(DeleteComponentToolInput):
    """Operation input for `delete_component`."""
    pass

class DeleteComponentOutput(DeleteComponentToolOutput):
    """Operation output for `delete_component`."""
    pass

class GetComponentInput(GetComponentToolInput):
    """Operation input for `get_component`."""
    pass

class GetComponentOutput(GetComponentToolOutput):
    """Operation output for `get_component`."""
    pass

class UpdateComponentInput(UpdateComponentToolInput):
    """Operation input for `update_component`."""
    pass

class UpdateComponentOutput(UpdateComponentToolOutput):
    """Operation output for `update_component`."""
    pass

class JiraComponentResource(BaseResourceClient):
    """Operations for the `component` resource."""

    @operation(
        name='create_component',
        title='CreateComponent',
        input_model=CreateComponentInput,
        output_model=CreateComponentOutput,
        tools_used=('create_component',),
        tags=tuple(['Project components']),
    )
    async def create(self, data: CreateComponentInput) -> CreateComponentOutput:
        """Creates a component. Use components to provide containers for issues within a project. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project in which the component is created or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_component')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateComponentOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_component',
        title='DeleteComponent',
        input_model=DeleteComponentInput,
        output_model=DeleteComponentOutput,
        tools_used=('delete_component',),
        tags=tuple(['Project components']),
    )
    async def delete(self, data: DeleteComponentInput) -> DeleteComponentOutput:
        """Deletes a component. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the component or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, move_issues_to"""
        tool = self._client.get_tool('delete_component')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteComponentOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_component',
        title='GetComponent',
        input_model=GetComponentInput,
        output_model=GetComponentOutput,
        tools_used=('get_component',),
        tags=tuple(['Project components']),
    )
    async def get(self, data: GetComponentInput) -> GetComponentOutput:
        """Returns a component. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for project containing the component.

Important inputs: id"""
        tool = self._client.get_tool('get_component')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetComponentOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_component',
        title='UpdateComponent',
        input_model=UpdateComponentInput,
        output_model=UpdateComponentOutput,
        tools_used=('update_component',),
        tags=tuple(['Project components']),
    )
    async def update(self, data: UpdateComponentInput) -> UpdateComponentOutput:
        """Updates a component. Any fields included in the request are overwritten. If `leadAccountId` is an empty string ("") the component lead is removed. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the component or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('update_component')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateComponentOutput.model_validate(coerce_tool_result(result))
