from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAvailableTimeTrackingImplementationsToolInput, GetAvailableTimeTrackingImplementationsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAvailableTimeTrackingImplementationsInput(GetAvailableTimeTrackingImplementationsToolInput):
    """Operation input for `get_available_time_tracking_implementations`."""
    pass

class GetAvailableTimeTrackingImplementationsOutput(GetAvailableTimeTrackingImplementationsToolOutput):
    """Operation output for `get_available_time_tracking_implementations`."""
    pass

class JiraAvailableTimeTrackingImplementationsResource(BaseResourceClient):
    """Operations for the `available_time_tracking_implementations` resource."""

    @operation(
        name='get_available_time_tracking_implementations',
        title='GetAvailableTimeTrackingImplementations',
        input_model=GetAvailableTimeTrackingImplementationsInput,
        output_model=GetAvailableTimeTrackingImplementationsOutput,
        tools_used=('get_available_time_tracking_implementations',),
        tags=tuple(['Time tracking']),
    )
    async def get(self, data: GetAvailableTimeTrackingImplementationsInput) -> GetAvailableTimeTrackingImplementationsOutput:
        """Returns all time tracking providers. By default, Jira only has one time tracking provider: *JIRA provided time tracking*. However, you can install other time tracking providers via apps from the Atlassian Marketplace. For more information on time tracking providers, see the documentation for the [ Time Tracking Provider](https://developer.atlassian.com/cloud/jira/platform/modules/time-tracking-provider/) module. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_available_time_tracking_implementations')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAvailableTimeTrackingImplementationsOutput.model_validate(coerce_tool_result(result))
