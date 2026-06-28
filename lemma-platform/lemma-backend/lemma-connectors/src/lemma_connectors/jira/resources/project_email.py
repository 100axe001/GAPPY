from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetProjectEmailToolInput, GetProjectEmailToolOutput, UpdateProjectEmailToolInput, UpdateProjectEmailToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProjectEmailInput(GetProjectEmailToolInput):
    """Operation input for `get_project_email`."""
    pass

class GetProjectEmailOutput(GetProjectEmailToolOutput):
    """Operation output for `get_project_email`."""
    pass

class UpdateProjectEmailInput(UpdateProjectEmailToolInput):
    """Operation input for `update_project_email`."""
    pass

class UpdateProjectEmailOutput(UpdateProjectEmailToolOutput):
    """Operation output for `update_project_email`."""
    pass

class JiraProjectEmailResource(BaseResourceClient):
    """Operations for the `project_email` resource."""

    @operation(
        name='get_project_email',
        title='GetProjectEmail',
        input_model=GetProjectEmailInput,
        output_model=GetProjectEmailOutput,
        tools_used=('get_project_email',),
        tags=tuple(['Project email']),
    )
    async def get(self, data: GetProjectEmailInput) -> GetProjectEmailOutput:
        """Returns the [project's sender email address](https://confluence.atlassian.com/x/dolKLg). **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

Important inputs: project_id"""
        tool = self._client.get_tool('get_project_email')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectEmailOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_project_email',
        title='UpdateProjectEmail',
        input_model=UpdateProjectEmailInput,
        output_model=UpdateProjectEmailOutput,
        tools_used=('update_project_email',),
        tags=tuple(['Project email']),
    )
    async def update(self, data: UpdateProjectEmailInput) -> UpdateProjectEmailOutput:
        """Sets the [project's sender email address](https://confluence.atlassian.com/x/dolKLg). If `emailAddress` is an empty string, the default email address is restored. **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

Important inputs: project_id, body"""
        tool = self._client.get_tool('update_project_email')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateProjectEmailOutput.model_validate(coerce_tool_result(result))
