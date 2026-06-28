from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import ToggleFeatureForProjectToolInput, ToggleFeatureForProjectToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ToggleFeatureForProjectInput(ToggleFeatureForProjectToolInput):
    """Operation input for `toggle_feature_for_project`."""
    pass

class ToggleFeatureForProjectOutput(ToggleFeatureForProjectToolOutput):
    """Operation output for `toggle_feature_for_project`."""
    pass

class JiraToggleFeatureForResource(BaseResourceClient):
    """Operations for the `toggle_feature_for` resource."""

    @operation(
        name='toggle_feature_for_project',
        title='ToggleFeatureForProject',
        input_model=ToggleFeatureForProjectInput,
        output_model=ToggleFeatureForProjectOutput,
        tools_used=('toggle_feature_for_project',),
        tags=tuple(['Project features']),
    )
    async def project(self, data: ToggleFeatureForProjectInput) -> ToggleFeatureForProjectOutput:
        """Sets the state of a project feature.

Important inputs: project_id_or_key, feature_key, body"""
        tool = self._client.get_tool('toggle_feature_for_project')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ToggleFeatureForProjectOutput.model_validate(coerce_tool_result(result))
