from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllAccessibleProjectTypesToolInput, GetAllAccessibleProjectTypesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllAccessibleProjectTypesInput(GetAllAccessibleProjectTypesToolInput):
    """Operation input for `get_all_accessible_project_types`."""
    pass

class GetAllAccessibleProjectTypesOutput(GetAllAccessibleProjectTypesToolOutput):
    """Operation output for `get_all_accessible_project_types`."""
    pass

class JiraAllAccessibleProjectTypesResource(BaseResourceClient):
    """Operations for the `all_accessible_project_types` resource."""

    @operation(
        name='get_all_accessible_project_types',
        title='GetAllAccessibleProjectTypes',
        input_model=GetAllAccessibleProjectTypesInput,
        output_model=GetAllAccessibleProjectTypesOutput,
        tools_used=('get_all_accessible_project_types',),
        tags=tuple(['Project types']),
    )
    async def get(self, data: GetAllAccessibleProjectTypesInput) -> GetAllAccessibleProjectTypesOutput:
        """Returns all [project types](https://confluence.atlassian.com/x/Var1Nw) with a valid license.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_all_accessible_project_types')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllAccessibleProjectTypesOutput.model_validate(coerce_tool_result(result))
