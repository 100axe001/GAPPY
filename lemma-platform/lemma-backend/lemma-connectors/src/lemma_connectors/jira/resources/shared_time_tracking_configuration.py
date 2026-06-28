from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetSharedTimeTrackingConfigurationToolInput, GetSharedTimeTrackingConfigurationToolOutput, SetSharedTimeTrackingConfigurationToolInput, SetSharedTimeTrackingConfigurationToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetSharedTimeTrackingConfigurationInput(GetSharedTimeTrackingConfigurationToolInput):
    """Operation input for `get_shared_time_tracking_configuration`."""
    pass

class GetSharedTimeTrackingConfigurationOutput(GetSharedTimeTrackingConfigurationToolOutput):
    """Operation output for `get_shared_time_tracking_configuration`."""
    pass

class SetSharedTimeTrackingConfigurationInput(SetSharedTimeTrackingConfigurationToolInput):
    """Operation input for `set_shared_time_tracking_configuration`."""
    pass

class SetSharedTimeTrackingConfigurationOutput(SetSharedTimeTrackingConfigurationToolOutput):
    """Operation output for `set_shared_time_tracking_configuration`."""
    pass

class JiraSharedTimeTrackingConfigurationResource(BaseResourceClient):
    """Operations for the `shared_time_tracking_configuration` resource."""

    @operation(
        name='get_shared_time_tracking_configuration',
        title='GetSharedTimeTrackingConfiguration',
        input_model=GetSharedTimeTrackingConfigurationInput,
        output_model=GetSharedTimeTrackingConfigurationOutput,
        tools_used=('get_shared_time_tracking_configuration',),
        tags=tuple(['Time tracking']),
    )
    async def get(self, data: GetSharedTimeTrackingConfigurationInput) -> GetSharedTimeTrackingConfigurationOutput:
        """Returns the time tracking settings. This includes settings such as the time format, default time unit, and others. For more information, see [Configuring time tracking](https://confluence.atlassian.com/x/qoXKM). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_shared_time_tracking_configuration')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetSharedTimeTrackingConfigurationOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_shared_time_tracking_configuration',
        title='SetSharedTimeTrackingConfiguration',
        input_model=SetSharedTimeTrackingConfigurationInput,
        output_model=SetSharedTimeTrackingConfigurationOutput,
        tools_used=('set_shared_time_tracking_configuration',),
        tags=tuple(['Time tracking']),
    )
    async def set(self, data: SetSharedTimeTrackingConfigurationInput) -> SetSharedTimeTrackingConfigurationOutput:
        """Sets the time tracking settings. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('set_shared_time_tracking_configuration')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetSharedTimeTrackingConfigurationOutput.model_validate(coerce_tool_result(result))
