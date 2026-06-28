from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetDefaultShareScopeToolInput, GetDefaultShareScopeToolOutput, SetDefaultShareScopeToolInput, SetDefaultShareScopeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetDefaultShareScopeInput(GetDefaultShareScopeToolInput):
    """Operation input for `get_default_share_scope`."""
    pass

class GetDefaultShareScopeOutput(GetDefaultShareScopeToolOutput):
    """Operation output for `get_default_share_scope`."""
    pass

class SetDefaultShareScopeInput(SetDefaultShareScopeToolInput):
    """Operation input for `set_default_share_scope`."""
    pass

class SetDefaultShareScopeOutput(SetDefaultShareScopeToolOutput):
    """Operation output for `set_default_share_scope`."""
    pass

class JiraDefaultShareScopeResource(BaseResourceClient):
    """Operations for the `default_share_scope` resource."""

    @operation(
        name='get_default_share_scope',
        title='GetDefaultShareScope',
        input_model=GetDefaultShareScopeInput,
        output_model=GetDefaultShareScopeOutput,
        tools_used=('get_default_share_scope',),
        tags=tuple(['Filter sharing']),
    )
    async def get(self, data: GetDefaultShareScopeInput) -> GetDefaultShareScopeOutput:
        """Returns the default sharing settings for new filters and dashboards for a user. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_default_share_scope')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetDefaultShareScopeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_default_share_scope',
        title='SetDefaultShareScope',
        input_model=SetDefaultShareScopeInput,
        output_model=SetDefaultShareScopeOutput,
        tools_used=('set_default_share_scope',),
        tags=tuple(['Filter sharing']),
    )
    async def set(self, data: SetDefaultShareScopeInput) -> SetDefaultShareScopeOutput:
        """Sets the default sharing for new filters and dashboards for a user. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: body"""
        tool = self._client.get_tool('set_default_share_scope')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetDefaultShareScopeOutput.model_validate(coerce_tool_result(result))
