from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetProjectComponentsToolInput, GetProjectComponentsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProjectComponentsInput(GetProjectComponentsToolInput):
    """Operation input for `get_project_components`."""
    pass

class GetProjectComponentsOutput(GetProjectComponentsToolOutput):
    """Operation output for `get_project_components`."""
    pass

class JiraProjectComponentsResource(BaseResourceClient):
    """Operations for the `project_components` resource."""

    @operation(
        name='get_project_components',
        title='GetProjectComponents',
        input_model=GetProjectComponentsInput,
        output_model=GetProjectComponentsOutput,
        tools_used=('get_project_components',),
        tags=tuple(['Project components']),
    )
    async def get(self, data: GetProjectComponentsInput) -> GetProjectComponentsOutput:
        """Returns all components in a project. See the [Get project components paginated](#api-rest-api-3-project-projectIdOrKey-component-get) resource if you want to get a full list of components with pagination. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

Important inputs: project_id_or_key"""
        tool = self._client.get_tool('get_project_components')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectComponentsOutput.model_validate(coerce_tool_result(result))
