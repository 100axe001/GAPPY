from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAdvancedSettingsToolInput, GetAdvancedSettingsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAdvancedSettingsInput(GetAdvancedSettingsToolInput):
    """Operation input for `get_advanced_settings`."""
    pass

class GetAdvancedSettingsOutput(GetAdvancedSettingsToolOutput):
    """Operation output for `get_advanced_settings`."""
    pass

class JiraAdvancedSettingsResource(BaseResourceClient):
    """Operations for the `advanced_settings` resource."""

    @operation(
        name='get_advanced_settings',
        title='GetAdvancedSettings',
        input_model=GetAdvancedSettingsInput,
        output_model=GetAdvancedSettingsOutput,
        tools_used=('get_advanced_settings',),
        tags=tuple(['Jira settings']),
    )
    async def get(self, data: GetAdvancedSettingsInput) -> GetAdvancedSettingsOutput:
        """Returns the application properties that are accessible on the *Advanced Settings* page. To navigate to the *Advanced Settings* page in Jira, choose the Jira icon > **Jira settings** > **System**, **General Configuration** and then click **Advanced Settings** (in the upper right). **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_advanced_settings')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAdvancedSettingsOutput.model_validate(coerce_tool_result(result))
