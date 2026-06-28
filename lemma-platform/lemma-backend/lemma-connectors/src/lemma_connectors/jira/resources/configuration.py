from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetConfigurationToolInput, GetConfigurationToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetConfigurationInput(GetConfigurationToolInput):
    """Operation input for `get_configuration`."""
    pass

class GetConfigurationOutput(GetConfigurationToolOutput):
    """Operation output for `get_configuration`."""
    pass

class JiraConfigurationResource(BaseResourceClient):
    """Operations for the `configuration` resource."""

    @operation(
        name='get_configuration',
        title='GetConfiguration',
        input_model=GetConfigurationInput,
        output_model=GetConfigurationOutput,
        tools_used=('get_configuration',),
        tags=tuple(['Jira settings']),
    )
    async def get(self, data: GetConfigurationInput) -> GetConfigurationOutput:
        """Returns the [global settings](https://confluence.atlassian.com/x/qYXKM) in Jira. These settings determine whether optional features (for example, subtasks, time tracking, and others) are enabled. If time tracking is enabled, this operation also returns the time tracking configuration. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_configuration')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetConfigurationOutput.model_validate(coerce_tool_result(result))
