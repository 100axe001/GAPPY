from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetFeaturesForProjectToolInput, GetFeaturesForProjectToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetFeaturesForProjectInput(GetFeaturesForProjectToolInput):
    """Operation input for `get_features_for_project`."""
    pass

class GetFeaturesForProjectOutput(GetFeaturesForProjectToolOutput):
    """Operation output for `get_features_for_project`."""
    pass

class JiraFeaturesForProjectResource(BaseResourceClient):
    """Operations for the `features_for_project` resource."""

    @operation(
        name='get_features_for_project',
        title='GetFeaturesForProject',
        input_model=GetFeaturesForProjectInput,
        output_model=GetFeaturesForProjectOutput,
        tools_used=('get_features_for_project',),
        tags=tuple(['Project features']),
    )
    async def get(self, data: GetFeaturesForProjectInput) -> GetFeaturesForProjectOutput:
        """Returns the list of features for a project.

Important inputs: project_id_or_key"""
        tool = self._client.get_tool('get_features_for_project')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetFeaturesForProjectOutput.model_validate(coerce_tool_result(result))
