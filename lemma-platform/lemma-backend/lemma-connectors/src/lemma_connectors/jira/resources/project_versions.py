from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetProjectVersionsToolInput, GetProjectVersionsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetProjectVersionsInput(GetProjectVersionsToolInput):
    """Operation input for `get_project_versions`."""
    pass

class GetProjectVersionsOutput(GetProjectVersionsToolOutput):
    """Operation output for `get_project_versions`."""
    pass

class JiraProjectVersionsResource(BaseResourceClient):
    """Operations for the `project_versions` resource."""

    @operation(
        name='get_project_versions',
        title='GetProjectVersions',
        input_model=GetProjectVersionsInput,
        output_model=GetProjectVersionsOutput,
        tools_used=('get_project_versions',),
        tags=tuple(['Project versions']),
    )
    async def get(self, data: GetProjectVersionsInput) -> GetProjectVersionsOutput:
        """Returns all versions in a project. The response is not paginated. Use [Get project versions paginated](#api-rest-api-3-project-projectIdOrKey-version-get) if you want to get the versions in a project with pagination. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

Important inputs: project_id_or_key, expand"""
        tool = self._client.get_tool('get_project_versions')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetProjectVersionsOutput.model_validate(coerce_tool_result(result))
