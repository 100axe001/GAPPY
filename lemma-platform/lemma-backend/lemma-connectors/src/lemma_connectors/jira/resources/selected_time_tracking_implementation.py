from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetSelectedTimeTrackingImplementationToolInput, GetSelectedTimeTrackingImplementationToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetSelectedTimeTrackingImplementationInput(GetSelectedTimeTrackingImplementationToolInput):
    """Operation input for `get_selected_time_tracking_implementation`."""
    pass

class GetSelectedTimeTrackingImplementationOutput(GetSelectedTimeTrackingImplementationToolOutput):
    """Operation output for `get_selected_time_tracking_implementation`."""
    pass

class JiraSelectedTimeTrackingImplementationResource(BaseResourceClient):
    """Operations for the `selected_time_tracking_implementation` resource."""

    @operation(
        name='get_selected_time_tracking_implementation',
        title='GetSelectedTimeTrackingImplementation',
        input_model=GetSelectedTimeTrackingImplementationInput,
        output_model=GetSelectedTimeTrackingImplementationOutput,
        tools_used=('get_selected_time_tracking_implementation',),
        tags=tuple(['Time tracking']),
    )
    async def get(self, data: GetSelectedTimeTrackingImplementationInput) -> GetSelectedTimeTrackingImplementationOutput:
        """Returns the time tracking provider that is currently selected. Note that if time tracking is disabled, then a successful but empty response is returned. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_selected_time_tracking_implementation')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetSelectedTimeTrackingImplementationOutput.model_validate(coerce_tool_result(result))
