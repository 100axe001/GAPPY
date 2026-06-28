from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllProjectTypesToolInput, GetAllProjectTypesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllProjectTypesInput(GetAllProjectTypesToolInput):
    """Operation input for `get_all_project_types`."""
    pass

class GetAllProjectTypesOutput(GetAllProjectTypesToolOutput):
    """Operation output for `get_all_project_types`."""
    pass

class JiraAllProjectTypesResource(BaseResourceClient):
    """Operations for the `all_project_types` resource."""

    @operation(
        name='get_all_project_types',
        title='GetAllProjectTypes',
        input_model=GetAllProjectTypesInput,
        output_model=GetAllProjectTypesOutput,
        tools_used=('get_all_project_types',),
        tags=tuple(['Project types']),
    )
    async def get(self, data: GetAllProjectTypesInput) -> GetAllProjectTypesOutput:
        """Returns all [project types](https://confluence.atlassian.com/x/Var1Nw), whether or not the instance has a valid license for each type. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_all_project_types')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllProjectTypesOutput.model_validate(coerce_tool_result(result))
