from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateProjectCategoryToolInput, CreateProjectCategoryToolOutput, RemoveProjectCategoryToolInput, RemoveProjectCategoryToolOutput, UpdateProjectCategoryToolInput, UpdateProjectCategoryToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateProjectCategoryInput(CreateProjectCategoryToolInput):
    """Operation input for `create_project_category`."""
    pass

class CreateProjectCategoryOutput(CreateProjectCategoryToolOutput):
    """Operation output for `create_project_category`."""
    pass

class RemoveProjectCategoryInput(RemoveProjectCategoryToolInput):
    """Operation input for `remove_project_category`."""
    pass

class RemoveProjectCategoryOutput(RemoveProjectCategoryToolOutput):
    """Operation output for `remove_project_category`."""
    pass

class UpdateProjectCategoryInput(UpdateProjectCategoryToolInput):
    """Operation input for `update_project_category`."""
    pass

class UpdateProjectCategoryOutput(UpdateProjectCategoryToolOutput):
    """Operation output for `update_project_category`."""
    pass

class JiraProjectCategoryResource(BaseResourceClient):
    """Operations for the `project_category` resource."""

    @operation(
        name='create_project_category',
        title='CreateProjectCategory',
        input_model=CreateProjectCategoryInput,
        output_model=CreateProjectCategoryOutput,
        tools_used=('create_project_category',),
        tags=tuple(['Project categories']),
    )
    async def create(self, data: CreateProjectCategoryInput) -> CreateProjectCategoryOutput:
        """Creates a project category. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_project_category')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateProjectCategoryOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='remove_project_category',
        title='RemoveProjectCategory',
        input_model=RemoveProjectCategoryInput,
        output_model=RemoveProjectCategoryOutput,
        tools_used=('remove_project_category',),
        tags=tuple(['Project categories']),
    )
    async def remove(self, data: RemoveProjectCategoryInput) -> RemoveProjectCategoryOutput:
        """Deletes a project category. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id"""
        tool = self._client.get_tool('remove_project_category')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemoveProjectCategoryOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_project_category',
        title='UpdateProjectCategory',
        input_model=UpdateProjectCategoryInput,
        output_model=UpdateProjectCategoryOutput,
        tools_used=('update_project_category',),
        tags=tuple(['Project categories']),
    )
    async def update(self, data: UpdateProjectCategoryInput) -> UpdateProjectCategoryOutput:
        """Updates a project category. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, body"""
        tool = self._client.get_tool('update_project_category')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateProjectCategoryOutput.model_validate(coerce_tool_result(result))
